import streamlit as st
import mysql.connector
import os
import time
import pickle
from pathlib import Path
from app.home import home
from app.pilih_rekomendasi import pilih_rekomendasi
from app.daftar_rekomendasi import daftar_rekomendasi
from app.riwayat_rekomendasi import riwayat_rekomendasi
from app.edit_rekomendasi import edit_rekomendasi
from app.hapus_rekomendasi import hapus_rekomendasi
from app.daftar_user import daftar_user

# Fungsi utama
def main():
    st.set_page_config(
        page_title="My Streamlit App",
        layout="wide",  # Set layout to wide mode
        initial_sidebar_state="auto",  # Sidebar initial state
    )

    # Path ke file penyimpanan username
    user_home_dir = Path.home()
    file_path = user_home_dir / 'user_login.pkl'

    # Inisialisasi session_state
    if 'user' not in st.session_state:
        st.session_state.user = {'username': None, 'role': None}
    if 'login' not in st.session_state:
        st.session_state.login = False

    # Fungsi untuk membuat koneksi ke database
    def create_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )

    # Fungsi untuk memeriksa login
    def check_login(username, password):
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT username, password, role FROM user WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            if user and user["password"] == password:
                return user["role"]
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    # Cek apakah file login ada, jika ada baca username dari file
    if file_path.exists():
        with open(file_path, 'rb') as file:
            username = pickle.load(file)
            conn = create_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT role FROM user WHERE username = %s", (username,))
            role = cursor.fetchone()["role"]
            cursor.close()
            conn.close()
            st.session_state.user = {'username': username, 'role': role}
            st.session_state.login = True

    # Tampilkan form login jika belum login
    if not st.session_state.login:
        with st.container():
            col1, col2 = st.columns([3, 2])
            with col1:
                st.header('Hai, Selamat Datang di NuansaDesain')
                st.subheader('Silahkan Login')
                username = st.text_input("Username:")
                password = st.text_input("Password:", type="password")
                if st.button("Login"):
                    role = check_login(username, password)
                    if role:
                        st.session_state.user = {'username': username, 'role': role}
                        st.session_state.login = True
                        with open(file_path, 'wb') as file:
                            pickle.dump(username, file)
                        st.success("Login berhasil")
                        time.sleep(2)
                        st.experimental_rerun()
                    else:
                        st.error("Login gagal. Silakan coba lagi.")
            with col2:
                st.image('data/warna/Warni.png')

    # Jika sudah login, tampilkan halaman setelah login
    if st.session_state.login:
        username = st.session_state.user['username']
        role = st.session_state.user['role']
        st.sidebar.title(f'Hai, {username}!')
        
        if role == 'Admin':
            opsi = st.sidebar.radio("Pilih Halaman", ['Beranda', 'Pilih Rekomendasi', 'Daftar Rekomendasi', 'Riwayat Rekomendasi', 'Edit Rekomendasi', 'Hapus Rekomendasi', 'Daftar User'])
        else:
            opsi = st.sidebar.radio("Pilih Halaman", ['Beranda', 'Pilih Rekomendasi', 'Daftar Rekomendasi', 'Riwayat Rekomendasi'])

        # Konten utama
        if opsi == "Beranda":
            home()
        elif opsi == "Pilih Rekomendasi":
            pilih_rekomendasi()
        elif opsi == 'Daftar Rekomendasi':
            daftar_rekomendasi()
        elif opsi == 'Riwayat Rekomendasi':
            riwayat_rekomendasi()
        elif opsi == 'Edit Rekomendasi':
            edit_rekomendasi()
        elif opsi == 'Hapus Rekomendasi':
            hapus_rekomendasi()
        elif opsi == 'Daftar User':
            daftar_user()
        # elif opsi == 'Daftar User Baru':
        #     daftar_user_baru()

        if st.sidebar.button("Logout"):
            st.session_state.login = False
            st.session_state.user = {'username': None, 'role': None}
            st.success("Logout berhasil!")
            if file_path.exists():
                file_path.unlink()
            time.sleep(2)
            st.experimental_rerun()

if __name__ == '__main__':
    main()

