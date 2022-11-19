#Question: https://leetcode.com/problems/defanging-an-ip-address/
def defangIPadd(ip):
    new_ip = ip.replace('.','[.]')
    return new_ip

print(defangIPadd("1.1.1.1"))
print(defangIPadd("255.100.50.0"))

#Replace function to take in 3 parameters: (1) original string, (2) old character needed changes, and (3) new character to replace
def replace(og_str, old_value, new_value):
    p = []
    for i in range(len(og_str)):
        if og_str[i] == old_value:
            p.append(i)
    
    if len(p) == 0:
        return og_str
    
    new_str = og_str
    for j in p:
        new_str = new_str[:j] + new_value + new_str[j+1:]
    return new_str

print(replace('Hello how are you','o','u'))
print(replace('My name is Tram','u','o'))
print(replace('Oh my god','o','u'))
print(replace('uuuuu','u','o'))

#Same question above but with value is a group of characters
def replacechars(og_str, old_value, new_value, count=None):
    p = []
    if count is None:
        count = len(og_str)
    for i in range(len(og_str)+1-len(old_value)):
        if count != 0:
            for j in range(len(old_value)):
                if og_str[i+j] == old_value[j]:
                    if j == len(old_value)-1:
                        p.append(i)
                        count -= 1
                else:
                    break
        else:
            break
    
    if len(p) == 0:
        return og_str
    
    new_str = og_str
    for j in range(len(p)):
        k = p[j] + j * (len(new_value)-len(old_value))
        new_str = new_str[:k] + new_value + new_str[k+len(old_value):]
    return new_str

print(replacechars('-de-----de----de---------de','de','x',3))
# print(replacechars('abcdefghi','xyz','mno'))
# print(replacechars('abcdefaeu','abc','xyz'))
# print(replacechars('abcdefabc','abc','xyz'))
# print(replacechars('abcdefghi','ghi','xyz'))
# print(replacechars('abcdefghi','def','mnop'))
# print(replacechars('abcdefghi','defg','mno'))
