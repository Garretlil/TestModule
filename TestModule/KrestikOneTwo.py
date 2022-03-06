import Date
print ("Возврат хода - буква R")
setka=int(input('введи размер желаемого поля: '))
Choice=int(input('введи 1 для подключения одномерного массива|2 для двумерного: '))

if Choice is 1:
    tarr=Date.OneArr()
if Choice is 2:
    tarr=Date.TwoArr()
tarr.initArr(setka)
tarr.ToConsoleArray(setka)

while True:

     tarr.vvod_XO(tarr.GetSymbol(),setka)
     tarr.ToConsoleArray(setka)    
     if tarr.win(setka):
        print('Win!')
        break
