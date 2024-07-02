import streamlit as st
import pandas as pd
import os
import mysql.connector
from mysql.connector import Error

def tambah_rekomendasi():
    st.title('Tambah Rekomendasi Warna')
    
    # Fungsi untuk membuat koneksi ke database
    def create_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )

    conn = create_connection()

    def save_to_db(gambar_filename, nama, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Menyimpan gambar ke direktori yang sesuai
                if gambar_filename:
                    save_image(gambar_filename)
                
                # Memasukkan data ke dalam tabel
                cursor.execute('''
                INSERT INTO data_warna (gambar, warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (
                    gambar_filename if gambar_filename else None,
                    nama,
                    ', '.join(style_desain),
                    ', '.join(makna_warna),
                    ', '.join(sifat),
                    ', '.join(usia_pengguna),
                    ', '.join(warna_dasar)
                ))
                
                conn.commit()
                st.success("Data Warna Baru berhasil disimpan ke database.")
            else:
                st.error("Koneksi ke database gagal.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()

    def save_image(gambar):
        # Simpan gambar ke direktori 'gambar'
        try:
            if not os.path.exists('gambar'):
                os.makedirs('gambar')
            
            # Simpan gambar dengan nama yang unik atau sesuai input
            with open(os.path.join('gambar', gambar.name), "wb") as f:
                f.write(gambar.getbuffer())
            
            st.success(f"Gambar '{gambar.name}' berhasil disimpan.")
            return gambar.name
        except Exception as e:
            st.error(f"Error saat menyimpan gambar: {e}")
            return None
        
    # Menampilkan gambar jika ada
    st.subheader("Masukkan Preferensi")
    
    # Input untuk gambar
    gambar = st.file_uploader("Pilih gambar untuk warna:")
    
    if gambar is not None:
        st.subheader("Gambar yang Dipilih")
        st.image(gambar, caption='Gambar yang Dipilih', use_column_width=True)
    
    nama = st.text_input("Masukkan nama warna:")
    style_desain_preference = st.multiselect("Pilih preferensi style desain:", ["American Classic", "Tradisional", "Modern", "Industrial", "Alam"])
    makna_warna_preference = st.multiselect("Pilih preferensi makna warna:", ["Suci", "Kekuatan", "Keceriaan", "Keberanian", "Keagungan", "Santai", "Ketenangan", "Kenyamanan", "Kerendahan hati", "Kewanitaan", "Kejantanan", "Kehangatan"])
    sifat_preference = st.multiselect("Pilih preferensi sifat:", ["Panas", "Hangat", "Dingin"])
    usia_pengguna_display = st.multiselect("Pilih preferensi usia pengguna:", ["Anak-anak (5-11 tahun)", "Remaja (12-25 tahun)", "Dewasa (26-45 tahun)", "Lansia (<45 tahun)"])

    usia_pengguna_preference = []
    for item in usia_pengguna_display:
        if item == "Anak-anak (5-11 tahun)":
            usia_pengguna_preference.append("A")
        elif item == "Remaja (12-25 tahun)":
            usia_pengguna_preference.append("R")
        elif item == "Dewasa (26-45 tahun)":
            usia_pengguna_preference.append("D")
        elif item == "Lansia (<45 tahun)":
            usia_pengguna_preference.append("L")

    warna_dasar_preference = st.multiselect("Pilih preferensi warna dasar:", ["Putih", "Hitam", "Merah", "Kuning", "Biru"])

    if st.button('Simpan Warna'):
        gambar_filename = None
        if gambar is not None:
            gambar_filename = save_image(gambar)
        
        save_to_db(
            gambar_filename,
            nama,
            style_desain_preference,
            makna_warna_preference,
            sifat_preference,
            usia_pengguna_preference,
            warna_dasar_preference
        )

if __name__ == "__main__":
    tambah_rekomendasi()