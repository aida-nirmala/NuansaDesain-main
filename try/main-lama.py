import streamlit as st
from app.home import home
from app.pilih_rekomendasi import pilih_rekomendasi
from app.daftar_rekomendasi_admin import daftar_rekomendasi
from app.riwayat_rekomendasi import riwayat_rekomendasi
from app.edit_rekomendasi import edit_rekomendasi


def main():

    st.set_page_config(
        page_title="My Streamlit App",
        layout="wide",  # Set layout to wide mode
        initial_sidebar_state="auto",  # Sidebar initial state
    )
    
    st.sidebar.title('Navigation')
    # Pilihan sidebar
    option = st.sidebar.radio("Go to", ['Home', 'Pilih Rekomendasi', 'Daftar Rekomendasi', 'Riwayat Rekomendasi', 'Edit Rekomendasi'])

    # Konten utama
    if option == "Home":
        home()

    elif option == "Pilih Rekomendasi":
        pilih_rekomendasi()
        
    elif option == 'Daftar Rekomendasi':
        daftar_rekomendasi()

    elif option == 'Riwayat Rekomendasi':
        riwayat_rekomendasi()
        
    elif option == 'Edit Rekomendasi':
        edit_rekomendasi()

if __name__ == "__main__":

    main()
