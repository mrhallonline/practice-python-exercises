def myfunc(t='string'):
    newstring=''
    for count, element in enumerate(t):
        if count%2==0:
            newstring += element.lower()
        else:
            newstring += element.upper()
    return newstring