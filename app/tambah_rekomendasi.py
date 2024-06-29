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

    def save_to_db(nama, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                
                
                # Memasukkan data ke dalam tabel
                cursor.execute('''
                INSERT INTO data_warna (warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''', (
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

    col1, col2 = st.columns(2)
    col1.subheader("Masukkan Preferensi")
    nama = col1.text_input("Masukkan nama warna:")
    style_desain_preference = col1.multiselect("Pilih preferensi style desain:", ["American Classic", "Tradisional", "Modern", "Industrial", "Alam"])
    makna_warna_preference = col1.multiselect("Pilih preferensi makna warna:", ["Suci", "Kekuatan", "Keceriaan", "Keberanian", "Keagungan", "Santai", "Ketenangan", "Kenyamanan", "Kerendahan hati", "Kewanitaan", "Kejantanan", "Kehangatan"])
    sifat_preference = col1.multiselect("Pilih preferensi sifat:", ["Panas", "Hangat", "Dingin"])
    usia_pengguna_display = col1.multiselect("Pilih preferensi usia pengguna:", ["Anak-anak (5-11 tahun)", "Remaja (12-25 tahun)", "Dewasa (26-45 tahun)", "Lansia (<45 tahun)"])

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

    warna_dasar_preference = col1.multiselect("Pilih preferensi warna dasar:", ["Putih", "Hitam", "Merah", "Kuning", "Biru"])

    if 'daftar_rekomendasi' not in st.session_state:
        st.session_state.daftar_rekomendasi = []

    if col1.button('Simpan Warna'):
        save_to_db(
                    nama,
                    style_desain_preference,
                    makna_warna_preference,
                    sifat_preference,
                    usia_pengguna_preference,
                    warna_dasar_preference
                )