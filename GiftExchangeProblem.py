
# coding: utf-8

# In[1]:


import itertools
class Logical:
    def __init__(self):
        a=0
        b=0
    def miniStartInput(self):
        self.a,self.b = int(input("please enter number of family member's: ")),int(input("Enter number of couples in you'r family: "))
    def factorial(self,val):
        if(val<=1):
            return 1
        return val*self.factorial(val-1)
    def pOfFixPosition(self,start,end):
        result=0
        for i in range(start,end):
                result = result+(-1)**(i+1)*1/self.factorial(i)
        print("P(probabiltiy of fixed position)= ",result)
        return result
    def uniqueVal(self,a,unique,total):
            i = list(map(lambda x: x,range(a)))
            num = ("".join(map(str,i)))
            print("p(No. of unique solutions)=",unique/total,"=",(unique),"/",total)
            uniqueSol=list(itertools.combinations(num,2))
            print(uniqueSol)
            return uniqueSol
    def miniStart(self,flag=True):
        a=self.a
        b=self.b
        
        if(2*b<=a):
            unique=(a*(a-1)/2)
            total = unique+a
            
            result = self.pOfFixPosition(start=2,end=a+1)

            uniqueSol=self.uniqueVal(a,unique,total)
            print("")
            print("P(No. of valid solutions)=", (unique+b)/total,"=",(unique+b),"/",total)
            if(flag):
                print(uniqueSol[b:])
            return uniqueSol
        else:
            print("please enter valid number of couples")
    def filtering(self,names,couple):
        result = list(filter(lambda x: x not in couple, names))
        return result
    
    def start(self):          
        names = {}
        combination=[]
        i=0
        while(True):
            name = str(input("Type name or Type exit to exit: "))
            if(name == "exit"): break
            elif(name==""): print("Name can't be empty")
            else: 
                names[i]={"name": name,"pIndex": None}
                i=i+1
        print(names)

        while(True):
            try:
                boolean,index2,index1=list(map(str,input("please enter t(true) and couple index followed by spaces to procees else type f f f ").split()))

                if(boolean == False or boolean=="false" or boolean=="f" or boolean== "F"): break
                if(boolean=="" or index1=="" or index2==""): print("opps you have some empty space to fill")
                else:
                    if(int(index1) < len(names) and int(index2)<len(names) and int(index2)!=int(index1)):
                        if(names[int(index1)]["pIndex"]==None and names[int(index2)]["pIndex"]==None):
                            combo=[]
                            names[int(index1)]["pIndex"]=int(index2)
                            names[int(index2)]["pIndex"]=int(index1)
                            combo.append(str(index1)) 
                            combo.append(str(index2))
                            
                            combo2=tuple(combo[::-1])
                            combo=tuple(combo)
                            combination.append(combo)
                            print(combo,combo2)
                            combination.append(combo2)

                        else: print("opps! partner is already taken")
                    else: print("opps! Index out of range")

            except ValueError:
                print("Error: you must enter Three inputs followd by space for e.g t 0 1")
        print(combination,"combination")        
        self.a=len(names)
        self.b=len(combination)
        uniqueSolution=self.miniStart(False)
        results=self.filtering(uniqueSolution,combination)
        print(results)
        finalResult=[]
        for i in results:
            local=[]
            local.append(names[int(i[0])]["name"])
            local.append(names[int(i[1])]["name"])

            
            finalResult.append(tuple(local))
        print(finalResult)
         
if __name__=='__main__': 
  
    # Start with the empty list 
    logics = Logical()
#     logics.miniStartInput()
#     logics.miniStart()
    logics.start()


