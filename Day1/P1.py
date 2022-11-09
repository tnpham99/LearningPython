<<<<<<< HEAD
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

=======
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
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
<<<<<<< HEAD
        if txt[i] == char:
=======
        if txt[i:i+len(char)] == char:
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
            myindex = i
            break
    return myindex

print(findchar('hello my name is tram','a'))
<<<<<<< HEAD
print(findchar('hello my name is tram','z'))
=======
print(findchar('hello my name is tram','my'))
print(findchar('hello my name is tram','z'))
print(findchar('hello my name is tram','lo'))
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
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
<<<<<<< HEAD
        if txt[i] == char:
=======
        if txt[i:i+len(char)] == char:
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
            myindex.append(i)
    return myindex

print(findchars('hello my name is tram','a'))
<<<<<<< HEAD
print(findchars('hello my name is tram','m'))
print(findchars('hello my name is tram','z'))
=======
print(findchars('hello my name is tram','my'))
print(findchars('hello my name is tram','z'))
print(findchars('hello my name is tram','lo'))
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
print(findchars('hello my name is tram','a',12))
print(findchars('hello my name is tram','m',8,12))
print(findchars('ohmymymyabcdefmy','my'))
print('-'*20)

#Convert string into lower case
txt = 'Hello, And Welcome To My World!'
print(txt.lower())

def lowerstr(txt):
    uppertolower = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
    for i in range(len(txt)):
<<<<<<< HEAD
        if txt[i] in uppertolower:
=======
        if txt[i] in uppertolower.keys():
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
            txt = txt[0:i] + uppertolower[txt[i]] + txt[i+1:]
    return txt

print(lowerstr('Hello, And Welcome To My World!'))
print(lowerstr('HSKHNKXjkjskfeKWEOIIHF'))
print(lowerstr('hello how are you'))
print('-'*20)

#upper case all characters
def upperstr(txt):
    lowertoupper = {'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    for i in range(len(txt)):
<<<<<<< HEAD
        if txt[i] in lowertoupper:
=======
        if txt[i] in lowertoupper.keys():
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
            txt = txt[0:i] + lowertoupper[txt[i]] + txt[i+1:]
    return txt

print(upperstr('Hello, And Welcome To My World!'))
print(upperstr('HSKHNKXjkjskfeKWEOIIHF'))
print(upperstr('HELLO HOW ARE YOU'))
print('-'*20)

<<<<<<< HEAD
#count the number of times a specified character appears in the string
def countvalue(txt,char,start=None,end=None):
    return len(findchars(txt,char,start,end))

print(countvalue('hello my name is tram','a'))
print(countvalue('hello my name is tram','z'))
print(countvalue('hello my name is tram','a',12))
print(countvalue('hello my name is tram','m',8,12))
print(countvalue('ohmymymyabcdefmy','m'))
=======
#count the number of times a specified value appears in the string
def countvalue(txt,char,start=None,end=None):
    count = 0
    for i in findchars(txt,char,start,end):
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
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
print('-'*20)

#string capitalize method: change first character in a string to upper case, while other characters remain lower case
def capitalizestr(txt):
<<<<<<< HEAD
=======
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584
    if txt[0] in alphabet:
        txt = upperstr(txt[0]) + txt[1:]
    return txt

print(capitalizestr('zebras are African equines with distinctive black-and-white striped coats.'))
print(capitalizestr('All string methods returns new values. They do not change the original string.'))
print(capitalizestr('HELLO WORLD'))
print('-'*20)

#isupper() - returns True if all characters in the string are upper case
def isuppercase(txt):
<<<<<<< HEAD
    for i in txt:
        if i in alphabet:
            return False
    return True
=======
    if txt == upperstr(txt):
        return True
    return False
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584

print(isuppercase('Hello World!'))
print(isuppercase('hello 123'))
print(isuppercase('MY NAME IS PETER'))
print('-'*20)

#islower() - returns True if all characters in the string are lower case
def islowercase(txt):
<<<<<<< HEAD
    for i in txt:
        if i not in alphabet:
            return False
    return True
=======
    if txt == lowerstr(txt):
        return True
    return False
>>>>>>> cfed6c69c379ba04d51b5d2031397ebecf5e3584

print(islowercase('Hello World!'))
print(islowercase('hello 123'))
print(islowercase('mynameisPeter'))
print('-'*20)

#isalpha() - returns True if all characters in the string are in the alphabet
def isalphabet(txt):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(txt)):
        if lowerstr(txt[i]) in alphabet:
            if i == len(txt)-1:
                return True
        else:
            return False

print(isalphabet('CompanyX'))
print(isalphabet('Company10'))
print(isalphabet('123'))
print('-'*20)

#isspace() - returns True if all chracters in the string are whitespaces
def iswhitespaces(txt):
    for i in range(len(txt)):
        if txt[i] == " ":
            if i == len(txt)-1:
                return True
        else:
            return False

print(iswhitespaces('   '))
print(iswhitespaces('    s    '))
print('-'*20)