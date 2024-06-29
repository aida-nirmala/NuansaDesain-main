import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import time

# Fungsi untuk mengambil data dari database
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

# Fungsi untuk menyimpan user ke database
def save_user_to_db(username, role, password):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            insert_query = "INSERT INTO user (username, password, role) VALUES (%s, %s, %s)"
            data = (username, password, role)
            cursor.execute(insert_query, data)
            conn.commit()
            st.success("Data user berhasil ditambahkan ke database.")
            time.sleep(2)
            st.experimental_rerun()
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Bagian utama dari aplikasi
def daftar_user():
    st.title('Daftar User')
    col1, col2 = st.columns([3,2])

    with col1:
        st.subheader('Data User')

        # Menambahkan deskripsi setelah judul
        st.markdown("""
            <p>Berikut adalah daftar semua pengguna yang terdaftar dalam sistem rekomendasi warna.</p>
        """, unsafe_allow_html=True)

        query_user = "SELECT * FROM user"
        df_asli = fetch_data_from_db(query_user)

        # Rename columns as needed
        df_asli.columns = ["ID", "Username", "Role", "Password"]

        st.markdown(df_asli.to_html(index=False), unsafe_allow_html=True)

    with col2:

        st.subheader("Tambah User")
            
        username_preference = st.text_input("Masukkan username:")
        role_preference = st.selectbox("Pilih role:", ['Klien', 'Admin'])
        password_preference = st.text_input("Masukkan password:", type="password")

        if st.button('Simpan'):
            # Memanggil fungsi untuk menyimpan data ke database
            save_user_to_db(username_preference, role_preference, password_preference)

