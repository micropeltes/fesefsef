program IL;
uses crt;
var
    p,l,t : integer;
    pk1,pk2,pk3,pk4,pk5,pk6,pk7,pk8,pk9,pk10,pk11,pktotal : real;
    
begin
    writeln('----------------------------------');
    writeln('    Tugas Integrated Learning     ');
    writeln(' Nama      : Gwayne               ');
    writeln(' Kelas     : XIIB                 ');
    writeln(' No. Absen : 11                   ');
    writeln('----------------------------------');
    pktotal :=0;
    writeln('Ruangan Dining Room dan Kitchen');
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk1:=(0.75*p)+(1*l)+(1.5*t);
    pktotal:= pktotal + pk1;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Powder : ',pk3 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Laundry');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk4 :=(1*p)+(0.5*l)+(1.5*t);
    pktotal:= pktotal + pk4;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Living Room : ',pk2 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Powder');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk3:=(1*l)+(0.5*p)+(1.5*t);
    pktotal:= pktotal + pk3;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Laundry : ',pk4 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Garage');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk5 :=(1*p)+(0.5*l)+(1.5*t);
    pktotal:= pktotal + pk5;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Garage : ',pk5 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Bathroom');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk6 :=(1.5*p)+(1.5*t);
    pktotal:= pktotal + pk6;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Bathroom : ',pk6 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Master Bedroom');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk7 :=(2.75*p)+(0.75*l)+(1.5*t);
    pktotal:= pktotal + pk7;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Bedroom 2 : ',pk7 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Bedroom 3');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk8 :=(1.5*p)+(1*l)+(1.5*t);
    pktotal:= pktotal + pk8;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Bedroom 3 : ',pk8 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Bedroom 2');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk9 :=(2.25*p)+(1.75*l)+(1.5*t);
    pktotal:= pktotal + pk9;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Master Bedroom : ',pk9 : 3:2);
    textcolor(yellow);
    writeln('Ruangan W/I');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk10 :=(1*p)+(2.5*l)+(1.5*t);
    pktotal:= pktotal + pk10;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Master Bedroom : ',pk10 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Kamer Mandi Kecil Kanan');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk11 :=(0.5*p)+(2*l)+(1.5*t);
    pktotal:= pktotal + pk11;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Dining Room dan Kitchen : ',pk1 : 3:2);
    textcolor(yellow);
    writeln('Ruangan Living Room');
    textcolor(white);
    write('Panjang :');
    readln(p);
    write('Lebar   :');
    readln(l);
    write('Tinggi  :');
    readln(t);
    pk2:=(1*p)+(2.5*l)+(1.5*t);
    pktotal:= pktotal + pk2;
    
    
    textcolor(green);
    writeln ('Panjang Kabel Ruangan Master Bedroom : ',pk11 : 3:2);
    writeln ('Panjang kabel total : ',pktotal:3:2) ;
    end.
