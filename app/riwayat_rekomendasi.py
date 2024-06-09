import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error

def riwayat_rekomendasi():
    st.title('Riwayat Rekomendasi')
    
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )

    # Variabel Streamlit untuk mendapatkan input dari pengguna
    nama_kombinasi_preference = st.text_input('Nama Kombinasi Preference')
    id_warna_1_preference = st.text_input('ID Warna 1 Preference')
    id_warna_2_preference = st.text_input('ID Warna 2 Preference')
    style_desain_preference = st.multiselect(
        "Pilih preferensi style desain:", 
        ["American Classic", "Tradisional", "Modern", "Industrial", "Alam"], 
        key='style_desain'
    )
    makna_warna_preference = st.multiselect(
        "Pilih preferensi makna warna:", 
        ["Suci", "Kekuatan", "Keceriaan", "Keberanian", "Keagungan", "Santai", "Ketenangan", "Kenyamanan", "Kerendahan hati", "Kewanitaan", "Kejantanan", "Kehangatan"], 
        key='makna_warna'
    )
    sifat_preference = st.multiselect(
        "Pilih preferensi sifat:", 
        ["Panas", "Hangat", "Dingin"], 
        key='sifat'
    )
    usia_pengguna_preference = st.multiselect(
        "Pilih preferensi usia pengguna:", 
        ["Anak-anak (5-11 tahun)", "Remaja (12-25 tahun)", "Dewasa (26-45 tahun)", "Lansia (<45 tahun)"], 
        key='usia_pengguna'
    )
    warna_dasar_preference = st.multiselect(
        "Pilih preferensi warna dasar:", 
        ["Putih", "Hitam", "Merah", "Kuning", "Biru"], 
        key='warna_dasar'
    )

    # Fungsi untuk menyimpan data ke dalam database MySQL
    def save_to_db(nama_kombinasi, id_warna_1, id_warna_2, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Membuat tabel jika belum ada
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS riwayat_rekomendasi (
                    id_riwayat INT AUTO_INCREMENT PRIMARY KEY,
                    nama_kombinasi TEXT,
                    id_warna_1 TEXT,
                    id_warna_2 TEXT,
                    style_desain TEXT,
                    makna_warna TEXT,
                    sifat TEXT,
                    usia_pengguna TEXT,
                    warna_dasar TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
                ''')
                
                # Memasukkan data ke dalam tabel
                cursor.execute('''
                INSERT INTO riwayat_rekomendasi (nama_kombinasi, id_warna_1, id_warna_2, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    nama_kombinasi,
                    id_warna_1,
                    id_warna_2,
                    ', '.join(style_desain),
                    ', '.join(makna_warna),
                    ', '.join(sifat),
                    ', '.join(usia_pengguna),
                    ', '.join(warna_dasar)
                ))
                
                conn.commit()
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Tombol untuk menyimpan data
    if st.button('Simpan Preferensi'):
        save_to_db(
            nama_kombinasi_preference,
            id_warna_1_preference,
            id_warna_2_preference,
            style_desain_preference,
            makna_warna_preference,
            sifat_preference,
            usia_pengguna_preference,
            warna_dasar_preference
        )
        st.success('Preferensi berhasil disimpan ke dalam database.')
    
    # Menampilkan data dari tabel
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )
    if conn.is_connected():
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM riwayat_rekomendasi")
        result = mycursor.fetchall()

        columns = [i[0] for i in mycursor.description]
        df = pd.DataFrame(result, columns=columns)
        st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        
        mycursor.close()
        conn.close()

