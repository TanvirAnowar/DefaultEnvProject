'''

va = True;   
print( True and True,1);
if (va == True):
   print("a")
else:  
    print("o") 

# ? range test 

for i in range(10,1,-2):
   print(i)
   


# ? characters traverse in string
name = "Tanvir Anowar"

for i in name:
   print(i)
   


#? break forloop
for i in range(10):
   if i== 5:
      break
   print(i)


#? continue forloop
for i in range(10):
   if i%2==0:
      continue
   print(i)
   


#? prime number

for num in range(1,100):
   if (num == 1) or (num==2) or (num==3):
      print(num)
   else:
      for i in range(2, num//2):
         if num%i == 0:
            break 
      else:        # compulsory execution after a forloop use "else"
         print(num)
         
'''

#? List examples 

fruits = ["apple","banana","cherry","dub"]

#print(fruits) #['apple', 'banana', 'cherry', 'dub']

#print(fruits[1:]) #['banana', 'cherry', 'dub']

#print(fruits[1:3]) #['banana', 'cherry']

#print(fruits[-2]) #'cherry'

#fruits.append("new fruit")
#fruits.insert(3,"after cherry")
#print(fruits)

#fruits.remove("banana")
#print(fruits)

#fruits.append("appended")
#print(fruits)

#fruits.pop(0)
#print(fruits)

#idx = fruits.index("dub")
#print(idx)

#fruits.reverse()
#print(fruits)

#for index,fruit in enumerate(fruits):
#   print(index,fruit)

