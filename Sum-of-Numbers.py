def main():
    fileName = input('Enter a file name: ')
    sumNumber(fileName)

def sumNumber(fileName):
    file_handle = open(r'C:\\Users\\mrpot\\OneDrive\\Documents\\For Study\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 7 - Files and Exceptions\\' + fileName, 'r')
    sum = 0
    for lines in file_handle:
        sum += int(lines)
    
    print('Sum of numbers =', sum)
    file_handle.close()

main()