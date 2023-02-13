'''Write a program which basically sum all the integers from the sample_input
string and returns the final result.Sample_input =”PRA12Ga782d45601$3”'''

#Enter Any String
string=input()

# Function to sum integers present in String
def stringsum(string):
    """Function to sum integers present in String"""
    sum=0
    for i in range(len(string)):
        if string[i].isnumeric():
            sum+=int(string[i])
    return sum

# Calling Function to Find Result
print(stringsum(string))
