import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

def daftar_user():
    st.title('Daftar User')

    # Menambahkan deskripsi setelah judul
    st.markdown("""
            <p>Berikut adalah daftar semua pengguna yang terdaftar dalam sistem rekomendasi warna.</p>
    """, unsafe_allow_html=True)

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

    query_user = "SELECT * FROM user"
    df_asli = fetch_data_from_db(query_user)

    # Rename columns as needed
    df_asli.columns = ["Id", "Username", "Password", "Role"]

    st.markdown(df_asli.to_html(index=False), unsafe_allow_html=True)

if __name__ == '__main__':
    daftar_user()
