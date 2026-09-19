position = input()

column = position[0]
row = int(position[1])

if column == 'a':
    col_num = 1
elif column == 'b':
    col_num = 2
elif column == 'c':
    col_num = 3
elif column == 'd':
    col_num = 4
elif column == 'e':
    col_num = 5
elif column == 'f':
    col_num = 6
elif column == 'g':
    col_num = 7
else:
    col_num = 8

if (col_num + row) % 2 == 0:
    print("black")
else:
    print("white")