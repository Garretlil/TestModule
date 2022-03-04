import OneArr,TwoArr
print ("Возврат хода - буква R")
setka=int(input('введи размер желаемого поля: '))
Choice=int(input('введи 1 для подключения одномерного массива|2 для двумерного: '))
if Choice is 1:
    OneArr.initArr(setka)
    OneArr.ToConsoleArray(setka)
    while True:
        OneArr.vvod_XO(OneArr.GetSymbol(),setka)
        OneArr.ToConsoleArray(setka)    
        if OneArr.win(setka):
           print('Win!')
           break
if Choice is 2:
    TwoArr.initArr(setka)
    TwoArr.ToConsoleArray(setka)
    while True:

        TwoArr.vvod_XO(TwoArr.GetSymbol(),setka)
        TwoArr.ToConsoleArray(setka)    
        if TwoArr.win(setka):
           print('Win!')
           break
