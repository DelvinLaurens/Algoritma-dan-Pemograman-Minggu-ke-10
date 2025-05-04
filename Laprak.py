#Soal 2
def kuis_dari_file(nama_file):
    try:
        with open("soal.txt") as nama_file:
            for i in nama_file:
                a = i.split(" || ")
                simpan = a[1].strip()
                print(a[0])
                jawab = input('Jawaban: ')
                if jawab.lower() == simpan.lower():
                    print('Jawaban benar!')
                else:
                    print('Jawaban salah!')
                   
                
    except FileNotFoundError:
        print("File tidak di temukan")
kuis_dari_file("soal.txt")
