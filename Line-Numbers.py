def main():
    fileName = input('Enter a file name: ')
    lineNum(fileName)

def lineNum(fileName):
    file_handle = open(r'C:\\Users\\mrpot\\OneDrive\\Documents\\For Study\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 7 - Files and Exceptions\\' + fileName, 'r')
    lineCount = 0
    for lines in file_handle:
        lineCount += 1
        print(str(lineCount) + ': ' + lines.rstrip('\n'))
    
    file_handle.close()

main()    