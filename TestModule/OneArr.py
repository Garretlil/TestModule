arraysetka=[]
arraysteps=[]
words = ("X", "O")
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False 
     
def vvod_XO(bukva_,n):
    x=input('следующий ход игрока' + ' '+ bukva_ +', выберите номер: ')

    if x.upper()=='R' :
        if  len(arraysteps)!=0:
            stepp=arraysteps[len(arraysteps)-1]# последний ход
            arraysetka[stepp-1]=stepp
            arraysteps.pop(len(arraysteps)-1)
    if is_integer(x) :
        x=int(x)
        try:
            if not(x<=n**2 and x>0 ):
                raise BaseException("введи допустимое значение")
            if not(x in arraysetka):
                raise BaseException("поле занято")
            arraysetka[x-1]=bukva_
            arraysteps.append(x)
        except BaseException as ve:
          print(ve)
          vvod_XO(bukva_,n)    
        

def ResearchOfSize(current_element,maxlensymbol_):    
    dlina=len(str(current_element))
    return maxlensymbol_-dlina


def vuvod_stroka(setka_,k): 
    stroka='|'
    maxlensymbol=len(str(setka_**2))
    for i in range(k,k+setka_):
        stroka+=str(arraysetka[i])
        stroka+=' '*ResearchOfSize(arraysetka[i],maxlensymbol)
        stroka+='|'
    return stroka

def ToConsoleArray(setka_):    
    t=0
    for i in range(setka_):
        stroka=vuvod_stroka(setka_,t)
        print(stroka)
        t+=setka_

def askwin(win_combinations):   
    for i in range(len(win_combinations)-1):
        if win_combinations[i]!=win_combinations[i+1]:
            return False
    return True

def win(n):
    k=0
    mass=[]
    # проверка по строкам
    for i in range(n):
        for s in range(k,k+n):
            mass.append(arraysetka[s])
        if askwin(mass):
            return True
        else:
            k+=n

    mass.clear()
        # проверка по столбцам
    for i in range(n):  
        mass.clear()
        for s in range(i,i+n*(n-1)+1,n):
            mass.append(arraysetka[s])
        if askwin(mass):
            return True

    mass.clear()
     # проверка по диагоналям
    for i in range(0,n**2,n+1):
        mass.append(arraysetka[i])
    if askwin(mass):
            return True

    mass.clear()
    for i in range(n-1,n**2-n+1,n-1):
        mass.append(arraysetka[i])
    if askwin(mass):
            return True
        
    return False

def GetSymbol():    
   return words[len(arraysteps)%2] 
    

def initArr(setka):
   for i in range(1,setka**2+1):
    arraysetka.append(i)
