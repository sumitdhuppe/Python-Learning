str1="this is string"
str2='this is string'
str3='''this is string'''

print(str1)
print(str2)
print(str3)
#basicaly we are going to use the double inverted quama

#concatination means addition of str
str1="sumit"
str2="dhuppe"
print(str1+str2)
print(len(str1))#printing the lengthof the str1
final_str=str1+""+str2
print(len(final_str))

#indexing sumit that is starting from0
str="dhuppe_sumit"
char=str[0]
print(char)

str1="balaji kirana"
print(str1[4])

#slicing the letters
str3="balaji kirana"
print(str3[0:14])
print(str3[0:8])
print(str3[:14])
print(str3[0:])
print(str3[-3:-1])#they are also using the - slicing they are starting to give -1 from end
#using the string functions
str="i am started to learn the python programming"
print(str.endswith("app"))#returns true if string ends with substr
print(str.capitalize())#capitalize the first character
print(str.replace("i","he"))#replace all occurrences of old
print(str.find("am"))#returns the first index of first occurrence
print(str.count("am"))#count the occurrence of substr

#question

name=input("enter your first name")
print("lenth of your name is",len(name))