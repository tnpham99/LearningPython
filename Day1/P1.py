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

#Convert string into lower case
txt = 'Hello, And Welcome To My World!'
print(txt.lower())

def lowerstr(txt):
    for i in range(len(txt)):
        if txt[i] == 'A':
            txt = txt[0:i] + 'a' + txt[i+1:]
        elif txt[i] == 'B':
            txt = txt[0:i] + 'b' + txt[i+1:]
        elif txt[i] == 'C':
            txt = txt[0:i] + 'c' + txt[i+1:]
        elif txt[i] == 'D':
            txt = txt[0:i] + 'd' + txt[i+1:]
        elif txt[i] == 'E':
            txt = txt[0:i] + 'e' + txt[i+1:]
        elif txt[i] == 'F':
            txt = txt[0:i] + 'f' + txt[i+1:]
        elif txt[i] == 'G':
            txt = txt[0:i] + 'g' + txt[i+1:]
        elif txt[i] == 'H':
            txt = txt[0:i] + 'h' + txt[i+1:]
        elif txt[i] == 'I':
            txt = txt[0:i] + 'i' + txt[i+1:]
        elif txt[i] == 'J':
            txt = txt[0:i] + 'j' + txt[i+1:]
        elif txt[i] == 'K':
            txt = txt[0:i] + 'k' + txt[i+1:]
        elif txt[i] == 'L':
            txt = txt[0:i] + 'l' + txt[i+1:]
        elif txt[i] == 'M':
            txt = txt[0:i] + 'm' + txt[i+1:]
        elif txt[i] == 'N':
            txt = txt[0:i] + 'n' + txt[i+1:]
        elif txt[i] == 'O':
            txt = txt[0:i] + 'o' + txt[i+1:]
        elif txt[i] == 'P':
            txt = txt[0:i] + 'p' + txt[i+1:]
        elif txt[i] == 'Q':
            txt = txt[0:i] + 'q' + txt[i+1:]
        elif txt[i] == 'R':
            txt = txt[0:i] + 'r' + txt[i+1:]
        elif txt[i] == 'S':
            txt = txt[0:i] + 's' + txt[i+1:]
        elif txt[i] == 'T':
            txt = txt[0:i] + 't' + txt[i+1:]
        elif txt[i] == 'U':
            txt = txt[0:i] + 'u' + txt[i+1:]
        elif txt[i] == 'V':
            txt = txt[0:i] + 'v' + txt[i+1:]
        elif txt[i] == 'W':
            txt = txt[0:i] + 'w' + txt[i+1:]
        elif txt[i] == 'X':
            txt = txt[0:i] + 'x' + txt[i+1:]
        elif txt[i] == 'Y':
            txt = txt[0:i] + 'y' + txt[i+1:]
        elif txt[i] == 'Z':
            txt = txt[0:i] + 'z' + txt[i+1:]
    return txt

print(lowerstr('Hello, And Welcome To My World!'))
print(lowerstr('HSKHNKXjkjskfeKWEOIIHF'))
print(lowerstr('hello how are you'))
print('-'*20)

#upper case all characters
def upperstr(txt):
    for i in range(len(txt)):
        if txt[i] == 'a':
            txt = txt[0:i] + 'A' + txt[i+1:]
        elif txt[i] == 'b':
            txt = txt[0:i] + 'B' + txt[i+1:]
        elif txt[i] == 'c':
            txt = txt[0:i] + 'D' + txt[i+1:]
        elif txt[i] == 'd':
            txt = txt[0:i] + 'D' + txt[i+1:]
        elif txt[i] == 'e':
            txt = txt[0:i] + 'E' + txt[i+1:]
        elif txt[i] == 'f':
            txt = txt[0:i] + 'F' + txt[i+1:]
        elif txt[i] == 'g':
            txt = txt[0:i] + 'G' + txt[i+1:]
        elif txt[i] == 'h':
            txt = txt[0:i] + 'H' + txt[i+1:]
        elif txt[i] == 'i':
            txt = txt[0:i] + 'I' + txt[i+1:]
        elif txt[i] == 'j':
            txt = txt[0:i] + 'J' + txt[i+1:]
        elif txt[i] == 'k':
            txt = txt[0:i] + 'K' + txt[i+1:]
        elif txt[i] == 'l':
            txt = txt[0:i] + 'L' + txt[i+1:]
        elif txt[i] == 'm':
            txt = txt[0:i] + 'M' + txt[i+1:]
        elif txt[i] == 'n':
            txt = txt[0:i] + 'N' + txt[i+1:]
        elif txt[i] == 'o':
            txt = txt[0:i] + 'O' + txt[i+1:]
        elif txt[i] == 'p':
            txt = txt[0:i] + 'P' + txt[i+1:]
        elif txt[i] == 'q':
            txt = txt[0:i] + 'Q' + txt[i+1:]
        elif txt[i] == 'r':
            txt = txt[0:i] + 'R' + txt[i+1:]
        elif txt[i] == 's':
            txt = txt[0:i] + 'S' + txt[i+1:]
        elif txt[i] == 't':
            txt = txt[0:i] + 'T' + txt[i+1:]
        elif txt[i] == 'u':
            txt = txt[0:i] + 'U' + txt[i+1:]
        elif txt[i] == 'v':
            txt = txt[0:i] + 'V' + txt[i+1:]
        elif txt[i] == 'w':
            txt = txt[0:i] + 'W' + txt[i+1:]
        elif txt[i] == 'x':
            txt = txt[0:i] + 'X' + txt[i+1:]
        elif txt[i] == 'y':
            txt = txt[0:i] + 'Y' + txt[i+1:]
        elif txt[i] == 'z':
            txt = txt[0:i] + 'Z' + txt[i+1:]
    return txt

print(upperstr('Hello, And Welcome To My World!'))
print(upperstr('HSKHNKXjkjskfeKWEOIIHF'))
print(upperstr('HELLO HOW ARE YOU'))
print('-'*20)

#count the number of times a specified value appears in the string
def countvalue(txt,char,start=None,end=None):
    count = 0
    for i in range(len(findchars(txt,char,start,end))):
        count += 1
    return count

print(countvalue('hello my name is tram','a'))
print(countvalue('hello my name is tram','my'))
print(countvalue('hello my name is tram','z'))
print(countvalue('hello my name is tram','lo'))
print(countvalue('hello my name is tram','a',12))
print(countvalue('hello my name is tram','m',8,12))
print(countvalue('ohmymymyabcdefmy','my'))
print(countvalue('I love apples, apple are my favorite fruit','apple'))
print('-'*20)

#endswith() - returns true if the string ends with the specified value
#def isendswith(txt,char)

#isupper() - returns True if all characters in the string are upper case
def isuppercase(txt):
    if txt == upperstr(txt):
        return True
    return False

print(isuppercase('Hello World!'))
print(isuppercase('hello 123'))
print(isuppercase('MY NAME IS PETER'))
print('-'*20)

#islower() - returns True if all characters in the string are lower case
def isuppercase(txt):
    if txt == lowerstr(txt):
        return True
    return False

print(isuppercase('Hello World!'))
print(isuppercase('hello 123'))
print(isuppercase('mynameisPeter'))
print('-'*20)

#isalpha() - returns True if all characters in the string are in the alphabet
def isalphabet(txt):
    for i in range(len(txt)):
        if txt[i] == 'A' or 'a' or 'B' or 'b' or 'C' or 'c' or 'D' or 'd' or 'E' or 'e' or 'F' or 'f' or 'G' or 'g' or 'H' or 'h' or 'I' or 'i' or 'J' or 'j' or 'K' or 'k' or 'L' or 'l' or 'M' or 'm' or 'N' or 'n' or 'O' or 'o' or 'P' or 'p' or 'Q' or 'q' or 'R' or 'r' or 'S' or 's' or 'T' or 't' or 'U' or 'u' or 'V' or 'v' or 'W' or 'w' or 'X' or 'x' or 'Y' or 'y' or 'Z' or 'z':
            if i == len(txt):
                return True
        else:
            return False

print(isalphabet('CompanyX'))
print(isalphabet('Company10'))
print(isalphabet('123'))
print('-'*20)