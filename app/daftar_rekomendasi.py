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
    def handle_tab_change():
        st.session_state['current_tab'] = None
        if 'edit_triggered' in st.session_state and st.session_state['edit_triggered']:
            st.session_state['current_tab'] = "Edit Warna"

    tabs = ["Data Warna", "Tambah Data Warna", "Data Kombinasi"]

    current_tab = "Data Warna"
    if st.session_state.get("current_tab") in tabs:
        current_tab = st.selectbox("Pilih Halaman", tabs, on_change=handle_tab_change())

    active = st.session_state.get("current_tab", current_tab)

    if active is None:
        active = current_tab
        st.session_state['current_tab'] = active

    # Menampilkan konten berdasarkan tab yang dipilih
    if active == "Tambah Data Warna":
        tambah()
    elif active == "Data Warna":
        data_warna()
    elif active == "Data Kombinasi":
        data_kombinasi()
    elif active == "Edit Warna":
        edit_id = st.session_state['edit_id']
        edit_warna(edit_id)

def data_warna():
    st.header("Data Warna")
    
    query_user = "SELECT * FROM data_warna"
    total_items_query = "SELECT COUNT(*) FROM data_warna"
    items_per_page = 10

    # Hitung total item
    total_items_df = fetch_paginated(total_items_query)
    total_items = total_items_df.iloc[0, 0] if not total_items_df.empty else 0
    total_pages = math.ceil(total_items / items_per_page)

    # Pagination
    current_page = st.selectbox("Halaman", range(1, total_pages + 1))
    offset = (current_page - 1) * items_per_page

    df_asli = fetch_paginated(query_user, offset, items_per_page)

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

        def delete_warna_from_db(id_warna):
            try:
                conn = create_connection()
                if conn.is_connected():
                    cursor = conn.cursor()

                    # Cek nama warna yang akan dihapus
                    warna = fetch(f"SELECT warna FROM data_warna WHERE id_warna = {id_warna}")

                    # Hapus data dari tabel data_kombinasi
                    delete_query_kombinasi = f"DELETE FROM data_kombinasi WHERE kombinasi_warna LIKE '{warna[0][0]} &%' OR kombinasi_warna LIKE '%& {warna[0][0]}'"
                    cursor.execute(delete_query_kombinasi)

                    # Hapus data dari tabel data_warna
                    delete_query = "DELETE FROM data_warna WHERE id_warna = %s"
                    cursor.execute(delete_query, (id_warna, ))

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
                st.warning(f"Apakah Anda yakin ingin menghapus warna dengan ID {st.session_state['delete_id']}?")
                col_yes, col_no = st.columns(2)
                if col_yes.button("Ya"):
                    delete_warna_from_db(st.session_state['delete_id'])
                if col_no.button("Batal"):
                    st.session_state['delete_id'] = None
                    st.session_state['confirm_delete'] = False
            else:
                st.warning(f"Apakah Anda yakin ingin menghapus warna dengan ID {st.session_state['delete_id']}?")
                col_yes, col_no = st.columns(2)
                if col_yes.button("Ya"):
                    delete_warna_from_db(st.session_state['delete_id'])
                if col_no.button("Batal"):
                    st.session_state['delete_id'] = None
                    st.session_state['confirm_delete'] = False

        # Create header columns
        header_cols = st.columns([1, 2, 2, 2, 2, 2, 2, 2, 2])
        
        headers = ["ID", "Gambar", "Warna", "Style Desain", "Makna Warna", "Sifat", "Usia Pengguna", "Warna Dasar", "Aksi"]
        for header, col in zip(headers, header_cols):
            col.write(f"**{header}**")

        def get_image_base64(path_to_image):
            with open(path_to_image, 'rb') as f:
                image_bytes = f.read()
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            return image_base64
        
        df_asli["Gambar"] = df_asli["Gambar"].apply(lambda x: f'data/warna/{x}' if x else 'data/warna/default.jpg')
        df_asli["Gambar"] = df_asli["Gambar"].apply(lambda x: f'<img src="data:image/jpg;base64,{get_image_base64(x)}" alt="{x}" style="width:100px;height:auto;">')

        for index, row in df_asli.iterrows():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([1, 2, 2, 2, 2, 2, 2, 2, 1, 1])
            col1.write(row['ID'])
            col2.markdown(row['Gambar'], unsafe_allow_html=True)
            col3.write(row['Warna'])
            col4.write(row['Style Desain'])
            col5.write(row['Makna Warna'])
            col6.write(row['Sifat'])
            col7.write(row['Usia Pengguna'])
            col8.write(row['Warna Dasar'])
            if col9.button("Edit", key=f"edit_{row['ID']}"):
                st.session_state['edit_triggered'] = True
                st.session_state['edit_id'] = row['ID']
                st.session_state['current_tab'] = "Edit Warna"
                st.experimental_rerun()
            if col10.button("Hapus", key=f"delete_{row['ID']}"):
                st.session_state['delete_id'] = row['ID']

def tambah():
    st.header('Tambah Data Warna')

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

        existing_colors = fetch(f"SELECT warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar FROM data_warna WHERE warna != '{warna}'")
        save_combinations(existing_colors, warna, style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference)

def data_kombinasi():
    # Menambahkan kolom Gambar dengan format base64
    def get_image_base64(path_to_image):
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

        data_warna_1 = fetch(f"SELECT gambar FROM data_warna WHERE warna = '{warna_1}'")
        data_warna_2 = fetch(f"SELECT gambar FROM data_warna WHERE warna = '{warna_2}'")

        if not data_warna_1 or not data_warna_2:
            return None
        
        path_gambar_1 = 'data/warna/' + data_warna_1[0][0] if data_warna_1[0][0] else 'data/warna/default.jpg'
        path_gambar_2 = 'data/warna/' + data_warna_2[0][0] if data_warna_2[0][0] else 'data/warna/default.jpg'

        img1 = get_image_base64(path_gambar_1)
        img2 = get_image_base64(path_gambar_2)
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

def edit_warna(id):
    st.header("Edit Warna")

    query = f"SELECT * FROM data_warna WHERE id_warna = {id}"
    result = fetch(query)

    gambar = st.file_uploader("Pilih gambar untuk warna: (kosongkan jika tidak ingin mengubah)")
    if gambar is not None:
        st.subheader("Gambar yang Dipilih")
        st.image(gambar, caption='Gambar yang Dipilih', use_column_width=True)
    elif result[0][1] is not None:
        st.subheader("Gambar saat ini")
        st.image(f"data/warna/{result[0][1]}", caption='Gambar saat ini', use_column_width=True)

    warna = st.text_input("Masukkan nama warna:", result[0][2])
    style_desain_preference = st.multiselect("Pilih preferensi style desain:", ["American Classic", "Tradisional", "Modern", "Industrial", "Alam", "Minimalis"], result[0][3].split(', '))
    makna_warna_preference = st.multiselect("Pilih preferensi makna warna:", ["Suci", "Kekuatan", "Keceriaan", "Keberanian", "Keagungan", "Santai", "Ketenangan", "Kenyamanan", "Kerendahan hati", "Kewanitaan", "Kejantanan", "Kehangatan"], result[0][4].split(', '))
    sifat_preference = st.multiselect("Pilih preferensi sifat:", ["Panas", "Hangat", "Dingin"], result[0][5].split(', '))

    existing_usia = result[0][6].split(', ')
    selected_usia = []
    for item in existing_usia:
        if item == "A":
            selected_usia.append("Anak-anak (5-11 tahun)")
        elif item == "R":
            selected_usia.append("Remaja (12-25 tahun)")
        elif item == "D":
            selected_usia.append("Dewasa (26-45 tahun)")
        elif item == "L":
            selected_usia.append("Lansia (<45 tahun)")

    usia_pengguna_display = st.multiselect("Pilih preferensi usia pengguna:", ["Anak-anak (5-11 tahun)", "Remaja (12-25 tahun)", "Dewasa (26-45 tahun)", "Lansia (<45 tahun)"], selected_usia)
    warna_dasar_preference = st.multiselect("Pilih preferensi warna dasar:", ["Putih", "Hitam", "Merah", "Kuning", "Biru"], result[0][7].split(', '))

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

    col1, col2  = st.columns([1, 1])
    if col1.button("Simpan Perubahan"):
        simpan_edit(id, gambar, warna, style_desain_preference, makna_warna_preference, sifat_preference, usia_pengguna_preference, warna_dasar_preference)
        st.session_state['edit_triggered'] = False
        st.session_state['current_tab'] = "Data Warna"
        st.experimental_rerun()
    if col2.button("Batal"):
        st.session_state['edit_triggered'] = False
        st.session_state['current_tab'] = "Data Warna"
        st.experimental_rerun()

def simpan_edit(id, gambar, warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()

            existing_data = fetch(f"SELECT warna, gambar FROM data_warna WHERE id_warna = {id}")

            # Update data pada tabel data_warna
            cursor.execute('''
            UPDATE data_warna
            SET warna = %s, style_desain = %s, makna_warna = %s, sifat = %s, usia_pengguna = %s, warna_dasar = %s
            WHERE id_warna = %s
            ''', (
                warna,
                ', '.join(style_desain),
                ', '.join(makna_warna),
                ', '.join(sifat),
                ', '.join(usia_pengguna),
                ', '.join(warna_dasar),
                id
            ))

            # Update gambar jika ada
            if gambar is not None:
                # Hapus gambar lama
                if existing_data[0][1] is not None:
                    os.remove(f"data/warna/{existing_data[0][1]}")
                
                # Simpan gambar baru
                gambar_filename = save_image(gambar)
                cursor.execute('''
                UPDATE data_warna
                SET gambar = %s
                WHERE id_warna = %s
                ''', (
                    gambar_filename,
                    id
                ))

            # Hapus data kombinasi yang sudah ada
            cursor.execute(f"DELETE FROM data_kombinasi WHERE kombinasi_warna LIKE '{existing_data[0][0]} &%' OR kombinasi_warna LIKE '%& {existing_data[0][0]}'")

            conn.commit()

            # Simpan data kombinasi baru
            existing_colors = fetch(f"SELECT warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar FROM data_warna WHERE id_warna != '{id}'")
            save_combinations(existing_colors, warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)

            st.success("Data Warna berhasil diubah.")
        else:
            st.error("Koneksi ke database gagal.")
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def fetch_paginated(query, offset=0, limit=0):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            if limit == 0:
                query_with_pagination = query
            else:
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

def fetch(query):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return result

# Fungsi untuk membuat koneksi ke database
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )

def save_image(gambar):
    # Simpan gambar ke direktori 'gambar'
    try:
        if not os.path.exists('data/warna'):
            os.makedirs('data/warna')
        
        # Simpan gambar dengan nama yang unik atau sesuai input
        gambar_path = os.path.join('data/warna/', gambar.name)
        with open(gambar_path, "wb") as f:
            f.write(gambar.getbuffer())
        
        st.success(f"Gambar '{gambar.name}' berhasil disimpan.")
        return gambar.name
    except Exception as e:
        st.error(f"Error saat menyimpan gambar: {e}")
        return None

def save_combinations(existing_colors, warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            for color in existing_colors:
                cursor.execute('''
                INSERT INTO data_kombinasi (kombinasi_warna, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''', (
                    f"{color[0]} & {warna}",
                    ', '.join(merge_lists(color[1], style_desain)),
                    ', '.join(merge_lists(color[2], makna_warna)),
                    ', '.join(merge_lists(color[3], sifat)),
                    ', '.join(merge_lists(color[4], usia_pengguna)),
                    ', '.join(merge_lists(color[5], warna_dasar))
                ))
                conn.commit()
            st.success("Data Kombinasi Warna berhasil disimpan ke database.")
        else:
            st.error("Koneksi ke database gagal.")
    except Exception as e:
        st.error(f"Error saat menyimpan kombinasi warna: {e}")
        return None

def merge_lists(string_list, addition):
        # Buat list dari string yang dipisahkan oleh koma
        ls = string_list.split(', ')

        # Tambahkan elemen baru ke list
        for item in addition:
            if item not in ls:
                ls.append(item)
        
        return ls

if __name__ == "__main__":
    daftar_rekomendasi()
