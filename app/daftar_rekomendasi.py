import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import base64

# def daftar_rekomendasi():
#     st.title('Daftar Rekomendasi Warna')

#     def fetch_data_from_db(query):
#         try:
#             conn = mysql.connector.connect(
#                 host='localhost',
#                 user='root',
#                 password='',
#                 database='db_rekomendasi'
#             )
#             cursor = conn.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()
#             columns = [i[0] for i in cursor.description]
#             df = pd.DataFrame(result, columns=columns)
#         except Error as e:
#             st.error(f"Error: {e}")
#             return pd.DataFrame()  # Return an empty DataFrame on error
#         finally:
#             if conn.is_connected():
#                 cursor.close()
#                 conn.close()
#         return df


#     # Menambahkan barisan atau informasi tambahan
#     st.markdown("""
#          <p>Berikut adalah daftar rekomendasi warna berdasarkan data yang tersedia.</p>
#     """, unsafe_allow_html=True)

#     st.subheader('Data Warna')
#     query_data_warna = "SELECT * FROM data_warna"

#     # Fetch data from database
#     df_asli = fetch_data_from_db(query_data_warna)

#     # Rename columns as needed
#     df_asli.columns = ["Id", "Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

#     # Menambahkan kolom Gambar dengan format base64
#     def get_image_base64(warna):
#         path_to_image = f'warna/{warna}.png'
#         with open(path_to_image, 'rb') as f:
#             image_bytes = f.read()
#         image_base64 = base64.b64encode(image_bytes).decode('utf-8')
#         return image_base64

#     df_asli['Gambar'] = df_asli['Warna'].apply(lambda x: f'<img src="data:image/png;base64,{get_image_base64(x)}" alt="{x}" style="width:100px;height:auto;">')

#     # Mengurutkan kolom untuk menempatkan kolom Gambar di posisi kedua
#     columns_order = ['Id', 'Gambar'] + df_asli.columns[1:7].tolist()
#     df_asli = df_asli[columns_order]

#     st.markdown(df_asli.to_html(escape=False, index=False), unsafe_allow_html=True)

#     st.subheader('Data Kombinasi')
#     query_data_kombinasi = "SELECT * FROM data_kombinasi"
#     df_kombinasi = fetch_data_from_db(query_data_kombinasi)

#     # Rename columns for data_kombinasi
#     df_kombinasi.columns = ["Id", "Kombinasi Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

#     # Menambahkan kolom Gambar dengan dua gambar dalam satu kolom
#     def get_combined_image_base64(kombinasi_warna):
#         warna_1, warna_2 = kombinasi_warna.split(' & ')
#         img1 = get_image_base64(warna_1)
#         img2 = get_image_base64(warna_2)
#         return f'<img src="data:image/png;base64,{img1}" alt="{warna_1}" style="width:50px;height:auto;">' \
#                f'<img src="data:image/png;base64,{img2}" alt="{warna_2}" style="width:50px;height:auto;">'

#     df_kombinasi['Gambar'] = df_kombinasi['Kombinasi Warna'].apply(get_combined_image_base64)

#     # Mengurutkan kolom untuk menempatkan kolom Gambar di posisi kedua
#     columns_order = ['Id', 'Gambar'] + df_kombinasi.columns[1:7].tolist()
#     df_kombinasi = df_kombinasi[columns_order]

#     st.markdown(df_kombinasi.to_html(escape=False, index=False), unsafe_allow_html=True)


def daftar_rekomendasi():
    st.title('Aplikasi dengan Tab Streamlit')

    # Pilihan tab
    tabs = ["Tambah Data Warna", "Data Warna", "Data Kombinasi"]
    current_tab = st.selectbox("Pilih Halaman", tabs)

    # Menampilkan konten berdasarkan tab yang dipilih
    if current_tab == "Tambah Data Warna":
        tambah()
    elif current_tab == "Data Warna":
        data_warna()
    elif current_tab == "Data Kombinasi":
        data_kombinasi()

def tambah():
    st.header("Tambah Data Warna")
    st.write("Ini adalah konten untuk Halaman 1.")

def data_warna():
    st.header("Data Warna")
    st.write("Ini adalah konten untuk Halaman 2.")

def data_kombinasi():
    st.header("Data kombinasi")
    st.write("Ini adalah konten untuk Halaman 2.")

if __name__ == "__main__":
    daftar_rekomendasi()