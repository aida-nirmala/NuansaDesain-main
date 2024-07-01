import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import time

# Function to fetch data from the database
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
        if result:
            df = pd.DataFrame(result, columns=columns)
        else:
            df = pd.DataFrame(columns=columns)  # Handle case with no data
    except Error as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return df

# Function to save user to the database
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

# Function to delete user from the database
def delete_user_from_db(user_id):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            delete_query = "DELETE FROM user WHERE id_user = %s"
            cursor.execute(delete_query, (user_id,))
            conn.commit()
            st.success("Data user berhasil dihapus dari database.")
            time.sleep(2)
            st.experimental_rerun()
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to update user in the database
def update_user_in_db(user_id, new_username, new_role, new_password):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_rekomendasi'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            update_query = "UPDATE user SET username = %s, role = %s, password = %s WHERE id_user = %s"
            cursor.execute(update_query, (new_username, new_role, new_password, user_id))
            conn.commit()
            st.success("Data user berhasil diupdate di database.")
            time.sleep(2)
            st.experimental_rerun()
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to edit user
def edit_user(user_id):
    query = f"SELECT username, role, password FROM user WHERE id_user = {user_id}"
    user_data = fetch_data_from_db(query)
    if not user_data.empty:
        username = user_data.at[0, 'username']
        role = user_data.at[0, 'role']
        password = user_data.at[0, 'password']

        new_username = st.text_input("Username:", value=username)
        new_role = st.selectbox("Role:", ['Klien', 'Admin'], index=['Klien', 'Admin'].index(role))
        new_password = st.text_input("Password:", value=password, type="password")

        if st.button("Update"):
            update_user_in_db(user_id, new_username, new_role, new_password)
    else:
        st.error("User tidak ditemukan.")

# Main part of the application
def daftar_user():
    st.title('Daftar User')

    # Fetch data from database
    query_user = "SELECT id_user, username, role, password FROM user"
    df_asli = fetch_data_from_db(query_user)

    # Check if DataFrame is empty
    if df_asli.empty:
        st.warning("Tidak ada data pengguna yang ditemukan.")
    else:
        # Rename columns as needed
        df_asli.columns = ["ID", "Username", "Role", "Password"]

        # Displaying data in columns
        col1, col2 = st.columns([3, 2])

        with col1:
            st.subheader('Data User')
            # Adding description after the title
            st.markdown("""
                <p>Berikut adalah daftar semua pengguna yang terdaftar dalam sistem rekomendasi warna.</p>
            """, unsafe_allow_html=True)
            for index, row in df_asli.iterrows():
                st.write(f"ID: {row['ID']}, Username: {row['Username']}, Role: {row['Role']}, Password: {row['Password']}")
                col_edit, col_delete = st.columns([1, 1])
                if col_edit.button("Edit", key=f"edit_{row['ID']}"):
                    st.session_state['edit_id'] = row['ID']
                if col_delete.button("Hapus", key=f"delete_{row['ID']}"):
                    st.session_state['delete_id'] = row['ID']

        with col2:
            st.subheader("Tambah User")

            username_preference = st.text_input("Masukkan username:")
            role_preference = st.selectbox("Pilih role:", ['Klien', 'Admin'])
            password_preference = st.text_input("Masukkan password:", type="password")

            if st.button('Simpan'):
                # Call function to save data to database
                save_user_to_db(username_preference, role_preference, password_preference)

    # Handling edit and delete functions
    if 'edit_id' not in st.session_state:
        st.session_state['edit_id'] = None
    if 'delete_id' not in st.session_state:
        st.session_state['delete_id'] = None

    edit_id = st.session_state['edit_id']
    delete_id = st.session_state['delete_id']

    if edit_id is not None:
        edit_user(edit_id)

    if delete_id is not None:
        confirm_delete = st.button(f"Apakah Anda yakin ingin menghapus user dengan ID {delete_id}?")
        if confirm_delete:
            delete_user_from_db(delete_id)
            st.session_state['delete_id'] = None  # Reset delete_id after deletion

if __name__ == "__main__":
    daftar_user()
