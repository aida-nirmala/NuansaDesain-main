import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import base64

def main():
    # Sidebar untuk navigasi halaman
    st.sidebar.title("Navigasi")
    page = st.sidebar.selectbox("Pilih halaman", ["Daftar Rekomendasi", "Tambah Data Warna"])

    if page == "Daftar Rekomendasi":
        daftar_rekomendasi()
    elif page == "Tambah Data Warna":
        tambah_data_warna()

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

def execute_db_query(query, values=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        conn.commit()
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def insert_data(table, columns, values):
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
    execute_db_query(query, values)

def daftar_rekomendasi():
    st.title('Daftar Rekomendasi Warna')

    st.subheader('Data Warna')
    query_data_warna = "SELECT * FROM data_warna"

    # Fetch data from database
    df_asli = fetch_data_from_db(query_data_warna)

    # Rename columns as needed
    df_asli.columns = ["Id", "Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

    # Menambahkan kolom Gambar dengan format base64
    def get_image_base64(warna):
        # Path ke gambar atau logika untuk mendapatkan gambar
        # Misalnya, mengambil dari direktori 'warna' dengan nama sesuai 'warna'
        # Sesuaikan ini dengan struktur direktori dan cara Anda menyimpan gambar
        path_to_image = f'warna/{warna}.png'

        # Membaca gambar dalam bentuk byte
        with open(path_to_image, 'rb') as f:
            image_bytes = f.read()

        # Mengonversi gambar ke base64
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        return image_base64

    # Menambahkan kolom Gambar dengan tag HTML img
    df_asli['Gambar'] = df_asli['Warna'].apply(lambda x: f'<img src="data:image/png;base64,{get_image_base64(x)}" alt="{x}" style="width:100px;height:auto;">')

    # Mengurutkan kolom untuk menempatkan kolom Gambar di posisi kedua
    columns_order = ['Id', 'Gambar'] + df_asli.columns[1:7].tolist()  # ['Id', 'Gambar', 'Warna', 'Style Desain', 'Makna Warna', 'Sifat', 'Usia Pengguna', 'Warna Dasar']
    df_asli = df_asli[columns_order]

    # Menampilkan DataFrame sebagai tabel di Streamlit dengan konten HTML yang diizinkan
    st.markdown(df_asli.to_html(escape=False, index=False), unsafe_allow_html=True)

    st.subheader('Data Kombinasi')
    query_data_kombinasi = "SELECT * FROM data_kombinasi"
    df_kombinasi = fetch_data_from_db(query_data_kombinasi)

    # Rename columns for data_kombinasi
    df_kombinasi.columns = ["Id", "Kombinasi Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

    st.markdown(df_kombinasi.to_html(index=False), unsafe_allow_html=True)

    if st.button('Tambah Data Warna Baru'):
        st.session_state.page = "Tambah Data Warna"

def tambah_data_warna():
    st.title('Tambah Data Warna Baru')
    with st.form(key='insert_form'):
        warna_baru = st.text_input('Nama Warna')
        style_desain = st.text_input('Style Desain')
        makna_warna = st.text_input('Makna Warna')
        sifat = st.text_input('Sifat')
        usia_pengguna = st.text_input('Usia Pengguna')
        warna_dasar = st.text_input('Warna Dasar')
        
        submit_button = st.form_submit_button(label='Tambah')
        if submit_button:
            if all([warna_baru, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar]):
                insert_data('data_kombinasi', ['nama_warna', 'style_desain', 'makna_warna', 'sifat', 'usia_pengguna', 'warna_dasar'],
                            [warna_baru, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar])
                st.success(f'Data {warna_baru} berhasil ditambahkan')
                st.session_state.page = "Daftar Rekomendasi"
                st.experimental_rerun()  # Refresh page to show updated data
            else:
                st.error('Semua field harus diisi.')

if __name__ == '__main__':
    if 'page' not in st.session_state:
        st.session_state.page = "Daftar Rekomendasi"
    main()
