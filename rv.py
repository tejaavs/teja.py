def rev(str):
   vowel=('a','e','i','o','u')
   for i in str:
   if i in vowel:
   str=str.replace(i,"")
   print(str[::-1])
a=int(input(""))
str=input("")
rev(str)
   
