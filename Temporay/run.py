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

#fruits = ["apple","banana","cherry","dub"]

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

#list comprehension 
#comp = [ num for num in range(10) if num%2==0 ]

#list1 = [1,2,3,4]
#list2 = ['a','b','c','d']
#comp_list = [(i,j) for i in list1 for j in list2]
#print(comp_list)

# first_tup = (1,2,3)
# second_tup = (4,5,6)

# new_tup = first_tup + second_tup
#print(new_tup*3)
# print(new_tup)
# print(new_tup.index(6))
# print(new_tup.count(6))

# a,b,c,*d,e,f = new_tup
# print(a,b,c,d,e,f)

# print(type(d))

# ? Dictionary 

new_dic = {"name":"Tanvir","age":"25","city":"Dhaka"}
'''

print(new_dic)

print(new_dic.get("city"))

print(new_dic.keys())
print(new_dic.values())
print(new_dic.items())
print(new_dic.pop("age"))
print(new_dic)
print(new_dic.popitem())
print(new_dic)
new_dic.update({"country":"Bangladesh"})
print(new_dic)
new_dic.popitem()
print(new_dic)
new_dic.clear()
print(new_dic)

copy_dic = new_dic.copy()
new_dic.update({"country":"UK"})
print(new_dic,copy_dic)
'''

for key,value in new_dic.items():
   print(key,value)
   
print(type(new_dic.items()))
   
