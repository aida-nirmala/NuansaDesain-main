import streamlit as st

def pilih_rekomendasi():
    st.title('Pilih Rekomendasi Page')
    st.write('Welcome to the Pilih Rekomendasi Page!')

    # Fungsi untuk merekomendasikan warna
    def recommend_color(color_database, style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference):
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
            
            recommendations.append((item[0], total_score))
        
        # Menghilangkan rekomendasi warna yang hanya memiliki satu warna dasar
        recommendations = [rec for rec in recommendations if len(rec[0]) > 1]
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations

    # Fungsi untuk menghitung skor preferensi
    def calculate_score(user_preference, item_attribute):
        if isinstance(item_attribute, list):
            num_values = len(item_attribute)
            match_count = sum(1 for value in item_attribute if value in user_preference)
            return match_count / num_values if num_values > 0 else 0
        else:
            return 1 if item_attribute in user_preference else 0

    st.header("Rekomendasi Warna")
    st.subheader("Masukkan Preferensi")

    # Contoh database rekomendasi_warna
    color_database = [
        ("Putih", ["American Classic", "Tradisional", "Industrial", "Minimalis", "Alam"], ["Suci", "Bersih"], "Dingin", ["Remaja", "Lansia"], "Putih"),
        ("Hitam", "Industrial", "Kekuatan", "Panas", ["R", "D"], "Hitam"),
        ("Merah", "American Classic", "Keberanian", "Panas", ["A", "R", "D"], "Merah"),
        ("Ungu", "Modern", "Keagungan", "Dingin", ["A", "R", "D"], ["Merah", "Biru"]),
        ("Hijau","Alam", "Santai", "Dingin", ["A", "R", "D", "L"], ["Kuning", "Biru"]),
        ("Biru","Alam", "Ketenangan", "Dingin", ["A", "R", "D", "L"], "Biru"),
        ("Oren","American Classic", "Keceriaan", "Panas", ["A", "R", "D", "L"], ["Merah", "Kuning"]),
        ("Coklat", ["Tradisional", "Alam"], "Kenyamanan", "Hangat", ["R", "L"], ["Merah", "Biru", "Kuning"]),
        ("Grey", "Industrial", "Kerendahan hati", "Dingin", ["R", "D", "L"], ["Hitam", "Putih"]),
        ("Pink", "Modern", "Kewanitaan", "Panas", ["A", "R", "D"], ["Merah", "Putih"]),
        ("Dark red", "Modern", "Keberanian", "Panas", ["R", "L"], ["Merah", "Hitam"]),
        ("Dark blue", "Alam", "Ketenangan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Hitam"]),
        ("Dark grey", "Industrial", "Kerendahan hati", "Panas", ["D", "R", "L"], ["Putih", "Hitam"]),
        ("Dark green", "Alam", "Santai", "Dingin", ["L"], ["Hijau", "Hitam"]),
        ("Dark brown", ["Tradisional", "Alam"], "Kejantanan", "Hangat", ["L"], ["Merah", "Biru", "Kuning"]),
        ("Light brown", ["American Classic", "Tradisional", "Alam"], "Kejantanan", "Hangat", ["L"], ["Merah", "Biru", "Kuning"]),
        ("Light blue", ["American Classic", "Alam"], "Kewanitaan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Putih"]),
        ("Light grey", "Industrial", "Kerendahan hati", "Dingin", ["R", "D", "L"], ["Hitam", "Putih"]),
        ("Light green", ["American Classic", "Alam"], "Kewanitaan", "Hangat", ["A", "R", "D", "L"], ["Biru", "Kuning"]),
        ("Magenta", ["American Classic", "Modern"], "Kewanitaan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Merah", "Putih"]),
        ("Gold", "American Classic", "Keagungan", "Panas", ["A", "R", "D", "L"], ["Merah", "Biru", "Kuning"]),
        ("Navy blue", "Alam", "Ketenangan", "Dingin", ["A", "R", "D", "L"], None),
        ("Maroon", ["Tradisional", "Alam"], "Keceriaan", "Panas", ["R", "D", "L"], ["Merah", "Biru", "Kuning"]),
        ("Peach", ["American Classic", "Modern"], "Kewanitaan", "Hangat", ["R", "D", "L"], ["Merah", "Kuning", "Putih"]),
        ("Silver", "Industrial", "Ketenangan", "Dingin", ["R", "D", "L"], ["Hitam", "Putih"]),
        ("Coral", "American Classic", "Kewanitaan", "Panas", ["A", "R", "D", "L"], ["Merah", "Kuning"]),
        ("Aqua", ["American Classic", "Alam"], "Ketenangan", "Dingin", ["A", "R", "D", "L"], ["Biru", "Putih"]),
        ("Khaki", "American Classic", "Kehangatan", "Hangat", ["R", "D", "L"], ["Merah", "Biru", "Kuning"]),
        ("Olive", "Alam", "Kejantanan", "Dingin", ["L"], ["Biru", "Kuning", "Putih"])
    ]

    # Meminta input dari pengguna untuk preferensi mereka
    style_desain_preference = st.multiselect("Pilih preferensi style desain:", ["American Classic", "Tradisional", "Modern", "Industrial", "Alam"])
    makna_warna_preference = st.multiselect("Pilih preferensi makna warna:", ["Suci", "Kekuatan", "Keceriaan", "Keberanian", "Keagungan", "Santai", "Ketenangan", "Kenyamanan", "Kerendahan hati", "Kewanitaan", "Kejantanan", "Kehangatan"])
    sifat_preference = st.multiselect("Pilih preferensi sifat:", ["Dingin", "Panas", "Hangat"])
    usia_pengguna_preference = st.multiselect("Pilih preferensi usia pengguna:", ["R", "L", "A", "D"])
    warna_dasar_preference = st.multiselect("Pilih preferensi warna dasar:", ["Putih", "Hitam", "Merah", "Biru", "Kuning"])

    if st.button('Cari Rekomendasi'):   
        # Mendapatkan rekomendasi
        recommendations = recommend_color(color_database, style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference)

        # Menampilkan rekomendasi
        st.text("Rekomendasi Pemilihan Rekomendasi Warna:")
        for i, (nama_warna, score) in enumerate(recommendations, start=1):
            st.text(f"Rekomendasi {i}: {nama_warna} (Skor: {score})")

pilih_rekomendasi()
