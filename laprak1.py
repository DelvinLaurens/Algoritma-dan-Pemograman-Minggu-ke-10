#soal 1
def banding(file1, file2):
    try:
        with open(file1,'r') as file1, open(file2,'r') as file2:
            a = file1.readlines()
            b = file2.readlines()
            maxlen = max(len(a),len(b))
            hitung = 0
            for i in range(maxlen):
                if i < len(a):
                    baris1 = a[i].strip()
                else:
                    ''
                if i < len(b):
                    baris2 = b[i].strip()
                else:
                    ''
                if baris1 != baris2:
                    print(f'Beda pada baris ke-{i + 1}')
                    hitung += 1
                else:
                    print(f"Sama pada baris ke-{i + 1}")
            print(f'Jumlah beda:{hitung}')
    except FileNotFoundError:
        print("File eror")
banding("text1.txt","text2.txt")
