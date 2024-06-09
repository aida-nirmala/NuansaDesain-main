import streamlit as st
import mysql.connector
import bcrypt
import pickle
import os
import time
from pathlib import Path
from app.home import home
from app.pilih_rekomendasi import pilih_rekomendasi
from app.daftar_rekomendasi import daftar_rekomendasi
from app.riwayat_rekomendasi import riwayat_rekomendasi
from app.edit_rekomendasi import edit_rekomendasi
from app.daftar_user import daftar_user

# Fungsi utama
def main():
    st.set_page_config(
        page_title="My Streamlit App",
        layout="wide",  # Set layout to wide mode
        initial_sidebar_state="auto",  # Sidebar initial state
    )
    # Inisialisasi session_state
    if 'user' not in st.session_state:
        st.session_state.user = {'username': None}
    if 'login' not in st.session_state:
        st.session_state.login = False

    def create_connection():
        # Buat koneksi ke database MySQL Anda
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )

    def check_login(username, password):
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Query untuk mendapatkan pengguna berdasarkan username
            query = "SELECT username, password FROM user WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()

            # Memeriksa apakah pengguna ditemukan dan password cocok
            if user and user["password"] == password:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conn.close()

    # Tampilkan form login jika belum login
    if not st.session_state.login:
        with st.container():
            # Membuat dua kolom dengan rasio 3:2
            col1, col2 = st.columns([3, 2])
            with col1:
                st.header('Hai, Selamat Datang di NuansaDesain')
                st.subheader('Silahkan Login')
                username = st.text_input("Username:")
                password = st.text_input("Password:", type="password")
                if st.button("Login"):
                    # Periksa kecocokan username dan password
                    if check_login(username, password):
                        st.session_state.user = {'username': username}
                        st.session_state.login = True

                        # Simpan email ke dalam file menggunakan pickle (opsional)
                        try:
                            user_home_dir = Path.home()
                            file_path = user_home_dir / 'user_email.pkl'
                            with open(file_path, 'wb') as file:
                                pickle.dump(username, file)
                        except PermissionError:
                            pass  # Ignore the PermissionError

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
        st.sidebar.title(f'Hai, {username}!')
        opsi = st.sidebar.radio("Pilih Halaman", ['Beranda', 'Pilih Rekomendasi', 'Daftar Rekomendasi', 'Riwayat Rekomendasi', 'Edit Rekomendasi', 'Daftar User'])

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
        elif opsi == 'Daftar User':
            daftar_user()

        if st.sidebar.button("Logout"):
            # Hapus informasi pengguna dari sesi saat logout
            st.session_state.login = False
            st.success("Logout berhasil!")
            # Hapus file user_email.pkl saat logout (opsional)
            try:
                file_path = Path.home() / 'user_email.pkl'
                if file_path.exists():
                    file_path.unlink()
            except PermissionError:
                pass  # Ignore the PermissionError

            time.sleep(2)
            st.experimental_rerun()

if __name__ == '__main__':
    main()
