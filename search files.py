import re,os
def searchFiles(content,expStr):
    if expStr.search(content) is None:
        print("No matches was found.")
    else:
        print(expStr.findall(content))
      
foldername = 'C:/Users/uhalder/Documents/New folder'
windowTextPaths = []
openTextPath = []
readTextPath = []
openPath = []
readPath = []
for i in os.listdir(foldername):
    if i.endswith('.txt'):
        windowTextPaths.append(os.path.join(foldername, i))
searchStr = input("Enter the string:")
expStr = re.compile(searchStr)
for i in range(len(windowTextPaths)):
    openTextPath = open(windowTextPaths[i])
    openPath.append(openTextPath)
for i in range(len(openPath)):
        readTextPath = openPath[i].read()
        readPath.append(readTextPath)
        #openPath[i].close()
for i in readPath:  
      searchFiles(i,expStr)
      