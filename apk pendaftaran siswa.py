import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Data siswa
data_siswa = {}

# Format tanggal
format_tanggal = "%d-%m-%Y"

def simpan():
    # Validasi input
    if not entry_nama_lengkap.get() or not entry_ttl.get() or not entry_alamat.get() or not entry_no_telp.get() or not combo_asal_sekolah.get():
        label_status["text"] = "Harap isi semua data!"
        return

    # Ambil data dari input
    nama_lengkap = entry_nama_lengkap.get()
    ttl_str = entry_ttl.get()

    # Validasi format tanggal
    try:
        ttl = datetime.strptime(ttl_str, format_tanggal).date()
    except ValueError:
        label_status["text"] = "Format tanggal tidak valid! Gunakan format dd-mm-yyyy"
        return

    alamat = entry_alamat.get()
    no_telp = entry_no_telp.get()
    asal_sekolah = combo_asal_sekolah.get()

    # Masukkan data ke data siswa
    data_siswa[nama_lengkap] = {
        "ttl": ttl,
        "alamat": alamat,
        "no_telp": no_telp,
        "asal_sekolah": asal_sekolah,
    }

    # Tampilkan pesan sukses
    label_status["text"] = "Data berhasil disimpan!"
    update_saved_data_text()

def update_saved_data_text():
    # Hapus isi text widget
    saved_data_text.delete("1.0", tk.END)

    # Tampilkan data yang disimpan
    for nama, data in data_siswa.items():
        saved_data_text.insert(tk.END, f"Nama: {nama}\n")
        saved_data_text.insert(tk.END, f"TTL: {data['ttl'].strftime(format_tanggal)}\n")
        saved_data_text.insert(tk.END, f"Alamat: {data['alamat']}\n")
        saved_data_text.insert(tk.END, f"No. Telepon: {data['no_telp']}\n")
        saved_data_text.insert(tk.END, f"Asal Sekolah: {data['asal_sekolah']}\n")
        saved_data_text.insert(tk.END, "\n")

# Jendela utama
root = tk.Tk()
root.title("Pendaftaran Siswa Baru")

# Label informasi
label_judul = tk.Label(root, text="Pendaftaran Siswa Baru", font=("Helvetica", 16))

# Entry dan combo box untuk data siswa
entry_nama_lengkap = ttk.Entry(root, width=40)
entry_ttl = ttk.Entry(root, width=20)
entry_alamat = ttk.Entry(root, width=40)
entry_no_telp = ttk.Entry(root, width=20)
combo_asal_sekolah = ttk.Combobox(root, values=["Sekolah A", "Sekolah B", "Sekolah C"])

# Label untuk status
label_status = ttk.Label(root, text="")

# Tombol
button_simpan = ttk.Button(root, text="Simpan", command=simpan)
button_batal = ttk.Button(root, text="Batal", command=root.destroy)

# Tata letak widget
label_judul.pack(pady=10)
label_nama_lengkap = ttk.Label(root, text="Nama Lengkap")
label_nama_lengkap.pack(pady=5)
entry_nama_lengkap.pack(pady=5)
label_ttl = ttk.Label(root, text="Tanggal Lahir (dd-mm-yyyy)")
label_ttl.pack(pady=5)
entry_ttl.pack(pady=5)
label_alamat = ttk.Label(root, text="Alamat")
label_alamat.pack(pady=5)
entry_alamat.pack(pady=5)
label_no_telp = ttk.Label(root, text="Nomor Telepon")
label_no_telp.pack(pady=5)
entry_no_telp.pack(pady=5)
label_asal_sekolah = ttk.Label(root, text="Asal Sekolah")
label_asal_sekolah.pack(pady=5)
combo_asal_sekolah.pack(pady=5)
button_simpan.pack(pady=5)
button_batal.pack(pady=5)
label_status.pack(pady=5)

# Text widget untuk menampilkan data yang disimpan
saved_data_text = tk.Text(root, height=10, width=50)
saved_data_text.pack(pady=10)

# Jalankan GUI
root.mainloop()
