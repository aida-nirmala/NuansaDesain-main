import streamlit as st
import pandas as pd
import os
import mysql.connector
from mysql.connector import Error

def hapus_rekomendasi():
    st.text('Hapus Rekomendasi')