'''
Created on Oct 24, 2016

@author: Ravi Sankar Karuturi
'''

def add(a,b):
    return a+b

def addFixedValue(a):
        y = 5
        return y +a

print add(1,2)
print addFixedValue(1)

s = "abcdefg"
assert (s[0:4]=="abcd")
assert ( s[4:]=="efg")
assert ("abcdefg"[4:0]=="")
assert ("abcdefg"[0:2]=="ab")