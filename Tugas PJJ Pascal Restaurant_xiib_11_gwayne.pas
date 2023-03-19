Program Menu_pilihan;
uses crt;
var harga, porsi, kepedasan, tambah, menu, total, jumlah, plus, i :longint;
var   jenis, nama, najen :string;
begin
clrscr;
  GotoXY(40,7);writeln('       RESTORAN SEJAHTERA       ');
  GotoXY(36,8);writeln('     ____________________________________ ');
  GotoXY(36,9);writeln('    |NO. |     Daftar Menu Makanan       |');
  GotoXY(36,10);writeln('    |____|_______________________________|');
  GotoXY(36,11);writeln('    | 1. |   Paket nasi ayam goreng         |');
  GotoXY(36,12);writeln('    | 2. |   Paket nasi ayam bakar          |');
  GotoXY(36,13);writeln('    | 3. |   Ayam goreng a la carte                |');
  GotoXY(36,14);writeln('    | 4. |   Ayam bakar a la carte          |');
  GotoXY(36,15);writeln('    | 5. |   Ayam geprek                   |');
  GotoXY(36,16);writeln('    |____|_______________________________|');
  GotoXY(36,17);write('    Masukan Menu Pilihan Anda : ');
  readln(menu);
          case menu of
          1: begin
              harga:=25000;
              nama:='Paket nasi ayam goreng';
              GotoXY(40,18);write('Kepedasan (sedikit/pedas/sambal dipisah): ');readln(kepedasan);
              GotoXY(40,18);write('Porsi (kecil/sedang/besar): ');readln(porsi);
              end;
          2: begin
              harga:=25000;
              nama:='Paket nasi ayam bakar';
              GotoXY(40,18);write('Kepedasan (sedikit/pedas/sambal dipisah): ');readln(kepedasan);
              GotoXY(40,18);write('Porsi (kecil/sedang/besar): ');readln(porsi);
              end;
          3: begin
              harga:=8000;
              nama:='Ayam goreng a la carte';
              GotoXY(40,18);write('Kepedasan (sedikit/pedas/sambal dipisah): ');readln(kepedasan);
              GotoXY(40,18);write('Porsi (kecil/sedang/besar): ');readln(porsi);
              end;
          4: begin
              harga:=8000;
              nama:='Ayam bakar a la carte';
              GotoXY(40,18);write('Kepedasan (sedikit/pedas/sambal dipisah): ');readln(kepedasan);
              GotoXY(40,18);write('Porsi (kecil/sedang/besar): ');readln(porsi);
              end;
          5: begin
              harga:=15000;
              nama:='Ayam geprek';
              GotoXY(40,18);write('Kepedasan (sedikit/pedas/sambal dipisah): ');readln(kepedasan);
              GotoXY(40,18);write('Porsi (kecil/sedang/besar): ');readln(porsi);
              end;
          end;
             
GotoXY (41,18);write('Jumlah Porsi : '); readln(porsi);
Total:=harga * porsi;
Clrscr;
GotoXY(25,22);writeln('   <>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>');
    GotoXY(25,24);writeln('    ___________________________________________________________ ');
    GotoXY(25,25);writeln('   |                      PESANAN ANDA                         |');
    GotoXY(25,26);writeln('   |___________________________________________________________|');
    GotoXY(25,27);writeln('   ',nama,' ');
    GotoXY(65,27);writeln('Rp.', harga ,',00');
    GotoXY(25,28);writeln(' porsi ');
    GotoXY(65,28);writeln(' ',porsi,' ');
    GotoXY(25,30);writeln(' Total ');
    GotoXY(65,29);writeln('Rp.',total,',00');
     readln;
end.
