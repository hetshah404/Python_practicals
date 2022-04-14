# Name : Het Shah
# ID : 20CE127
# Aim :  Find runner-up from given list
# GITHUB LINK : 
list1 = []
  
# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))
  
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
set1 = set(list1)
set1.remove(max(set1))
print(max(set1))
