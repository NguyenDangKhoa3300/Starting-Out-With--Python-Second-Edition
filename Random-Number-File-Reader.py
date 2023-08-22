def main():
    fileName = input('Enter a file name: ')
    ranNumReader(fileName)

def ranNumReader(fileName):
    file_handle = open(r'C:\\Users\\mrpot\\OneDrive\\Documents\\For Study\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 7 - Files and Exceptions\\' + fileName, 'r')

    sum = 0
    count = 0

    for lines in file_handle:
        sum += int(lines)
        count += 1
    
    print('Total:', sum)
    print('Number of random numbers:', count)

    file_handle.close()

main()
        