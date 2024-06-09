from itertools import combinations
import streamlit as st

class ColorItem:
    def __init__(self, nama_warna ,style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        self.nama_warna = nama_warna
        self.style_desain = style_desain
        self.makna_warna = makna_warna
        self.sifat = sifat
        self.usia_pengguna = usia_pengguna
        self.warna_dasar = warna_dasar

# Definisi color_database
color_database = [
    ColorItem("Putih", ["American Classic", "Tradisional", "Industrial", "Minimalis", "Alam"], ["Suci", "Bersih"], "Dingin", ["Remaja", "Lansia"], "Putih"),
    ColorItem("Hitam", "Industrial", "Kekuatan", "Panas", ["R", "D"], "Hitam"),
    ColorItem("Merah", "American Classic", "Keberanian", "Panas", ["A", "R", "D"], "Merah"),
    ColorItem("Ungu", "Modern", "Keagungan", "Dingin", ["A", "R", "D"], ["Merah", "Biru"]),
    ColorItem("Hijau","Alam", "Santai", "Dingin", ["A", "R", "D", "L"], ["Kuning", "Biru"]),
    ColorItem("Biru","Alam", "Ketenangan", "Dingin", ["A", "R", "D", "L"], "Biru"),
    ColorItem("Oren","American Classic", "Keceriaan", "Panas", ["A", "R", "D", "L"], ["Merah", "Kuning"]),
    ColorItem("Coklat", ["Tradisional", "Alam"], "Kenyamanan", "Hangat", ["R", "L"], ["Merah", "Biru", "Kuning"]),
    ColorItem("Grey", "Industrial", "Kerendahan hati", "Dingin", ["R", "D", "L"], ["Hitam", "Putih"]),
    ColorItem("Pink", "Modern", "Kewanitaan", "Panas", ["A", "R", "D"], ["Merah", "Putih"]),
    ColorItem("Dark red", "Modern", "Keberanian", "Panas", ["R", "L"], ["Merah", "Hitam"]),
    ColorItem("Dark blue", "Alam", "Ketenangan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Hitam"]),
    ColorItem("Dark grey", "Industrial", "Kerendahan hati", "Panas", ["D", "R", "L"], ["Putih", "Hitam"]),
    ColorItem("Dark green", "Alam", "Santai", "Dingin", ["L"], ["Hijau", "Hitam"]),
    ColorItem("Dark brown", ["Tradisional", "Alam"], "Kejantanan", "Hangat", ["L"], ["Merah", "Biru", "Kuning"]),
    ColorItem("Light brown", ["American Classic", "Tradisional", "Alam"], "Kejantanan", "Hangat", ["L"], ["Merah", "Biru", "Kuning"]),
    ColorItem("Light blue", ["American Classic", "Alam"], "Kewanitaan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Putih"]),
    ColorItem("Light grey", "Industrial", "Kerendahan hati", "Dingin", ["R", "D", "L"], ["Hitam", "Putih"]),
    ColorItem("Light green", ["American Classic", "Alam"], "Kewanitaan", "Hangat", ["A", "R", "D", "L"], ["Biru", "Kuning"]),
    ColorItem("Magenta", ["American Classic", "Modern"], "Kewanitaan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Merah", "Putih"]),
    ColorItem("Gold", "American Classic", "Keagungan", "Panas", ["A", "R", "D", "L"], ["Merah", "Biru", "Kuning"]),
    ColorItem("Navy blue", "Alam", "Ketenangan", "Dingin", ["A", "R", "D", "L"], None),
    ColorItem("Maroon", ["Tradisional", "Alam"], "Keceriaan", "Panas", ["R", "D", "L"], ["Merah", "Biru", "Kuning"]),
    ColorItem("Peach", ["American Classic", "Modern"], "Kewanitaan", "Hangat", ["R", "D", "L"], ["Merah", "Kuning", "Putih"]),
    ColorItem("Silver", "Industrial", "Ketenangan", "Dingin", ["R", "D", "L"], ["Hitam", "Putih"]),
    ColorItem("Coral", "American Classic", "Kewanitaan", "Panas", ["A", "R", "D", "L"], ["Merah", "Kuning"]),
    ColorItem("Aqua", ["American Classic", "Alam"], "Ketenangan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Putih"]),
    ColorItem("Khaki", "American Classic", "Kehangatan", "Hangat", ["R", "D", "L"], ["Merah", "Biru", "Kuning"]),
    ColorItem("Olive", "Alam", "Kejantanan", "Dingin", ["L"], ["Biru", "Kuning", "Putih"])

]  

def recommend_color(style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference):
    recommendations = []
    
    # Buat semua kombinasi dua warna dari color_database
    color_combinations = generate_color_combinations(color_database)
    
    for combination in color_combinations:
        style_desain_score = calculate_score(style_desain_preference, combination.style_desain)
        makna_warna_score = calculate_score(makna_warna_preference, combination.makna_warna)
        sifat_score = calculate_score(sifat_preference, combination.sifat)
        usia_pengguna_score = calculate_score(usia_pengguna_preference, combination.usia_pengguna)
        warna_dasar_score = calculate_score(warna_dasar_preference, combination.warna_dasar)
        
        total_score = (0.35 * style_desain_score +
                       0.25 * makna_warna_score +
                       0.25 * sifat_score +
                       0.1 * usia_pengguna_score +
                       0.05 * warna_dasar_score)
        
        recommendations.append((combination.nama_warna, total_score))
    
    # Menghilangkan rekomendasi warna yang hanya memiliki satu warna dasar
    recommendations = [rec for rec in recommendations if len(rec[0].split('+')) > 1]
    
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

def generate_color_combinations(color_database):
    color_combinations = []
    for color1, color2 in combinations(color_database, 2):
        combined_style_desain = list(set(color1.style_desain + color2.style_desain))
        combined_makna_warna = list(set(color1.makna_warna + color2.makna_warna))
        combined_sifat = list(set(color1.sifat + color2.sifat))
        combined_usia_pengguna = list(set(color1.usia_pengguna + color2.usia_pengguna))
        combined_warna_dasar = list(set(color1.warna_dasar + color2.warna_dasar))
        color_combinations.append(ColorItem(f"{color1.nama_warna} + {color2.nama_warna}",
                                             combined_style_desain,
                                             combined_makna_warna,
                                             combined_sifat,
                                             combined_usia_pengguna,
                                             combined_warna_dasar))
    return color_combinations

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
