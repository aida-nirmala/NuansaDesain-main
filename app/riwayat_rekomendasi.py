import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error

def riwayat_rekomendasi():
    st.title('Riwayat Rekomendasi')

    # Menambahkan barisan atau informasi tambahan
    st.markdown("""
         <p>Berikut adalah riwayat rekomendasi warna berdasarkan data yang terpilih.</p>
    """, unsafe_allow_html=True)

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )

    # Menampilkan data dari tabel
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )
    if conn.is_connected():
        mycursor = conn.cursor()
        role = st.session_state.user['role']
        username = st.session_state.user['username']
        if role == 'Admin' :
            mycursor.execute("SELECT * FROM riwayat_rekomendasi")
        else :
            mycursor.execute(f"SELECT * FROM riwayat_rekomendasi WHERE user = '{username}'")
        result = mycursor.fetchall()

        columns = [i[0] for i in mycursor.description]
        df = pd.DataFrame(result, columns=columns)

        # Menghilangkan kolom 'id_warna_1' dan 'id_warna_2'
        if 'id_warna_1' in df.columns and 'id_warna_2' in df.columns:
            df = df.drop(['id_warna_1', 'id_warna_2'], axis=1)

        # Merename kolom DataFrame
        df = df.rename(columns={
            'id_riwayat': 'Id',
            'nama_kombinasi': 'Kombinasi Warna',
            'style_desain': 'Style Desain',
            'makna_warna': 'Makna Warna',
            'sifat': 'Sifat',
            'usia_pengguna': 'Usia Pengguna',
            'warna_dasar': 'Warna Dasar',
            'created_at': 'Dibuat'
        })
        
        st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        
        mycursor.close()
        conn.close()

if __name__ == '__main__':
    riwayat_rekomendasi()
