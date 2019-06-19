import re
def replaceWords(words):
    resultFile = open('C:\\Users\\uhalder\\Documents\\Devops training\\python\\19-06-2019\\output.txt', 'w')
    resultString = ''
    for word in words:
        if adjRegex.match(word):
             word = adjRegex.sub(input("Give an adjective: "), word)
        elif nounRegex.match(word):
            word = nounRegex.sub(input("Give a noun: "), word)
        elif verbRegex.match(word):
            word = verbRegex.sub(input("Give a verb: "), word)
        elif advRegex.match(word):
            word = advRegex.sub(input("Give a adverb: "), word)
        resultString += word + ' '
        resultFile.write(word + ' ')
    print(resultString)
    resultFile.close()

fileInput = open('C:\\Users\\uhalder\\Documents\\Devops training\\python\\19-06-2019\\input.txt', 'r')
content = fileInput.read()
words = list(content.split())
fileInput.close()
adjRegex = re.compile(r'ADJECTIVE')
nounRegex = re.compile(r'NOUN')
advRegex = re.compile(r'ADVERB')
verbRegex = re.compile(r'VERB')
replaceWords(words)