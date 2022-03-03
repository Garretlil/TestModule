import TwoArr
print ("Возврат хода - буква R")
setka=int(input('введи размер желаемого поля: '))
t=5
TwoArr.initArr(setka)
TwoArr.ToConsoleArray(setka)
while True:

    TwoArr.vvod_XO(TwoArr.GetSymbol(),setka)
    TwoArr.ToConsoleArray(setka)    
    if TwoArr.win(setka):
       print('Win!')
       break
