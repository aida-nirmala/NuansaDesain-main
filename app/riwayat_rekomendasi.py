import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error

def riwayat_rekomendasi():
    st.title('Riwayat Rekomendasi')
    
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )

    # Fungsi untuk menyimpan data ke dalam database MySQL
    def save_to_db(nama_kombinasi, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar):
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                
                # Membuat tabel jika belum ada
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS riwayat_rekomendasi (
                    id_riwayat INT AUTO_INCREMENT PRIMARY KEY,
                    nama_kombinasi TEXT,
                    style_desain TEXT,
                    makna_warna TEXT,
                    sifat TEXT,
                    usia_pengguna TEXT,
                    warna_dasar TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
                ''')
                
                # Memasukkan data ke dalam tabel
                cursor.execute('''
                INSERT INTO riwayat_rekomendasi (nama_kombinasi, style_desain, makna_warna, sifat, usia_pengguna, warna_dasar)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''', (
                    nama_kombinasi,
                    ', '.join(style_desain),
                    ', '.join(makna_warna),
                    ', '.join(sifat),
                    ', '.join(usia_pengguna),
                    ', '.join(warna_dasar)
                ))
                
                conn.commit()
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # Menampilkan data dari tabel
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_rekomendasi'
    )
    if conn.is_connected():
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM riwayat_rekomendasi")
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
