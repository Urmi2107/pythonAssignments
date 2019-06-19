import re
def regexStrip(strInput, strRemove):
    if strRemove == None:
        return strInput.strip()
    else:
        strInput = strInput.strip()
        stringRegex = re.compile(strRemove)
        return stringRegex.sub('', strInput)


strInput = input('Enter a string:')
strRemove = input('Enter the str you want to remove from the string:')
strInput = regexStrip(strInput, strRemove)
print (strInput)