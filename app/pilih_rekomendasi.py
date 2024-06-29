import streamlit as st
import pandas as pd
import os
import mysql.connector
from mysql.connector import Error

def pilih_rekomendasi():
    st.title('Pilih Rekomendasi Warna')
    
    # Fungsi untuk membuat koneksi ke database
    def create_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )

    conn = create_connection()

    def recommend_color(style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference):
        def convert_to_list(value):
            if isinstance(value, str):
                return [item.strip() for item in value.split(',')]
            else:
                return value

        color_data = pd.read_csv("data/kombinasi_warna.csv", converters={
            'style_desain': convert_to_list,
            'makna_warna': convert_to_list,
            'sifat': convert_to_list,
            'usia_pengguna': convert_to_list,
            'warna_dasar': convert_to_list
        })

        color_database = color_data.values.tolist()
        recommendations = []
        for item in color_database:
            style_desain_score = calculate_score(style_desain_preference, item[1])
            makna_warna_score = calculate_score(makna_warna_preference, item[2])
            sifat_score = calculate_score(sifat_preference, item[3])
            usia_pengguna_score = calculate_score(usia_pengguna_preference, item[4])
            warna_dasar_score = calculate_score(warna_dasar_preference, item[5])
            
            total_score = (0.35 * style_desain_score +
                           0.25 * makna_warna_score +
                           0.25 * sifat_score +
                           0.1 * usia_pengguna_score +
                           0.05 * warna_dasar_score)
            
            item_scores = {
                'style_desain': style_desain_score,
                'makna_warna': makna_warna_score,
                'sifat': sifat_score,
                'usia_pengguna': usia_pengguna_score,
                'warna_dasar': warna_dasar_score
            }
            
            recommendations.append((item[0], total_score, item_scores))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations

    def calculate_score(user_preference, item_attribute):
        if isinstance(item_attribute, list):
            num_values = len(item_attribute)
            match_count = sum(1 for value in item_attribute if value in user_preference)
            return match_count / num_values if num_values > 0 else 0
        else:
            return 1 if item_attribute in user_preference else 0
    
    def save_to_db(nama_kombinasi, id_warna_1, id_warna_2, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        user = st.session_state.user['username']
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Membuat tabel jika belum ada
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS riwayat_rekomendasi (
                    id_riwayat INT AUTO_INCREMENT PRIMARY KEY,
                    nama_kombinasi TEXT,
                    user TEXT,
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
                INSERT INTO riwayat_rekomendasi (nama_kombinasi, user, id_warna_1, id_warna_2, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    nama_kombinasi,
                    user,
                    id_warna_1,
                    id_warna_2,
                    ', '.join(style_desain),
                    ', '.join(makna_warna),
                    ', '.join(sifat),
                    ', '.join(usia_pengguna),
                    ', '.join(warna_dasar)
                ))
                
                conn.commit()
                st.success("Rekomendasi berhasil disimpan ke database.")
            else:
                st.error("Koneksi ke database gagal.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()

    current_page = 'pilih_rekomendasi'
    if 'last_page' not in st.session_state or st.session_state.last_page != current_page:
        st.session_state.clear()
        st.session_state.last_page = current_page

    if 'has_cari_rekomendasi' not in st.session_state:
        st.session_state.has_cari_rekomendasi = False

    col1, col2 = st.columns(2)
    col1.subheader("Masukkan Preferensi")
    
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

    if col1.button('Cari Rekomendasi'):
        st.session_state.has_cari_rekomendasi = True

    if st.session_state.has_cari_rekomendasi:   
        col2.subheader("Hasil Rekomendasi")
        recommendations = recommend_color(style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference)

        top_recommendations = recommendations[:5]

        col2.text("Top 5 Rekomendasi Pemilihan Rekomendasi Warna:")

        for i, (nama_warna, score, item_scores) in enumerate(top_recommendations, start=1):
            col2.text(f"Rekomendasi {i}: {nama_warna} (Skor: {score})")
            col2.text(f" - Skor Style Desain: {item_scores['style_desain']}")
            col2.text(f" - Skor Makna Warna: {item_scores['makna_warna']}")
            col2.text(f" - Skor Sifat: {item_scores['sifat']}")
            col2.text(f" - Skor Usia Pengguna: {item_scores['usia_pengguna']}")
            col2.text(f" - Skor Warna Dasar: {item_scores['warna_dasar']}")

            warna_terpisah = [warna.strip() for warna in nama_warna.split('&')]
            cols = col2.columns(len(warna_terpisah))
            for col, warna in zip(cols, warna_terpisah):
                path_to_color_image = os.path.join("data", "warna", f"{warna}.jpg")
                if os.path.exists(path_to_color_image):
                    col.image(path_to_color_image, caption=warna, use_column_width=True)
                else:
                    col.warning(f"Image for {warna} not found!")

        pilihan = [i+1 for i in range(len(top_recommendations))]
        index_rekomendasi = col1.radio("Pilih satu opsi:", pilihan, key="options")
        if col1.button('Simpan Rekomendasi'):
            if index_rekomendasi <= len(top_recommendations):
                selected_rekomendasi = top_recommendations[index_rekomendasi-1][0]
                st.session_state.daftar_rekomendasi.append(selected_rekomendasi)
                col1.success(f"Rekomendasi '{selected_rekomendasi}' telah disimpan.")
                selected_ids = selected_rekomendasi.split('&')
                id_warna_1_preference, id_warna_2_preference = selected_ids
                save_to_db(
                    selected_rekomendasi,
                    id_warna_1_preference,
                    id_warna_2_preference,
                    style_desain_preference,
                    makna_warna_preference,
                    sifat_preference,
                    usia_pengguna_preference,
                    warna_dasar_preference
                )
                st.session_state.has_cari_rekomendasi = False

