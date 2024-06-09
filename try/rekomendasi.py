import streamlit as st
import pandas as pd

# Definisikan kelas ColorItem
class ColorItem:
    def __init__(self, nama_warna ,style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        self.nama_warna = nama_warna
        self.style_desain = style_desain
        self.makna_warna = makna_warna
        self.sifat = sifat
        self.usia_pengguna = usia_pengguna
        self.warna_dasar = warna_dasar

# Baca data warna dari file CSV
data = pd.read_csv('daftar_warna.csv')

# Inisialisasi daftar color_database
color_database = []

# Loop melalui setiap baris dalam data dan buat objek ColorItem
for index, row in data.iterrows():
    color_item = ColorItem(row['Warna'], row['Style'], row['Makna'], row['Sifat'], row['Usia'], row['Warna Dasar'])
    color_database.append(color_item)  


def recommend_color(style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference):
    recommendations = []
    for item in color_database:
        style_desain_score = calculate_score(style_desain_preference, item.style_desain)
        makna_warna_score = calculate_score(makna_warna_preference, item.makna_warna)
        sifat_score = calculate_score(sifat_preference, item.sifat)
        usia_pengguna_score = calculate_score(usia_pengguna_preference, item.usia_pengguna)
        warna_dasar_score = calculate_score(warna_dasar_preference, item.warna_dasar)
        
        total_score = (0.35 * style_desain_score +
                       0.25 * makna_warna_score +
                       0.25 * sifat_score +
                       0.1 * usia_pengguna_score +
                       0.05 * warna_dasar_score)
        
        recommendations.append((item.nama_warna, total_score))
    
    # Menghilangkan rekomendasi warna yang hanya memiliki satu warna dasar
    recommendations = [rec for rec in recommendations if len(item.warna_dasar) > 1]
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations

def calculate_score(user_preference, item_attribute):
    if isinstance(item_attribute, list):
        num_values = len(item_attribute)
        match_count = 0
        for value in item_attribute:
            if value in user_preference:
                match_count += 1
        return match_count / num_values if num_values > 0 else 0
    else:
        return 1 if item_attribute in user_preference else 0
st.header("Rekomendasi Warna")
st.subheader("Masukkan Preferensi")
# Meminta input dari pengguna untuk preferensi mereka
style_desain_preference = st.multiselect("Pilih preferensi style desain:", ["American Classic", "Tradisional", "Modern", "Industrial", "Alam"])
makna_warna_preference = st.multiselect("Pilih preferensi makna warna:", ["Suci", "Kekuatan", "Keceriaan", "Keberanian", "Keagungan", "Santai", "Ketenangan", "Kenyamanan", "Kerendahan hati", "Kewanitaan", "Kejantanan", "Kehangatan"])
sifat_preference = st.multiselect("Pilih preferensi sifat:", ["Dingin", "Panas", "Hangat"])
usia_pengguna_preference = st.multiselect("Pilih preferensi usia pengguna:", ["R", "L", "A", "D"])
warna_dasar_preference = st.multiselect("Pilih preferensi warna dasar:", ["Putih", "Hitam", "Merah", "Biru", "Kuning"])


if st.button('Cari Rekomendasi'):
        
    # Mendapatkan rekomendasi
    recommendations = recommend_color(style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference)

    # Menampilkan rekomendasi
    st.text("Rekomendasi Pemilihan Rekomendasi Warna:")
    for i, (nama_warna, score) in enumerate(recommendations, start=1):
        st.text(f"Rekomendasi {i}: {nama_warna} (Skor: {score})")
