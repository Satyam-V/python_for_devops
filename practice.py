#####defining function within function calling function as per need
# a = 27
# b = 7
# def add_two_num(a, b): 
#     sum = a + b
#     print(sum)
# def isgreater(a, b):
#     if (a > b):
#         print("1st is greater")
#     else:
#      print("2nd is greater")
# add_two_num(a, b)
# isgreater(a, b)
# c = 9
# d = 30
# add_two_num(c, d)
# #isgreater(f, g) (here it will give syntax error as value of f and g is not defined)

# f = 34
# g = 55
# add_two_num(f, g)
# isgreater(f, g)
# isgreater(c, d)
# def islesser(a, b): # one usecase to pass to complete function later
#    pass
# #### now lets talk about passing arguments to the function###
# def add_two_num(a=5, b=10): 
#     sum = a + b
#     print(sum)
# add_two_num()
# ###2nd way###
# def add_two_num(a=5, b=10): 
#     sum = a + b
#     print(sum)
# add_two_num(1, 5)
# ####3rd way
# def add_two_num(a=5, b=10): 
#     sum = a + b
#     print(sum)
# add_two_num(10)
# ###4th
# def add_two_num(a=5, b=10): 
#     sum = a + b
#     print(sum)
# add_two_num(b=110)
#### this is the only correct way if you are taking input
# a = int(input("Input the first number : ")) 
# b = int(input("Input the second number :"))
# def add_two_num(a, b): 
#     # a = int(input("Input the first number : ")) 
#     # b = int(input("Input the second number :"))
#     sum = a + b
#     print("The sum of given two numbers is", sum)
# add_two_num(a, b)
########
# def add_two_num(a, b): 
#     a = int(input("Input the first number : "))
#     b = int(input("Input the second number :"))
#     sum = a + b
#     print("The sum of given two numbers is", sum)
# add_two_num(10, 15)
######
# def add_two_num():
#     sum = a + b
#     a = int(input("Input the first number : "))
#     b = int(input("Input the second number :"))
#     if (a== 10):
#         print("The sum of given two numbers is", sum)
#     else:
#         print("Sorry")
# add_two_num()
##### Return function ####
def name(**name): 
    print(type(name))
    print("Hello,", name["fname"],
          name["mname"], name["lname"])
name(mname = "buchan", lname = "barnes", fname = "james")
#############
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))
average(7, 6, 8, 9)
average(7, 6)
##### return statement######
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)##basically return output ko save krta hai niche jaisa kiya hai hmne
###RETURN FUNCTION IS USED TO RETURN(STORE) THE VALUE OF THE EXPRESSION BACK TO THE CALLING FUNCTION
c = average(10, 20)
print(c)
##String slicing
# name = "satyam"
# print(name[1])
# print(name[1:3])
# print(name[0:len(name)])
# print(len(name))
# print(name[-5:-3]) # = print(name[len(name)-5:len(name)-3])
# print(name[len(name)-5:len(name)-3])
##String methods#######
##strings are imutable (not changeable)to make it mmutable we create a copy of it
# a = "satyam"
# print(a.upper())
# # print(a.lower()) ####sting methods make a copy of new string and operate on it
# print(a.replace("satyam", "aarohi"))
# b = "satyam aarohi"
# print(b.split(" "))# split into seperate strigs where spaces are available
# blogheading = "introduction to Python"
# print(blogheading.capitalize()) #capitalizethe first letter of string and converts other letter into small
# d = "satyam"
# print(d.count("a"))
# ###str1 = "my name is satyam" and i am in love with aarohi" # incorrect
# str1 = '"my name is "satyam" and i am in love with "aarohi"' ## correct
# print(str1.title())
# print(str1.find("z"))


########Decision making conditional statements#######
##### if, else, elseif ########
# def sum(a, b):
#     sum = a + b
# print(sum)
# sum(10, 15)
# # a = int(input("Enter the numbe:"))
# # b = int(input("enter the number:"))
# # sum = a + b
# # if(sum==int(input())):
# #         print("sum is:", sum)
# # elif(sum==int(input())):
# #         print(sum + 1)
# # else:
# #         print("sum is not:", sum)
        
# # print("Satyam")
# ########case statement##########
# x = int(input("please enter number:"))
# # match x:
#     case 0:    #ist case
#         print("x is zero")
#     case 4:    ###2nd case and so on
#         print("case is 4")
#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(" not matched")
#     case _:
#         print(x)
# # ###time program#####
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# # if(timestamp = int(time.strftime('%H')))
#### Loops we use to perform repeating works###
####We have For and while loop### we can use it seperately and together also i.e.
# #### we can use while loop inside for and for inside while loop and this is called as nested loops
##to iterate over a sequence of objects we use for loops##
## lets see for loop First###
# name = "satyam"
# for i in name:
#     print(i, end=",")
#     if(i =="t"):
#         print("this is middle")
#     elif (i == "m"):
#           print("last")
#     elif (i == "s"):
#          print("start")
#     else:
#          print("middle not found") 

#     ###the above program will iterate through each letter of name satyam###
#     ###Lets talk about range function
#     # for k in range(1, 10):
#     #     print(k)
# for k in range(10):
#         print(k)
    ##yha tk complete program hai or isko smjhna bhut jaruri hai
#####Lets see while loop
###emulate while loop
# i = int(input()) #initializing i
# while(i<=31):
#     i = int(input()) ### taking input
    

#     print(i)
###Decrementing while loop
# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1
# #####Incrementing while loop
# j = 0
# while (j < 10):
#     print(j)
#     j = j + 1
#### infinite loop
# count = 0
# while (count >=0):
#     print(count)
#     count = count + 1
##Break and Continue (break is used when you want to exit at particular iteration)
# for i in range(12): # 
#     if(i == 10):
#      break
#     print("5X", i+1, "=", 5 * (i+1))
# for i in range(12): # 
#     if(i == 10):
#         continue    #continue is used when you want to skip a particular iteratrion
#     print("5X", i+1, "=", 5 * (i+1))
# for i in range(10):
#    print(i) ####0....9
# for i in range(1, 10):
#  print(i) ###1......9
###emulate do while loop
### when i =100 it will come out of the loop 
# i = 0
# while True:
#     print(i)
#     i = i +1
#     if(i%100 == 0):
#         break



