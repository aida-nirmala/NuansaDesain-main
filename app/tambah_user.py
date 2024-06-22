import streamlit as st
import mysql.connector
from mysql.connector import Error

# Fungsi untuk koneksi ke database
def connect_to_database():
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

# Fungsi untuk menyimpan user ke database
def save_user_to_db(username, role, password):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            # Query SQL untuk memasukkan data user baru ke tabel user
            insert_query = "INSERT INTO user (username, password, role) VALUES (%s, %s, %s)"
            data = (username, password, role)
            cursor.execute(insert_query, data)
            conn.commit()
            st.success("Data user berhasil ditambahkan ke database.")
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def tambah_user():
    st.text('Tambah User')

    st.subheader("Masukkan Preferensi")
        
    username_preference = st.text_input("Masukkan username:")
    role_preference = st.selectbox("Pilih role:", ['Klien', 'Admin'])
    password_preference = st.text_input("Masukkan password:", type="password")

    if st.button('Simpan'):
        # Memanggil fungsi untuk menyimpan data ke database
        save_user_to_db(username_preference, role_preference, password_preference)
