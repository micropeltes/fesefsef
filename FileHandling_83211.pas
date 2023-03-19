Program File_Handling;
uses crt;
Label
    Mulai, InputMenu, TambahMenu, HasilMenu;
Type
    MenuRecord = Record
    m_kosong : string;
    m_nama   : string;
    m_harga  : string;
    end;
var
    MENU : MenuRecord;
    tambah : string;
    f:file of MenuRecord;
   
begin
    Mulai :
    clrscr;
    writeln('================================================');
    writeln('            Tugas Pascal File Handling          ');
    writeln(' Nama      : Kristoforus Gwayne Donovan Muliadi ');
    writeln(' Kelas     : XIIB                               ');
    writeln(' No. Absen : 11                                 ');
    writeln('================================================');
    assign(f,'datasiswa.txt');
    rewrite(f);
    writeln('Enter Untuk Membuat Menu');
    goto InputMenu;
    
    InputMenu :
    readln(MENU.m_kosong);
    writeln('Silahkan Tambah Menu         ');
    write('Masukkan Nama Menu           : ');
    readln(MENU.m_nama);
    write('Masukkan Harga Menu          : ');
    readln(MENU.m_harga);
    write(f,MENU);
    goto TambahMenu;
    
    TambahMenu : 
    writeln('Ketik "y" bila ingin menambah menu dan apapun selain y untuk total : ');
    write('>> ');
    read(tambah);
    if tambah = 'y' then
        begin
            goto InputMenu;
        end
    else
        begin
            writeln('================================================');
            writeln('                  Hasil Menu                    ');
            writeln('================================================');
            goto HasilMenu;
        end;
        
    HasilMenu :
    reset(f);
    writeln('Nama Menu             |Harga Menu               ');
    writeln('================================================');
    while not eof(f) do
    begin
        read(f,MENU);
        write(MENU.m_nama, '                      ');
        writeln(MENU.m_harga);
    end;
    close(f);
    
end.