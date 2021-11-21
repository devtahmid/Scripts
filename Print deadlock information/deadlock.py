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
