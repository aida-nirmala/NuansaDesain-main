import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import base64

def daftar_rekomendasi():

    # Pilihan tab
    tabs = ["Data Warna", "Tambah Data Warna", "Data Kombinasi"]
    current_tab = st.selectbox("Pilih Halaman", tabs)

    # Menampilkan konten berdasarkan tab yang dipilih
    if current_tab == "Tambah Data Warna":
        tambah()
    elif current_tab == "Data Warna":
        data_warna()
    elif current_tab == "Data Kombinasi":
        data_kombinasi()

def data_warna():
    def fetch_data_from_db(query):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_rekomendasi'
            )
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            df = pd.DataFrame(result, columns=columns)
        except Error as e:
            st.error(f"Error: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return df
    
    st.header("Data Warna")

    # Menambahkan barisan atau informasi tambahan
    st.markdown("""
         <p>Berikut adalah daftar rekomendasi warna berdasarkan data yang tersedia.</p>
    """, unsafe_allow_html=True)

    query_data_warna = "SELECT * FROM data_warna"

    # Fetch data from database
    df_asli = fetch_data_from_db(query_data_warna)

    # Rename columns as needed
    df_asli.columns = ["ID", "Gambar", "Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]
    df_asli = df_asli.drop(columns=['Gambar'])

    # Menambahkan kolom Gambar dengan format base64
    def get_image_base64(warna):
        path_to_image = f'warna/{warna}.png'
        with open(path_to_image, 'rb') as f:
            image_bytes = f.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        return image_base64

    df_asli['Gambar'] = df_asli['Warna'].apply(lambda x: f'<img src="data:image/png;base64,{get_image_base64(x)}" alt="{x}" style="width:100px;height:auto;">')

    # Mengurutkan kolom untuk menempatkan kolom Gambar di posisi kedua
    columns_order = ['ID', 'Gambar'] + df_asli.columns[1:7].tolist()
    df_asli = df_asli[columns_order]

    st.markdown(df_asli.to_html(escape=False, index=False), unsafe_allow_html=True)

def tambah():
    st.header('Tambah Data Warna')
    
    # Fungsi untuk membuat koneksi ke database
    def create_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )

    conn = create_connection()

    def save_to_db(gambar_filename, warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Memasukkan data ke dalam tabel
                cursor.execute('''
                INSERT INTO data_warna (gambar, warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (
                    gambar_filename if gambar_filename else None,
                    warna,
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
            gambar_path = os.path.join('gambar', gambar.name)
            with open(gambar_path, "wb") as f:
                f.write(gambar.getbuffer())
            
            st.success(f"Gambar '{gambar.name}' berhasil disimpan.")
            return gambar.name
        except Exception as e:
            st.error(f"Error saat menyimpan gambar: {e}")
            return None
    
    # Input untuk gambar
    gambar = st.file_uploader("Pilih gambar untuk warna:")
    
    if gambar is not None:
        st.subheader("Gambar yang Dipilih")
        st.image(gambar, caption='Gambar yang Dipilih', use_column_width=True)
    
    warna = st.text_input("Masukkan nama warna:")
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
            warna,
            style_desain_preference,
            makna_warna_preference,
            sifat_preference,
            usia_pengguna_preference,
            warna_dasar_preference
        )

def data_kombinasi():
    def fetch_data_from_db(query):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_rekomendasi'
            )
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            df = pd.DataFrame(result, columns=columns)
        except Error as e:
            st.error(f"Error: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return df

    # Menambahkan kolom Gambar dengan format base64
    def get_image_base64(warna):
        path_to_image = f'warna/{warna}.png'
        with open(path_to_image, 'rb') as f:
            image_bytes = f.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        return image_base64

    st.header("Data Kombinasi")
    query_data_kombinasi = "SELECT * FROM data_kombinasi"
    df_kombinasi = fetch_data_from_db(query_data_kombinasi)

    # Rename columns for data_kombinasi
    df_kombinasi.columns = ["ID", "Kombinasi Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

    # Menambahkan kolom Gambar dengan dua gambar dalam satu kolom
    def get_combined_image_base64(kombinasi_warna):
        warna_1, warna_2 = kombinasi_warna.split(' & ')
        img1 = get_image_base64(warna_1)
        img2 = get_image_base64(warna_2)
        return f'<img src="data:image/png;base64,{img1}" alt="{warna_1}" style="width:50px;height:auto;">' \
               f'<img src="data:image/png;base64,{img2}" alt="{warna_2}" style="width:50px;height:auto;">'

    df_kombinasi['Gambar'] = df_kombinasi['Kombinasi Warna'].apply(get_combined_image_base64)

    # Mengurutkan kolom untuk menempatkan kolom Gambar di posisi kedua
    columns_order = ['ID', 'Gambar'] + df_kombinasi.columns[1:7].tolist()
    df_kombinasi = df_kombinasi[columns_order]

    st.markdown(df_kombinasi.to_html(escape=False, index=False), unsafe_allow_html=True)

if __name__ == "__main__":
    daftar_rekomendasi()