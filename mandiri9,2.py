siji = []
while True:
    print("Masukkan angka dibawah, jika sudah ketik 'done'")
    inputuser = input("Input :")
    if inputuser == "done":
        break
    else:
        inputuser2 = int(inputuser)
        siji.append(inputuser2)
print(f"Daftar input anda{siji}")
print(f"Nilai Max: {max(siji)}")
print(f"Nilai MIn: {min(siji)}")