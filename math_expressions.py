"""Find which math expression matches the answer that you are given, if you have an integer answer, and a list of math expressions.

Task: 
Test each math expression to find the first one that matches the answer that you are given.

Input Format: 
Two inputs: an integer and a space separated string of math expressions. The following operations need to be supported: addition +, subtraction -, multiplication *, division /. 
An expression can include multiple operations.

Output Format: 
A string that tells the index of the first math expression that matches. If there are no matches, output 'none'.

Sample Input: 
15
(2+100) (5*3) (14+1)

Sample Output: 
index 1"""

"""Solution By: Haris Jafri"""


def math_oper_index(output,operation_string):
    operation_list = operation_string.split(" ")
    for i,x in enumerate(operation_list):
        result = eval(x)
        count = 0
        if result==output:
            return "The Math Expression at Index {} results in the desired Output".format(i)
            count+=1
            break
    if count==0:
        return "None of the Math Expressions provided will result in the desired Output you provided"
    

op = int(input("Enter the Expected Output of the Math Expressions you want to give:-->"))
st = input("Enter the list of Math Expressions with space in between:-->")

result = math_oper_index(op,st)

print(result)