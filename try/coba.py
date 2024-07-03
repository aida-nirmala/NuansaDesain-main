import streamlit as st
from app.home import home
from app.pilih_rekomendasi import pilih_rekomendasi
from app.daftar_rekomendasi_admin import daftar_rekomendasi
from app.riwayat_rekomendasi import riwayat_rekomendasi
from app.edit_rekomendasi import edit_rekomendasi
from app.daftar_user import daftar_user

def main():
    st.set_page_config(
        page_title="Aplikasi Streamlit Saya",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # Kredensial pengguna disimpan dalam dictionary
    credentials = {
        "aida": "aida123",
        "ilham": "ilham123"
    }
    
    # Membuat dua kolom dengan rasio 3:2
    col1, col2 = st.columns([3, 2])
    
    # Menambahkan konten ke dalam kolom pertama
    with col1:
        st.header('Hai, Selamat Datang di NuansaDesain')
        st.subheader('Silahkan Login')
        
        # Inisialisasi kunci session state
        if "username" not in st.session_state:
            st.session_state["username"] = ""
        if "password" not in st.session_state:
            st.session_state["password"] = ""
        if "login" not in st.session_state:
            st.session_state["login"] = False 
            
        # Fungsi untuk memeriksa kredensial pengguna
        def periksa_password():
            def password_dimasukkan():
                if st.session_state["username"] in credentials and credentials[st.session_state["username"]] == st.session_state["password"]:
                    st.session_state["login"] = True
                else:
                    st.session_state["login"] = False
                    st.error("Username atau password salah")

            if not st.session_state["login"]:
                st.text_input("Username", key="username")
                st.text_input("Password", type="password", key="password")
                st.button("Login", on_click=password_dimasukkan)

            return st.session_state["login"]
        
        # Memanggil fungsi untuk memeriksa password
        periksa_password()
    
    # Menambahkan konten ke dalam kolom kedua
    with col2:
        st.image('data/warna/Warni.png')
    
    # Fungsi untuk keluar (logout)
    def logout():
        st.session_state["login"] = False
        st.session_state["username"] = ""
        st.session_state["password"] = ""
        st.experimental_rerun()

    # Menampilkan halaman login jika belum login
    if st.session_state["login"]:
        st.write(f"Selamat datang, {st.session_state['username']}!")
        
        # Tambahkan tombol logout
        # Tempatkan konten aplikasi utama Anda di sini
        st.sidebar.title('Navigasi')
        
        # Pilihan sidebar
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

        if st.button("Logout"):
            logout()

if _name_ == "_main_":
    main()