NUM_ROWS =  3
NUM_COLS = 8
AVAIL = '-'
BOOKED = 'X'

seatTable = []
for i in range(NUM_ROWS):
    column = []
    for j in range(NUM_COLS):
        column.append(AVAIL)
    seatTable.append(column)

def resetTable(seats): 
    for i in range(NUM_ROWS):
        column = []
        for j in range(NUM_COLS):
            seatTable[i][j] = AVAIL

def printTable(seats):
    i=1
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    print('Row', end=' ')

    for num in range(NUM_COLS):
        print(f'{alpha[num]:2s}'.format(alpha),end='')
    print()

    for num in seats:
        print(f'{str(i):3s}'.format(str(i)), end=' ')
        i+=1
        for j in num:
            print(j,end=' ')
        print()

def full(seats):
    for row in seats:
        for seat in row:
            if seat == AVAIL:
                return False
    return True

def getRes():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        try:
            rowNum = input(f'Enter a row number (1 to {NUM_ROWS}): ')
            seatLetter = input(f'Enter a seat letter (A to {(alpha[NUM_COLS-1]).upper()}): ')
            reserve(seatTable,rowNum,seatLetter)
            break
        except:
            pass
        print('Error, Please choose another seat')
    print(f'Seat {rowNum}{seatLetter.upper()} has been booked\n')

def reserve(seats,resR,resC):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    column = 0
    p = 0
    for i in alpha:
        if i.lower() == resC.lower():
            column = p
        p+=1
    row = int(resR)-1
    seats[row][column] = BOOKED

def main():
    printTable(seatTable)
    while not full(seatTable):
        getRes()
        printTable(seatTable)
    print('Plane is booked')
    next = input('\nWould you like to check the next flight? (Y/N): ')
    if next == 'y': 
        resetTable(seatTable)
        return main()
    else:
        exit()
main()