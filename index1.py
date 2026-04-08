# num=int(input("Enter a number : "))
# print("Num:",num)
# print("type of num: ",type(num))

# for i in range(1,11):
#     print(num, "*", i,"=",(num*i))


# # factorial of a number
# integer=int(input("Enter an integer : "))   
# factorial=1
# if integer<0:
#     print("Factorial does not exist for negative numbers")      
# elif integer==0:
#     print("The factorial of 0 is 1")    
# else:    
#     for i in range(1,integer+1):
#         factorial=factorial*i
# print("The factorial of", integer, "is", factorial)     
 

# palindrome
# string=input("Enter a string : ")
# if string==string[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")


# age=10
# if age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are Thanmayi")


# #sum of digits
# number=int(input("Enter a number : "))
# sum=0
# while number>0:
#     digit=number%10
#     sum=sum+digit
#     number=number//10
# print("The sum of digits is : ",sum)

#count no of digits in a number
# number=int(input("Enter a number : "))
# count=0
# while number>0:
#     number=number//10
#     count=count+1
# print("The number of digits is : ",count)    


# # list
# mark=[10,20,30,40,50]
# print(mark)
# print(type(mark))
# print(sum(mark)) 

# #palindrome using list
# string=input("Enter a string : ")   
# string_list=list(string)
# if string_list==string_list[::-1]:
#     print("The string is a palindrome")
# else:    print("The string is not a palindrome")

#write a code in python to reverse a number
# number=int(input("Enter a number : "))
# reverse=0
# while number>0:
#     digit=number%10
#     reverse=reverse*10+digit
#     number=number//10
# print("The reverse of the number is : ",reverse)



#----------------DAY 2-----------------#


#creating a set

# marks={90,80,70,70}
# print(marks)
# print(type(marks))


# list1=[1,2,3,4,5,6,6,5,4]
# print(list1)
# set1=set(list1)
# print(set1)

# dict1={"name":"Thanmayi","age":20,"city":"Hyderabad"}
# print(dict1)
# print(type(dict1))
# print(dict1["name"])

# import numpy as np

# arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(arr1) 
# print(type(arr1))

# #shape of the array
# print(arr1.shape)

# #2-d array
# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2)
# print(arr2.shape)

# arr1=np.array([1,2,3,4,5,6])
# arr2=np.array([[7,8,9],[10,11,12]])

#----------addition----------

#print(arr1+20)
# print(arr2+30)

#----------subtraction---------
# print(arr1-10)
# print(arr2-20)

#--------multiplication---------

# print(arr1*2)
# print(arr2*3)

#--------division----------

# print(arr1/2)
# print(arr2/3)

#-------modulus---------

# print(arr1%2)
# print(arr2%5)

#---------powerof---------

# print(arr1**2)
# print(arr2**2)


# arr1=np.zeros((3,4))
# print(arr1)

# arr2=np.ones((2,3))
# print(arr2)

# arr3=np.arange(1,11)
# print(arr3)

# arr4=np.linspace(0,1,5)
# print(arr4)



import pandas as pd
# # s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# # print(s)

#data={"name":["Thanmayi","Siri","Anu"],"age":[20,21,22],"city":["Hyderabad","Bangalore","Chennai"]}
# df=pd.DataFrame(data)
# print(df)
# print(type(df))


# #read text file
# date=pd.read_csv("train.txt",sep=";",header=None,names=["Sentence","Emotions"])
# # print(date.head())#first 5 rows
# # print(date.tail())#last 5 rows
# # print(date.shape)#number of rows and columns    
# # print(date.isnull().sum)
# # print(date.describe())
# #getting unique emotions
# print(date["Emotions"].unique())

import matplotlib.pyplot as plt
import numpy as np
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.75, 0.62, 0.51, 0.43, 0.37, 0.32, 0.28, 0.25, 0.22]
val_loss = [0.92, 0.78, 0.68, 0.59, 0.54, 0.51, 0.49, 0.48, 0.47, 0.47]
# plt.figure(figsize=(8, 4)) # Set canvas size (width, height in inches)
# plt.plot(epochs, train_loss, color='blue', label='Training Loss', linewidth=2)
# plt.plot(epochs, val_loss, color='orange',label='Validation Loss', linewidth=2)
# plt.title('Model Training Loss Curve') # Chart title
# plt.xlabel('Epoch') # X-axis label
# plt.ylabel('Loss') # Y-axis label
# plt.legend() # Show the legend box
# plt.grid(True, alpha=0.3) # Add light gridlines
# plt.tight_layout()
# plt.savefig('loss_curve.png', dpi=150) # Save to file
# plt.show()
# # for bar graph
# plt.figure(figsize=(8, 4))
# x = np.arange(len(epochs))
# width = 0.35
# plt.bar(x - width/2, train_loss, width, label='Training Loss')
# plt.bar(x + width/2, val_loss, width, label='Validation Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.title('Model Training Loss Curve')
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.savefig('loss_curve_bar.png', dpi=150)
# plt.show()


# #for scatter graph
# plt.figure(figsize=(8, 4))
# scatter_size = 100
# plt.scatter(epochs, train_loss, color='blue', label='Training Loss', s=scatter_size)
# plt.scatter(epochs, val_loss, color='orange', label='Validation Loss', s=scatter_size)
# plt.title('Model Training Loss Curve')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.savefig('loss_curve_bar.png', dpi=150)
# plt.show()


# def word_count(sentence):
#     words = sentence.split(" ")
#     count = len(words)                 
#     return count

# def word_count_fixed(sentence):
#     words = sentence.split()
#     count = len(words)                 
#     return count

# print("Buggy:", word_count_fixed(""))   
# print("Fixed:", word_count_fixed("hello   world"))  

  
# def get_initials_fixed(full_name):
#     parts = full_name.split()
#     initials = ""
#     for part in parts:
#         initials += part[0]             
#     return initials.upper()

# print("Fixed:", get_initials_fixed("Alice Bob Charlie"))  # ABC
# print("Fixed:", get_initials_fixed(""))  