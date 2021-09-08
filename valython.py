import re

#--------------- Matching ----------------------------------

def isString(*arg):
    if len(arg) > 1:
        l = str(arg[1])
        return bool(re.fullmatch(r'[a-zA-Z]{'+l+'}$', arg[0]))
    else:
        return bool(re.fullmatch(r'[a-zA-Z]+$', arg[0]))

def isDigits(*arg):
    if len(arg) > 1:
        l = str(arg[1])
        return bool(re.fullmatch(r'[0-9]{'+l+'}$', arg[0]))
    else:
        return bool(re.fullmatch(r'[0-9]+$', arg[0]))

def isPassword(*arg):
    if len(arg) > 1:
        l = str(arg[1])
        return bool(re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{'+l+',}$', str(arg[0])))
    else:
        return bool(re.fullmatch(r'[A-Za-z0-9@#$%^&+=]+$', str(arg[0])))

def isSymbol(*arg):
    if len(arg) > 1:
        l = str(arg[1])
        return bool(re.fullmatch(r'[@#$%^&+=]{'+l+',}$', str(arg[0])))
    else:
        return bool(re.fullmatch(r'[@#$%^&+=]+$', str(arg[0])))

def isUrl(*arg):
        return bool(re.fullmatch(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', arg[0]))
    

#-------------- Search --------------------

def isEmail(email):
    return bool(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(email)))

def isAnyDigit(inputString):
    return bool(re.search(r'\d', inputString))

def isAnyString(inputString):
    return bool(re.search(r'[A-Za-z]', inputString))

def isAnySpace(inputString):
    return bool(re.search(r' +', inputString))

def isAnySymbol(symbol):
    return bool(re.search(r'[@#$%^&+=]', str(symbol)))