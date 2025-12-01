import os
#   r = Read
#   a = Append
#   w = Write
#   x = Create

#   Read
#f = open("names.txt")
#print(f.read())
#print(f.read(4))
#print(f.readline())

#for line in f:
#    print(line)

#f.close()

#   Append
#f = open("names.txt", "a")
#f.write("\n11. Kim")
#f.close()

#f = open("names.txt")
#print(f.read())
#f.close()

#   Write (overwrite)
#f = open("context.txt", "w")
#f.write("I deleted all selenium context")
#f.close()

f = open("context.txt")
print(f.read())
f.close()

#   Two ways to create new file
#   opens file for writing, create the file if it doesn't exist
#f = open("more_names.txt", "w")
#f.close()

#   Creates the specified file, but returns error if the file exists
#if not os.path.exists("selenium.txt"):
#    f = open("selenium.txt", "x")
#    f.close()

#   Delete a file

#   avoid error if it doesn't exist
if os.path.exists("selenium.txt"):
    os.remove("selenium.txt")
else:
    print("The file 'selenium.txt' does not exist")

with open("docs.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)

