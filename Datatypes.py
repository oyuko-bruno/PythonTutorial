#list
#dictionary
#tupples
#list mutable,ordred
#mylist =["Bruno","Joan"]
#tuple immutable orderd
#my_tuple = ("kenya","uganda","somali")
#print(my_tuple)

#print(f"My country is {my_tuple[0]}")
#list is like arrays in other programming language
#set unordered
#fruits={"oranges","pinnaples","mangoes"}
#print(fruits)
#Dictionaries

#if else statements
#num = int(input("Enter number:  "))
#if num >=0:
 #   print("The number is positive")
#else:
 #   print("The number is negative")
#num2 = int(input("Enter number:  "))
#if num2 %2==0:
 #   print("Number even")
##3else:
 #   print("number is odd")

marks= int(input("Enter Marks  :"))

if marks >80 and marks <= 100:
    print ("You got A")
elif marks >60 and marks <= 80:
    print("You got B")
elif marks> 40 and marks <=60:
    print("you got C")
elif marks >100 and marks < 0:
    print("Please Enter valid Marks")

else:
    print("Soory you Fail")




mylist=["kenya","uganda","tanzania"]
myname = "Bruno"
for i in mylist:
    print(i)
    if i=="uganda":
        break
for name in myname:
    print(name)
#neccested loop
#pallindrome of a number