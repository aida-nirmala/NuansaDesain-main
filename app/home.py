import streamlit as st

def home():
    username = st.session_state.user['username']
    st.header(f'Hai {username}, Selamat Datang di')
    # Membuat dua kolom dengan lebar yang sama
    col1, col2 = st.columns([3,2])
    # Menambahkan konten ke dalam kolom pertama
    with col1:
        
        st.title('NuansaDesain')
        st.write('<p style="text-align: justify;">Merupakan sistem rekomendasi pemilihan warna kombinasi pada desain interior yang telah selesai dirancang untuk memperluas aksebilitas informasi desain, mempermudah proses pengambilan keputusan pada pemilihan warna kombinasi desain interior. Aplikasi ini merupakan hasil dari penelitian berjudul "Implementasi Metode Knowledge Based Recommendation Untuk Sistem Rekomendasi Pemilihan Warna Pada Desain Interior Berbasis Website"</p>', unsafe_allow_html=True)

    # Menambahkan konten ke dalam kolom kedua
    with col2:
        st.image('data/warna/Warni.png')
        