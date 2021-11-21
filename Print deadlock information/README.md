## Prints deadlock information from error log, into seperate text files grouped by id number <br>
Looks for patterns that match "Deadlock Id [0-9]+ detected" and "End of deadlock information" to mark the beginning and end of a deadlock information, respectively. <br>

### Drawback <br>
Script assumes that the **two patterns are not present in the same line**


