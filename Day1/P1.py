#string capitalize method: change first character in a string to upper case, while other characters remain lower case
from gettext import find


a = "hello, how are you?"
print(a.capitalize())

def capitalizestr(txt):
    if txt[0] == 'a':
        new_txt = 'A' + txt[1:]
    elif txt[0] == 'b': #question: why elif but not if after the first if statement?
        new_txt = 'B' + txt[1:]
    elif txt[0] == 'c':
        new_txt = 'C' + txt[1:]
    elif txt[0] == 'd':
        new_txt = 'D' + txt[1:]
    elif txt[0] == 'e':
        new_txt = 'E' + txt[1:]
    elif txt[0] == 'f':
        new_txt = 'F' + txt[1:]
    elif txt[0] == 'g':
        new_txt = 'G' + txt[1:]
    elif txt[0] == 'h':
        new_txt = 'H' + txt[1:]
    elif txt[0] == 'i':
        new_txt = 'I' + txt[1:]
    elif txt[0] == 'j':
        new_txt = 'J' + txt[1:]
    elif txt[0] == 'k':
        new_txt = 'K' + txt[1:]
    elif txt[0] == 'l':
        new_txt = 'L' + txt[1:]
    elif txt[0] == 'm':
        new_txt = 'M' + txt[1:]
    elif txt[0] == 'n':
        new_txt = 'N' + txt[1:]
    elif txt[0] == 'o':
        new_txt = 'O' + txt[1:]
    elif txt[0] == 'p':
        new_txt = 'P' + txt[1:]
    elif txt[0] == 'q':
        new_txt = 'Q' + txt[1:]
    elif txt[0] == 'r':
        new_txt = 'R' + txt[1:]
    elif txt[0] == 's':
        new_txt = 'S' + txt[1:]
    elif txt[0] == 't':
        new_txt = 'T' + txt[1:]
    elif txt[0] == 'u':
        new_txt = 'U' + txt[1:]
    elif txt[0] == 'v':
        new_txt = 'V' + txt[1:]
    elif txt[0] == 'w':
        new_txt = 'W' + txt[1:]
    elif txt[0] == 'x':
        new_txt = 'X' + txt[1:]
    elif txt[0] == 'y':
        new_txt = 'Y' + txt[1:]
    elif txt[0] == 'z':
        new_txt = 'Z' + txt[1:]
    else:
        return txt
    return new_txt

print(capitalizestr("ah it's me"))
print(capitalizestr('hello how are you'))
print(capitalizestr('Hi my name is Tram'))
print(capitalizestr('zebras are African equines with distinctive black-and-white striped coats.'))
print(capitalizestr('All string methods returns new values. They do not change the original string.'))
print('-'*20)

#string find method
txt = 'Hello my name is Tram'
print(txt.find('a'))
print(txt.find('my'))

#find the position of the first occurrence of a character in a string
def findchar(txt,char,start=None,end=None):
    myindex = -1
    if start is None:
        start = 0
    if end is None:
        end = len(txt)
    for i in range(start,end):
        if txt[i:i+len(char)] == char:
            myindex = i
            break
    return myindex

print(findchar('hello my name is tram','a'))
print(findchar('hello my name is tram','my'))
print(findchar('hello my name is tram','z'))
print(findchar('hello my name is tram','lo'))
print(findchar('hello my name is tram','a',12))
print(findchar('hello my name is tram','m',8,12))
print('-'*20)

#find the positions of all occurrences of a character in a string
def findchars(txt,char,start=None,end=None):
    myindex = []
    if start is None:
        start = 0
    if end is None:
        end = len(txt)
    for i in range(start,end):
        if txt[i:i+len(char)] == char:
            myindex.append(i)
    return myindex

print(findchars('hello my name is tram','a'))
print(findchars('hello my name is tram','my'))
print(findchars('hello my name is tram','z'))
print(findchars('hello my name is tram','lo'))
print(findchars('hello my name is tram','a',12))
print(findchars('hello my name is tram','m',8,12))
print(findchars('ohmymymyabcdefmy','my'))
print('-'*20)

#find and capitalize a character