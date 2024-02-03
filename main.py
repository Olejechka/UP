from random import randint
sudokulist=[]
memlist=[]
secondlst=[]
sudokulist = [[0] * 9 for _ in range(9)]
secondlst = [['-'] * 9 for _ in range(9)]
num=1

for i in range(9):
    for c in range(9):
        sudokulist[0][i]=num
    num+=1

for i in range(1,9):
    sudokulist[i][0] = (sudokulist[i-1][0]) + 3
    if sudokulist[i][0]>9:
        sudokulist[i][0]-=8

for i in range(1,9):
    for c in range(1,9):
        sudokulist[i][c]=sudokulist[i][c-1]+1
        if sudokulist[i][c]>9:
            sudokulist[i][c]= 1

def swap_columns(m, n):
    for i in range(9):
        sudokulist[i][m-1], sudokulist[i][n-1] = sudokulist[i][n-1], sudokulist[i][m-1]

swap_columns(9, 7)
swap_columns(3, 1)

for i in range(0,9):
    for c in range(0,9):
        chance=randint(1,100)
        if chance<70:
            secondlst[i][c]=sudokulist[i][c]
print('sudoku 1.3')
print('')
print('Требуется ввести позицию клетки, а затем её значение')
print('Пример: 1 3 7')

game = True
while game:
    print('')
    for i in secondlst:
        print(*i)
    a,b,c=map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        for i in sudokulist:
            print(*i)
    elif a == -2 and b == -2 and c == -2:
        print('closing game...')
        game=False
    elif 0 <= (a - 1) < 9 and 0 <= (b - 1) < 9 and c == sudokulist[a - 1][b - 1]:
        print('correct')
        secondlst[a-1][b-1] = str(sudokulist[a-1][b-1])
    elif secondlst == sudokulist:
        print('win!')
        game=False
    else:
        print('incorrect')