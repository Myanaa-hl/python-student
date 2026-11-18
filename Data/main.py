from student import save, load
from grade import get_grade, ending

#input data
def input_student(students) :
    while True :
        
        student_names = (input("\nIsi Nama Siswa (or 'done'): ")).strip()
        
        if student_names == "done" :
            break

        if student_names == "" :
            print("Tolong Diisi Dengan Huruf")
            continue
            
        if student_names.isdigit() or "," in student_names :
            print("Nama Tidak Valid Tolong Isi Dengan Huruf")    
            continue
    
        try :
            score = int(input("\nIsi Nilai Siswa Di sini: "))
        except ValueError :
            print("\n Tolong Isi Dengan Angka")
            continue
                
        if score < 0 or score > 100 :
            print("Nilai Tidak Boleh Kurang Dari 0 Dan Lebih Dari 100")
            continue
    
        students[student_names] = score

#show data
def show_student(students) :
    if len(students) == 0 :
            print("Belum Ada Data Siswa Yang Terisi")
            return
        
    for student_names, score in students.items() :
            print(f"{student_names} : {score} (Grade {get_grade(score)})")
            print()
            
            
#search_student
def search(students) :
    name = input("\nNama yang Ingin Dicari: ").strip()
     
    if name in students :
        score = students[name]
        print(f"{name} : {score} (Grade {get_grade(score)})")
         
    else :
        print("Siswa Tidak Ditemukan")           
            
#delete_student
def del_student(students) :
    name = input("\nNama yang Ingin Dihapus: ").strip()
    
    if name in students :
        del students[name]
        print(f"{name} Berhasil Dihapus")
    
    else :
        print("Nama Siswa Tidak Ditemukan")
        
#statistic_student
def statistic(students) :
    
    if len(students) == 0 :
        print("Belum Ada Data Siswa Yang Terisi")
        return
    
    average = sum(students.values()) / len(students)
    print(f"Rata-rata Nilai: {average:.2f}")
        
    maximum = max(students.values())
    print (f"Nilai Tertinggi Adalah: {maximum}")
        
    minimum = min(students.values())
    print (f"Nilai Terendah Adalah: {minimum}")
    
    top_name = ""
    top_score = -1
        
    for student_names, score in students.items() :
        if score > top_score :
            top_score = score
            top_name = student_names
                
    print(f"{top_name} Merupakan Siswa Dengan Nilai {top_score}")
        
    lowest_name = ""
    lowest_rank = 101
        
    for student_names, score in students.items() :
        if score < lowest_rank :
            lowest_rank = score
            lowest_name = student_names
                
    print(f"{lowest_name} Merupakan Siswa Dengan Nilai Terendah {lowest_rank}")
         


#main_focus
def main() :
    students = load()
    
    while True :
        print("\n====Menu Utama====")
        print("1. Tambah Data Siswa")
        print("2. Lihat Data Siswa")
        print("3. Cari Siswa")
        print("4. Menghapus Data Siswa")
        print("5. Statistik Data Siswa")
        print("6. Keluar Dan Save")
        
        choice = input("\nPilih Berdasarkan Nomor: ").strip()
        
        if choice == "1" :
            input_student(students)
        elif choice == "2" :
            show_student(students)
        elif choice == "3" :
            search(students)
        elif choice == "4" :
            del_student(students)
        elif choice == "5" :
            statistic(students)
        elif choice == "6" :
            save(students)
            ending()
            return
        else :
            print("Pilihan Tidak Ada. Ketik Dalam Angka")
            
    
if __name__ == '__main__' :
    main()