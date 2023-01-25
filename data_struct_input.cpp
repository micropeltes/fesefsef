#include <iostream>
#include <string>
using namespace std;

int main() {
    int i=1;
    while (i < 6) {
        struct {//struct untuk student
        string nim, nama, place_birth;
        struct {//struct untuk address
            string provinsi, kota, nomor, nama_jalan;
        } alamat;
        struct {//struct untuk tanggal lahir
            string tahun, bulan, tanggal;
        } date_birth;
        } mahasiswa;
        //untuk menentukan nilai struct
        cout << "Masukkan NIM anda: " ;
        getline(cin >> mahasiswa.nim);
        cout << "Masukkan Nama anda: " ;
        getline(cin,mahasiswa.nama);
        cout << "Masukkan Tempat lahir anda: ";
        getline(cin,mahasiswa.place_birth);
        cout << "Masukkan tanggal lahir anda: ";
        getline(cin,mahasiswa.date_birth.tanggal);
        cout << "Masukkan bulan lahir anda: ";
        getline(cin,mahasiswa.date_birth.bulan);
        cout << "Masukkan tahun lahir anda: ";
        getline(cin,mahasiswa.date_birth.tahun);
        cout << "Masukkan provinsi anda:  ";
        getline(cin,mahasiswa.alamat.provinsi);
        cout << "Masukkan kota anda: " ;
        getline(cin,mahasiswa.alamat.kota);
        cout << "Masukkan nama jalan anda: ";
        getline(cin,mahasiswa.alamat.nama_jalan);
        cout << "Masukkan nomor alamat anda: ";
        getline(cin,mahasiswa.alamat.nomor);
        //untuk print data dari struct
        cout << "Data mahasiswa Ke-" << i << "\n";
        cout << "NIM                  : " << mahasiswa.nim << "\n";
        cout << "Nama                 : "<< mahasiswa.nama << "\n";
        cout <<"Tempat,Tanggal lahir : "<< mahasiswa.place_birth <<','<< mahasiswa.date_birth.tanggal <<'-'<< mahasiswa.date_birth.bulan <<'-'<< mahasiswa.date_birth.tahun << "\n";
        cout << "Provinsi             : "<<  mahasiswa.alamat.provinsi << "\n";
        cout << "Kota                 : "<<  mahasiswa.alamat.kota << "\n";
        cout << "Nama jalan,nomor     : "<<  mahasiswa.alamat.nama_jalan <<" No."<< mahasiswa.alamat.nomor <<"\n";
        i++;
    }
  return 0;
}