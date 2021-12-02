#!/bin/bash

original="log.txt"
input="log_copy.txt"
cp $original $input
echo -e "\nAppended line"  | tee -a $input  #while loop reads till 2nd last line of file, hence adding a new line

newFileOpened=0 #false

while IFS= read -r line
do
 if [ $newFileOpened -eq 0 ]
  then
  echo "$line"
  value="$(grep -Eq ".*server.*Deadlock.Id.[0-9]+.detected.*" <<< $line)"
   if [[ $? -eq 0 ]] ; then
    echo -e "\ntest1\n"
    echo "$value"
    value="$(grep -Eo "server.*Deadlock.Id.[0-9]+.detected" <<< $line)"
    echo "$value"
    idNum=$(echo "$value"| cut -d ' ' -f5)
    echo $idNum
    newFileName="$idNum.txt"
    newFileOpened=1
    echo -e $line >> $newFileName
   fi
 else
  echo -e $line >> $newFileName
  echo -e "\ntest2\n$newFileOpened\n"
  value="$(grep -Eq "End.of.deadlock.information" <<< $line)"
  echo $value
  echo -E "\ntest3\n$newFileOpened\n"
  echo -E "$line"
  testvalue="$(grep -Eo "End.of.deadlock.information" <<< $line)"
  if [[ $? -eq 0 ]]
  then
   newFileOpened=0
   echo -e "\ntest4\n$newFileOpened\n$testvalue\n"  
   echo -E "$line\n"
  fi
    
 fi
done <"$input"

echo -e "done\n"