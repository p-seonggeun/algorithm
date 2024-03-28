import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
string = ''

for index, i in enumerate(s) :
    if i == '(' or i == '[' or not stack :
        if index != 0 :
            if string[-1].isdigit() :
                string += '+'
        string += '('
        stack.append(i)
    elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') :
        stack.pop()
        if string[-1].isdigit() :
            string += ')*'
            if i == ')' :
                string += '2'
            else :
                string += '3'
        else :
            if i == ')' :
                string = string[:-1] + '2'
            else :
                string = string[:-1] + '3'

if stack :
    print(0)
else :
    print(eval(string))