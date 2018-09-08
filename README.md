
# Gift Exchange Problem


## This application is made in order to solve the problem of gift exchange between the family this problem is also called secret santa problem

### Explanation of code  

This code is writen inside a class named Logical which is having 8 function to solve the problem 

```
def __init__(self):
        a=0
        b=0
```
inatialise the value of a and b 


##### miniStartInput fucntion

This function takes two input first i/p is for number of members and 2nd input is for number of couples 

this fuction is called mini function as it is just for logical explanation of the app you can't enter names here but logic is build around numbers only right 

```
def miniStartInput(self):
        self.a,self.b = int(input("please enter number of family member's: ")),int(input("Enter number of couples in you'r family: "))
```

##### factorial function 

As the name suggest it is used to take factors of the number for e.g 3! = 3*2*1
it is a recursive funciton 

##### pOfFixPosition function 

This fucniton is used to solve the problem of derangement 
so called P(fix position) = ?

derangement(!n)~=n!/e 

e = 2.71828

P(no fix position) = !n/e i.e 1/e ~= .37%
P(fix position)=1-P(no fix position)=67%

```
def pOfFixPosition(self,start,end):
        result=0
        for i in range(start,end):
                result = result+(-1)**(i+1)*1/self.factorial(i)
        print("P(probabiltiy of fixed position)= ",result)
        return result
```

##### uniqueVal function 

This function is used to find number of unique solution 


the formula use here is P(No. of uniqusolutions)=unique/total

for e.g if n = 4 
4C2 or n*(n-1)/3 i.e (4*3)/2 = 6
P(U)=4C2/total = 6/10 if no couples are envolved 

```
def uniqueVal(self,a,unique,total):
            i = list(map(lambda x: x,range(a)))
            num = ("".join(map(str,i)))
            print("P(No. of unique solutions)=",unique/total,"=",(unique),"/",total)
            uniqueSol=list(itertools.combinations(num,2))
            print(uniqueSol)
            return uniqueSol
            
```

##### miniStart function

This function was initially build for miniStartInput function but later the same logic was used by start fucntion 

it calculates if couples popolation is no more than total number of peoples 
```
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
```
##### filtering fucntion 

this function is used to filter couples index from unique combination index
##### start function 

This fucntion takes input as names for e.g a b c d

try to make format such as 
names = 0{
     name:"a",
     pIndex:"for partner index if any"}
     
you press exit to proceed further.

then you enters couples in the format t (space) index1 (space) index2

e.g t 0 1

it will link a with b as a has index 0 and b has index 1

rest all story is same as miniStart


### summber with e.g


supposed you have 4 people a b c d 

number of uniquie combination will be =  ab ac ad bc bd cd (6)

totoal combinaiton will be = aa bb cc dd ab ac ad bc bd cd (10)

so p(a getting a) = 1/10

p(valid combination ) = 6/10

p(unvalid combination )=  4/10

