# pattern-matching-paths

This repository solves the problem of how to match paths divided up into fields (comma separated) with patterns. 

The input is a simple file with the following format

2     
pattern1  
pattern2  
2   
path1  
path2  

The first number is the number of patterns.  
The second number is the number of paths.  
Pattern fields are separated with commas.
Path fields are separated with forward slashes '/'.

You can run this at the command line with the following:  
**cat name_of_input_file | python3 run.py**

You can run the unit tests at the command line with the following:  
**python3 -m unittest PatternTests**  
 
