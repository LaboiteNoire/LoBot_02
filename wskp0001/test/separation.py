import string
import random as rd


"""
txt = ""
for k in range(1022):
    txt = txt + rd.choice(string.ascii_letters)


def separeStr(txt : str , value : int):
    if len(txt) <= value:
        return [txt]
    else:
        return [txt[:value]] + separeStr(txt[value:],value) 
"""
txt = ""
for k in range(rd.randint(0,4)):
    stxt = ""
    first_action = False
    for j in range(rd.randint(0,10)):
        stxt = stxt + rd.choice(string.ascii_letters)
    txt = txt + "  " + stxt
