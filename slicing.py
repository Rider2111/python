#this is about slicing and other operations on string

str = "Why pluto is not a planet?"
print(str)
print(len(str))

#for slicing of string we can use the following methods
print(str[0:5])
print(str[:5])
print(str[:])
print(str[0:-10])
print(str[-10:26])

#string methods
# Strings are immutable!!!

print(str.upper())
print(str.lower())
print(str.rstrip("?")) # removes the ? from string
print(str.replace("not","obviously")) #for replacing something in the string wherever it exists
print(str.split(" "))

str1 = 'this is a heading for an article'
print(str1.capitalize())
print(str1.center(50))
print(len(str1), len(str1.center(10)))

print(str.endswith("?"))
print(str.find("not"))
print(str.index("not"))

print(str.isalnum())
str2= 'heyidonotknowwhattotype63600'
print(str2.isalnum())