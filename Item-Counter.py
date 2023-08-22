def main():
    fileName = input('Enter a file name: ')
    itemCounter(fileName)

def itemCounter(fileName):
    file_handle = open(r'C:\\Users\\mrpot\\OneDrive\\Documents\\For Study\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 7 - Files and Exceptions\\' + fileName, 'r')
    count = 0
    for lines in file_handle:
        count += 1
    
    print('Total name in a file =', count)

main()