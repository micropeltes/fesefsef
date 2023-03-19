while True:
    line = input('> ')
    if line[0] == '#' :
        print('a')
        continue
    if line == 'done' :
        break
    print(line)
print('selesai')