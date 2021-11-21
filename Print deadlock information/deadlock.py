import re
readFileName= input("Enter exact file name along with extension: ")
logFile = open(readFileName, "r")
myline = logFile.readline()
matchFound= False
newFileOpened = False

while myline:
  if newFileOpened==False :
    deadlockStart = re.search(r"(Deadlock Id [0-9]+ detected)+", myline)
    if deadlockStart:
      matchFound= True
      idNum = re.search(r"[0-9]+", deadlockStart.group())
      newFilename= idNum.group() + ".txt"
      newFile = open(newFilename,'w')
      newFileOpened = True
      newFile.write(myline+"\n")
  else:
    newFile.write(myline+"\n")
    deadlockEnd = re.search(r"End of deadlock information", myline)
    if deadlockEnd:
      newFile.close()
      newFileOpened = False
  print(myline)
  myline = logFile.readline()

logFile.close()







'''

file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes

file1 = open("myfile.txt","r+")

print ("Output of Read function is ")
print (file1.read())

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print ("Output of Readline function is ")
print (file1.readline())


file1.seek(0)

# To show difference between read and readline
print ("Output of Read(9) function is ")
print (file1.read(9))

file1.seek(0)

print ("Output of Readline(9) function is ")
print (file1.readline(9))

file1.seek(0)
# readlines function
print ("Output of Readlines function is ")
print (file1.readlines())
print
file1.close()
'''