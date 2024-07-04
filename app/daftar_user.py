import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import time

# Function to fetch data from the database (moved to global scope)
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
            st.session_state['delete_id'] = None  # Reset delete_id after deletion
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
            st.success("Data user berhasil diedit di database.")
            st.session_state['edit_id'] = None  # Reset edit_id after successful update
            time.sleep(2)
            st.experimental_rerun()
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to save new user to the database
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
            insert_query = "INSERT INTO user (username, role, password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (username, role, password))
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

# Function to display user list and add/edit functionalities
def daftar_user():
    col_data, kosong, col_edit = st.columns([16, 1, 6])

    # Function to edit user
    def edit_user(user_id):
        # Adding description after the title
        col_edit.markdown("""
            <p>Silahkan edit data yang dipilih</p>
        """, unsafe_allow_html=True)
        query = f"SELECT username, role, password FROM user WHERE id_user = {user_id}"
        user_data = fetch_data_from_db(query)
        if not user_data.empty:
            username = user_data.at[0, 'username']
            role = user_data.at[0, 'role']
            password = user_data.at[0, 'password']

            new_username = col_edit.text_input("Username:", value=username, key=f"username_{user_id}")
            new_role = col_edit.selectbox("Role:", ['Klien', 'Admin'], index=['Klien', 'Admin'].index(role), key=f"role_{user_id}")
            new_password = col_edit.text_input("Password:", value=password, type="password", key=f"password_{user_id}")

            col_buttons = col_edit.columns([1, 3, 1])  # Add column for buttons (cancel, save)
            if col_buttons[1].button("Simpan", key=f"simpan_{user_id}"):
                update_user_in_db(user_id, new_username, new_role, new_password)
            if col_buttons[2].button("✖️", key=f"cancel_{user_id}"):
                st.session_state['edit_id'] = None  # Reset edit_id to hide form
        else:
            st.error("User tidak ditemukan.")

    # Function to display user list
    def data_user():
        col_data.header("Daftar User")
        with col_data.popover("Tambah Data User"):
            st.markdown("Tambah Data User")
            username_preference = st.text_input("Masukkan username:")
            role_preference = st.selectbox("Pilih role:", ['Klien', 'Admin'])
            password_preference = st.text_input("Masukkan password:", type="password")

            if st.button('Simpan'):
                # Call function to save data to database
                save_user_to_db(username_preference, role_preference, password_preference)

        # Fetch data from database
        query_user = "SELECT id_user, username, role, password FROM user"
        df_asli = fetch_data_from_db(query_user)

        # Check if DataFrame is empty
        if df_asli.empty:
            col_data.warning("Tidak ada data pengguna yang ditemukan.")
        else:
            # Rename columns as needed
            df_asli.columns = ["ID", "Username", "Role", "Password"]

            # Adding description after the title
            col_data.markdown("""
                <p>Berikut adalah daftar semua pengguna yang terdaftar dalam sistem rekomendasi warna.</p>
            """, unsafe_allow_html=True)

            # Create header columns
            header_cols = col_data.columns([1, 3, 2, 3, 4])
            headers = ["ID", "Username", "Role", "Password", "Aksi"]
            for header, col in zip(headers, header_cols):
                col.write(f"**{header}**")

            # Create columns for each user
            for index, row in df_asli.iterrows():
                col1, col2, col3, col4, col5, col6 = col_data.columns([1, 3, 2, 3, 2, 2])
                col1.write(row['ID'])
                col2.write(row['Username'])
                col3.write(row['Role'])
                col4.write(row['Password'])
                if col5.button("Edit", key=f"edit_{row['ID']}"):
                    st.session_state['edit_id'] = row['ID']
                if col6.button("Hapus", key=f"delete_{row['ID']}"):
                    st.session_state['delete_id'] = row['ID']

        # Handling edit and delete functions
        if 'edit_id' not in st.session_state:
            st.session_state['edit_id'] = None
        if 'delete_id' not in st.session_state:
            st.session_state['delete_id'] = None
        if 'confirm_delete' not in st.session_state:
            st.session_state['confirm_delete'] = False

        if st.session_state['edit_id'] is not None:
            edit_user(st.session_state['edit_id'])

        if st.session_state['delete_id'] is not None:
            if not st.session_state['confirm_delete']:
                st.warning(f"Apakah Anda yakin ingin menghapus user dengan ID {st.session_state['delete_id']}?")
                col_yes, col_no = st.columns(2)
                if col_yes.button("Ya", key="confirm_yes"):
                    delete_user_from_db(st.session_state['delete_id'])
                if col_no.button("Batal", key="confirm_no"):
                    st.session_state['delete_id'] = None
                    st.session_state['confirm_delete'] = False
            else:
                st.warning(f"Apakah Anda yakin ingin menghapus user dengan ID {st.session_state['delete_id']}?")
                col_yes, col_no = st.columns(2)
                if col_yes.button("Ya", key="confirm_yes"):
                    delete_user_from_db(st.session_state['delete_id'])
                if col_no.button("Batal", key="confirm_no"):
                    st.session_state['delete_id'] = None
                    st.session_state['confirm_delete'] = False

    data_user()

