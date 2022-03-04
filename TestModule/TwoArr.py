# сделать двумерный массив

class ClassTwoArr: 
    
    arraysetka=[]
    arraysteps=[]
    words = ("X", "O")

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




