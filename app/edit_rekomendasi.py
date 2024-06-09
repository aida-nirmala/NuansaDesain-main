import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

# Fungsi untuk membuat koneksi ke database
def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        st.error(f"Error: {e}")
        return None

# Fungsi untuk membuat tabel jika belum ada
def create_table_if_not_exists(conn, table_name, columns):
    try:
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {columns}
            );
        ''')
        conn.commit()
    except Error as e:
        st.error(f"Error: {e}")

# Fungsi untuk menyimpan data dari CSV ke tabel database
def save_to_db(conn, table_name, df):
    try:
        cursor = conn.cursor()
        for i, row in df.iterrows():
            placeholders = ', '.join(['%s'] * len(row))
            columns = ', '.join([f'`{col}`' for col in row.index])
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(row))
        conn.commit()
    except Error as e:
        st.error(f"Error: {e}")

# Halaman utama Streamlit
def edit_rekomendasi():
    st.title("Import CSV to SQL Database")

    # Unggah file CSV untuk data asli
    st.header("Import Data Asli")
    uploaded_file_asli = st.file_uploader("Choose a CSV file for Data Asli", type="csv", key="data_warna")
    
    if uploaded_file_asli is not None:
        # Baca file CSV
        df_asli = pd.read_csv(uploaded_file_asli)
        st.write("CSV file content:")
        st.dataframe(df_asli)

        # Buat koneksi ke database
        conn = create_connection()
        if conn:
            # Buat tabel jika belum ada
            table_name_asli = "data_warna"
            columns_asli = "id_rekomendasi INT AUTO_INCREMENT PRIMARY KEY, kombinasi_warna TEXT, style_desain TEXT, makna_warna TEXT, sifat TEXT, usia_pengguna TEXT, warna_dasar TEXT"
            create_table_if_not_exists(conn, table_name_asli, columns_asli)
            
            # Tombol untuk menyimpan data ke database
            if st.button("Save Data Asli to Database"):
                save_to_db(conn, table_name_asli, df_asli)
                st.success("Data Asli has been saved to the database")
                
                # Tampilkan data dari tabel database
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name_asli}")
                result = cursor.fetchall()
                
                columns = [i[0] for i in cursor.description]
                db_df_asli = pd.DataFrame(result, columns=columns)
                st.write("Data from database (Data Asli):")
                st.dataframe(db_df_asli)
                
                cursor.close()
                conn.close()

    # Unggah file CSV untuk data kombinasi
    st.header("Import Data Kombinasi")
    uploaded_file_kombinasi = st.file_uploader("Choose a CSV file for Data Kombinasi", type="csv", key="data_kombinasi")
    
    if uploaded_file_kombinasi is not None:
        # Baca file CSV
        df_kombinasi = pd.read_csv(uploaded_file_kombinasi)
        st.write("CSV file content:")
        st.dataframe(df_kombinasi)

        # Buat koneksi ke database
        conn = create_connection()
        if conn:
            # Buat tabel jika belum ada
            table_name_kombinasi = "data_kombinasi"
            columns_kombinasi = "id_rekomendasi INT AUTO_INCREMENT PRIMARY KEY, kombinasi_warna TEXT, style_desain TEXT, makna_warna TEXT, sifat TEXT, usia_pengguna TEXT, warna_dasar TEXT"
            create_table_if_not_exists(conn, table_name_kombinasi, columns_kombinasi)
            
            # Tombol untuk menyimpan data ke database
            if st.button("Save Data Kombinasi to Database"):
                save_to_db(conn, table_name_kombinasi, df_kombinasi)
                st.success("Data Kombinasi has been saved to the database")
                
                # Tampilkan data dari tabel database
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name_kombinasi}")
                result = cursor.fetchall()
                
                columns = [i[0] for i in cursor.description]
                db_df_kombinasi = pd.DataFrame(result, columns=columns)
                st.write("Data from database (Data Kombinasi):")
                st.dataframe(db_df_kombinasi)
                
                cursor.close()
                conn.close()
