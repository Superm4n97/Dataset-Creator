a = "add"
b = "acb"

if (a<b):
    print("correct")
else:
    print("incorrect")

fileobject = open("test.txt","a")

lst = ["hello","Rasel","Hossain"]

fileobject.write("Hello")
fileobject.writelines(lst)
fileobject.close()

fileobject = open("test.txt","r+")
print(fileobject.read())
