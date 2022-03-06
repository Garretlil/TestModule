class CommonArr:
    arraysetka=[]
    arraysteps=[]
    words = ("X", "O")
    def __init__(self): 
           pass
    def askwin(self,win_combinations):   
        for i in range(len(win_combinations)-1):
            if win_combinations[i]!=win_combinations[i+1]:
                return False
        return True
    def GetSymbol(self):    
       return self.words[len(self.arraysteps)%2] 
class OneArr(CommonArr):
    def __init__(self): 
           pass
    def is_integer(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False 
     
    def vvod_XO(self,bukva_,n):
        x=input('следующий ход игрока' + ' '+ bukva_ +', выберите номер: ')

        if x.upper()=='R' :
            if  len(self.arraysteps)!=0:
                stepp=self.arraysteps[len(self.arraysteps)-1]# последний ход
                self.arraysetka[stepp-1]=stepp
                self.arraysteps.pop(len(self.arraysteps)-1)
        if self.is_integer(x) :
            x=int(x)
            try:
                if not(x<=n**2 and x>0 ):
                    raise BaseException("введи допустимое значение")
                if not(x in self.arraysetka):
                    raise BaseException("поле занято")
                self.arraysetka[x-1]=bukva_
                self.arraysteps.append(x)
            except BaseException as ve:
              print(ve)
              self.vvod_XO(bukva_,n)    
        

    def ResearchOfSize(self,current_element,maxlensymbol_):    
        dlina=len(str(current_element))
        return maxlensymbol_-dlina


    def vuvod_stroka(self,setka_,k): 
        stroka='|'
        maxlensymbol=len(str(setka_**2))
        for i in range(k,k+setka_):
            stroka+=str(self.arraysetka[i])
            stroka+=' '*self.ResearchOfSize(self.arraysetka[i],maxlensymbol)
            stroka+='|'
        return stroka

    def ToConsoleArray(self,setka_):    
        t=0
        for i in range(setka_):
            stroka=self.vuvod_stroka(setka_,t)
            print(stroka)
            t+=setka_
    def win(self,n):
        k=0
        mass=[]
        # проверка по строкам
        for i in range(n):
            for s in range(k,k+n):
                mass.append(self.arraysetka[s])
            if self.askwin(mass):
                return True
            else:
                k+=n

        mass.clear()
            # проверка по столбцам
        for i in range(n):  
            mass.clear()
            for s in range(i,i+n*(n-1)+1,n):
                mass.append(self.arraysetka[s])
            if self.askwin(mass):
                return True

        mass.clear()
         # проверка по диагоналям
        for i in range(0,n**2,n+1):
            mass.append(self.arraysetka[i])
        if self.askwin(mass):
                return True

        mass.clear()
        for i in range(n-1,n**2-n+1,n-1):
            mass.append(self.arraysetka[i])
        if self.askwin(mass):
                return True
        
        return False

    def GetSymbol(self):    
       return self.words[len(self.arraysteps)%2] 
    

    def initArr(self,setka):
       for i in range(1,setka**2+1):
        self.arraysetka.append(i)
class TwoArr(CommonArr):
    def __init__(self): 
           pass

    def GetSymbol(self):    
       return self.words[len(self.arraysteps)%2]

    def vvod_XO(self,bukva_,setka_):
        temp=input('следующий ход игрока ' + bukva_+'  , выберите номер в формате [*,*]: ')

        if temp.upper()=='R' :
                if  len(self.arraysteps)!=0:
                    stepp=self.arraysteps[len(self.arraysteps)-1]# последний ход
                    self.arraysetka[stepp[0]][stepp[1]]=""
                    self.arraysteps.pop(len(self.arraysteps)-1)
        else: 
            x,y = map(int, temp.split(" "))

            try:
   
                if  (y>setka_-1 and y<0 ) or (x>setka_-1 and x>0 ):
                    raise BaseException("введи допустимое значение")
            
                if  (self.arraysetka[x][y]!=""):
                    raise BaseException("поле занято")            
            
                self.arraysetka[x][y]=bukva_                      
                self.arraysteps.append([x,y])
            except BaseException as ve:
                print(ve)
                self.vvod_XO(self,bukva_,setka_)    
        

    def ResearchOfSize(self,x,y,z,setka):    
        fulldlina=2*len(str(setka))+1
        dlina=len(str(x)+str(y))
        return fulldlina-dlina-z

    def ToConsoleArray(self,setka_):    
        t=0
        for i in range(setka_):
            stroka='|'
            for k in range(setka_):
                if self.arraysetka[i][k]!="":
                   stroka+=self.arraysetka[i][k] + " "*self.ResearchOfSize(i,k,-1,setka_)
                else:
                   stroka+=str(i)+","+str(k) + " "*self.ResearchOfSize(i,k,1,setka_)
                stroka+='|'
            print(stroka)

    def askwin(self,win_combinations):   
        for i in range(len(win_combinations)-1):
            if win_combinations[i]!=win_combinations[i+1] or win_combinations[i]=="" or win_combinations[i+1]=="": 
                return False
        return True

    def win(self,setka_):

        # проверка по строкам  
        # проверка по столбцам
    
        Astolbec=[]
        Astroka=[]
        ADiagDown=[]
        ADiagUp=[]
        for i in range(setka_):
           Astolbec.clear()
           Astroka.clear()
           for j in range(setka_):
                 Astolbec.append(self.arraysetka[j][i])
                 Astroka.append(self.arraysetka[i][j])
           ADiagUp.append(self.arraysetka[i][j-i])      
           ADiagDown.append(self.arraysetka[i][i])
           if self.askwin(Astolbec) or self.askwin(Astroka): return True
        if self.askwin(ADiagDown) or self.askwin(ADiagUp): return True
        return False

 
    





    def initArr(self,setka):
        for i in range(setka):
            mass=[]
            for k in range(setka):
                mass.append("")
            
            self.arraysetka.append(mass)
