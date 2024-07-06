import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import base64
import os
import time
import math

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

    query_user = "SELECT * FROM data_warna"
    df_asli = fetch_data_from_db(query_user)
    st.header("Data Warna")

    # Check if DataFrame is empty
    if df_asli.empty:
        st.warning("Tidak ada data pengguna yang ditemukan.")
    else:
        # Rename columns as needed
        df_asli.columns = ["ID", "Gambar", "Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

        # Adding description after the title
        st.markdown("""
            <p>Berikut adalah daftar semua warna dasar yang terdaftar dalam sistem rekomendasi warna.</p>
        """, unsafe_allow_html=True)

        def delete_user_from_db(id_warna):
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='db_rekomendasi'
                )
                if conn.is_connected():
                    cursor = conn.cursor()
                    delete_query = "DELETE FROM data_warna WHERE id_warna = %s"
                    cursor.execute(delete_query, (id_warna,))
                    conn.commit()
                    st.success("Data warna berhasil dihapus dari database.")
                    st.session_state['delete_id'] = None  # Reset delete_id after deletion
                    time.sleep(2)
                    st.experimental_rerun()   
            except Error as e:
                st.error(f"Error: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
        
        # Inisialisasi session_state
        if 'delete_id' not in st.session_state:
            st.session_state['delete_id'] = None

        if 'confirm_delete' not in st.session_state:
            st.session_state['confirm_delete'] = False

        if st.session_state['delete_id'] is not None:
            if not st.session_state['confirm_delete']:
                st.warning(f"Apakah Anda yakin ingin menghapus user dengan ID {st.session_state['delete_id']}?")
                col_yes, col_no = st.columns(2)
                if col_yes.button("Ya"):
                    delete_user_from_db(st.session_state['delete_id'])
                if col_no.button("Batal"):
                    st.session_state['delete_id'] = None
                    st.session_state['confirm_delete'] = False
            else:
                st.warning(f"Apakah Anda yakin ingin menghapus user dengan ID {st.session_state['delete_id']}?")
                col_yes, col_no = st.columns(2)
                if col_yes.button("Ya"):
                    delete_user_from_db(st.session_state['delete_id'])
                if col_no.button("Batal"):
                    st.session_state['delete_id'] = None
                    st.session_state['confirm_delete'] = False

        # Create header columns
        header_cols = st.columns([1, 2, 2, 2, 2, 2, 2, 2, 2])
        
        headers = ["ID", "Gambar", "Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar", "Aksi"]
        for header, col in zip(headers, header_cols):
            col.write(f"**{header}**")

        df_asli = df_asli.drop(columns=['Gambar'])

        def get_image_base64(warna):
            path_to_image = f'data/warna/{warna}.jpg'
            with open(path_to_image, 'rb') as f:
                image_bytes = f.read()
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            return image_base64

        df_asli['Gambar'] = df_asli['Warna'].apply(lambda x: f'<img src="data:image/jpg;base64,{get_image_base64(x)}" alt="{x}" style="width:100px;height:auto;">')

        for index, row in df_asli.iterrows():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1, 2, 2, 2, 2, 2, 2, 2, 2])
            col1.write(row['ID'])
            col2.markdown(row['Gambar'], unsafe_allow_html=True)
            col3.write(row['Warna'])
            col4.write(row['Style Desain'])
            col5.write(row['Makna Warna'])
            col6.write(row['Sifat'])
            col7.write(row['Usia Pengguna'])
            col8.write(row['Warna Dasar'])
            if col9.button("Hapus", key=f"delete_{row['ID']}"):
                st.session_state['delete_id'] = row['ID']

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
    # Menambahkan kolom Gambar dengan format base64
    def get_image_base64(warna):
        path_to_image = f'data/warna/{warna}.jpg'
        with open(path_to_image, 'rb') as f:
            image_bytes = f.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        return image_base64

    st.header("Data Kombinasi")
    query_data_kombinasi = "SELECT * FROM data_kombinasi"
    total_items_query = "SELECT COUNT(*) FROM data_kombinasi"
    items_per_page = 10

    # Hitung total item
    total_items_df = fetch_paginated(total_items_query)
    total_items = total_items_df.iloc[0, 0] if not total_items_df.empty else 0
    total_pages = math.ceil(total_items / items_per_page)

    # Pagination
    current_page = st.selectbox("Halaman", range(1, total_pages + 1))
    offset = (current_page - 1) * items_per_page

    df_kombinasi = fetch_paginated(query_data_kombinasi, offset, items_per_page)
    
    # Rename columns as needed
    df_kombinasi.columns = ["ID", "Kombinasi Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

    # Adding description after the title
    st.markdown("""
        <p>Berikut adalah daftar semua warna kombinasi yang terdaftar dalam sistem rekomendasi warna.</p>
    """, unsafe_allow_html=True)

    def delete_user_from_db(id_kombinasi):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_rekomendasi'
            )
            if conn.is_connected():
                cursor = conn.cursor()
                delete_query = "DELETE FROM data_kombinasi WHERE id_kombinasi = %s"
                cursor.execute(delete_query, (id_kombinasi,))
                conn.commit()
                st.success("Data kombinasi berhasil dihapus dari database.")
                st.session_state['delete_id'] = None  # Reset delete_id after deletion
                time.sleep(2)
                st.experimental_rerun()   
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    # Inisialisasi session_state
    if 'delete_id' not in st.session_state:
        st.session_state['delete_id'] = None

    if 'confirm_delete' not in st.session_state:
        st.session_state['confirm_delete'] = False

    if st.session_state['delete_id'] is not None:
        if not st.session_state['confirm_delete']:
            st.warning(f"Apakah Anda yakin ingin menghapus user dengan ID {st.session_state['delete_id']}?")
            col_yes, col_no = st.columns(2)
            if col_yes.button("Ya"):
                delete_user_from_db(st.session_state['delete_id'])
            if col_no.button("Batal"):
                st.session_state['delete_id'] = None
                st.session_state['confirm_delete'] = False
        else:
            st.warning(f"Apakah Anda yakin ingin menghapus user dengan ID {st.session_state['delete_id']}?")
            col_yes, col_no = st.columns(2)
            if col_yes.button("Ya"):
                delete_user_from_db(st.session_state['delete_id'])
            if col_no.button("Batal"):
                st.session_state['delete_id'] = None
                st.session_state['confirm_delete'] = False

    # Rename columns for data_kombinasi
    df_kombinasi.columns = ["ID", "Kombinasi Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar"]

    # Create header columns
    header_cols = st.columns([1, 2, 2, 2, 2, 2, 2, 2, 2])
    
    headers = ["ID", "Gambar", "Kombinasi Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar", "Aksi"]
    for header, col in zip(headers, header_cols):
        col.write(f"**{header}**")
    
    def get_combined_image_base64(kombinasi_warna):
        warna_1, warna_2 = kombinasi_warna.split(' & ')
        img1 = get_image_base64(warna_1)
        img2 = get_image_base64(warna_2)
        return f'<img src="data:image/jpg;base64,{img1}" alt="{warna_1}" style="width:50px;height:auto;">' \
               f'<img src="data:image/jpg;base64,{img2}" alt="{warna_2}" style="width:50px;height:auto;">'

    df_kombinasi['Gambar'] = df_kombinasi['Kombinasi Warna'].apply(get_combined_image_base64)

    for index, row in df_kombinasi.iterrows():
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1, 2, 2, 2, 2, 2, 2, 2, 2])
        col1.write(row['ID'])
        col2.markdown(row['Gambar'], unsafe_allow_html=True)
        col3.write(row['Kombinasi Warna'])
        col4.write(row['Style Desain'])
        col5.write(row['Makna Warna'])
        col6.write(row['Sifat'])
        col7.write(row['Usia Pengguna'])
        col8.write(row['Warna Dasar'])
        if col9.button("Hapus", key=f"delete_{row['ID']}"):
            st.session_state['delete_id'] = row['ID']

def fetch_paginated(query, offset=0, limit=10):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_rekomendasi'
            )
            cursor = conn.cursor()
            query_with_pagination = f"{query} LIMIT {limit} OFFSET {offset}"
            cursor.execute(query_with_pagination)
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

if __name__ == "__main__":
    daftar_rekomendasi()
