## Prints deadlock information from error log, into seperate text files grouped by id number <br>
Looks for patterns that match "Deadlock Id [0-9]+ detected" and "End of deadlock information" to mark the beginning and end of a deadlock information, respectively. <br>

## Operating <br>
Run the script in the same folder as the log file <br> 
1. Assign $original as the name of the log file <br>
2. $input will be a duplicate file which will be appended by an extra line. This is required so the loop is able to read till the last line <br>


### Drawback <br>
Script assumes that the two patterns are not present in the same line, and there is only one occurence of a pattern in a single line

