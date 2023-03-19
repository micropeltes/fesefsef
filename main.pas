program tugaspascal2;
uses crt;
label
    menu, makanan, minuman, keluar;
  
var
    a, b, c : integer;
    
begin
    menu :
    clrscr;
    writeln('============================');
    writeln('=      Tugas Pascal 2      =');
    writeln('= Nama      : K. Gwayne D. =');
    writeln('= Kelas     : XIIB         =');
    writeln('= No. Absen : 11           =');
    writeln('============================');
    writeln('Menu : ');
    writeln('1. Makanan');
    writeln('2. Minuman');
    writeln('9. Keluar');
    write('>> ');
    readln(a);
    if (a = 1 ) then
        begin
            goto makanan
        end
    else if (a = 2) then
        begin
            goto minuman
        end
    else if (a = 9) then
        begin
            goto keluar
        end
    else 
        begin 
            writeln('input angka yang anda masukkan tidak ada di dalam menu');
        end;
    readkey;
    goto menu;
    
    makanan :
    writeln('Menu Makanan :');
    writeln('1. Ayam goreng');
    writeln('2. Ayam bakar');
    writeln('3. Paket nasi ayam goreng');
    writeln('4. Paket nasi ayam bakar');
    writeln('5. Extra sambal');
    write('>> ');
    readln(b);
    if (b = 1) then 
        begin
            writeln('Anda memesan Ayam goreng');
        end
    else if (b = 2) then
        begin
            writeln('Anda memesan Ayam bakar');
        end
    else if (b = 3) then
        begin
            writeln('Anda memesan Paket nasi ayam goreng');
        end
    else if (b = 4) then
        begin
            writeln('Anda memesan Paket nasi ayam bakar');
        end
    else if (b = 5) then
        begin
            writeln('Anda memesan Extra sambal');
        end
    else
        begin
            writeln('input angka yang anda masukkan tidak ada di dalam menu');
        end;
    readkey;
    goto menu;
    
    minuman :
    writeln('Menu Minuman : ');
    writeln('1. Teh tawar panas');
    writeln('2. Es teh tawar');
    writeln('3. Teh manis panas');
    writeln('4. Es teh manis');
    writeln('5. Air mineral');
    write('>> ');
    readln(c);
    if (c = 1) then 
        begin
            writeln('Anda memesan Teh tawar panas');
        end
    else if (c = 2) then
        begin
            writeln('Anda memesan Es teh tawar');
        end
    else if (c = 3) then
        begin
            writeln('Anda memesan Teh manis panas');
        end
    else if (c = 4) then
        begin
            writeln('Anda memesan Es teh manis');
        end
    else if (c = 5) then
        begin
            writeln('Anda memesan Air mineral');
        end
    else
        begin
            writeln('input angka yang anda masukkan tidak ada di dalam menu');
        end;
    readkey;
    goto menu;
    
    keluar :
    writeln('terimakasih sudah memesan');
    
end.