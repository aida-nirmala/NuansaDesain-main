import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            # Membaca header
            header = next(csv_reader)
            print("Header:", header)
            
            # Membaca baris per baris
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

# Ganti 'file.csv' dengan nama file CSV yang sesuai
file_path = 'daftar_warna.csv'
read_csv_file(file_path)
