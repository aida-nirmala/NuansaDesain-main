import streamlit as st
import pandas as pd

st.markdown("<h2>Data Asli</h2>", unsafe_allow_html=True)
file_path = "data/data_warna.csv"
try:
    # Membaca file CSV menjadi DataFrame
    df = pd.read_csv(file_path)

    # Menambahkan kolom gambar ke DataFrame
    df['Gambar'] = df['Warna'].apply(lambda x: f'<img src="warna/{x}.png" width="50">')
    

    # Menampilkan isi DataFrame dengan menggunakan Markdown HTML
    st.markdown("<h3>Isi DataFrame:</h3>", unsafe_allow_html=True)
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)  # Menampilkan DataFrame dengan kolom Gambar dalam Markdown

except FileNotFoundError:
    st.error("File tidak ditemukan.")
except Exception as e:
    st.error("Terjadi kesalahan dalam membaca file CSV: {}".format(e))
