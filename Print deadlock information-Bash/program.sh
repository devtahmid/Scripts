#!/bin/bash

original="log.txt"
input="log_copy.txt"
cp $original $input
echo -e "\nAppended line"  | tee -a log_copy.txt  #while loop reads till 2nd last line of file, hence adding a new line

counter=0
newFileOpened=0 #false
zero=0


while IFS= read -r line
do
 if [ $newFileOpened -eq 0 ]
  then 
   if [[ $line =~ .*server.*Deadlock.Id.[0-9]+.detected.* ]]; then
    idNum=$(echo "$line"| cut -d ' ' -f7)
    newFileName="$idNum.txt"
    newFileOpened=1
    echo -e $line >> $newFileName
   fi
 else
  echo -e $line >> $newFileName
  if [[ $line =~ .*End.of.deadlock.information.* ]]; then
    newFileOpened=0  
  fi
    
 fi
done <"$input"

echo -e "done\n"