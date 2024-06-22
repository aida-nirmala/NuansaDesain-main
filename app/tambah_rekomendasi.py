import streamlit as st
import pandas as pd
import os
import mysql.connector
from mysql.connector import Error

def tambah_rekomendasi():
    st.text('Tambah Rekomendasi')