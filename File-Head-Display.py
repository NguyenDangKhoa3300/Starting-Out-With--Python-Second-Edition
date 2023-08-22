def main():
    fileName = input('Enter a file name: ')
    fileHead(fileName)

def fileHead(fileName):
    file_handler = open(r'C:\\Users\\mrpot\\OneDrive\\Documents\\For Study\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 7 - Files and Exceptions\\' + fileName, 'r')

    print('Reading a file.........')

    count = 0

    line = file_handler.readline()
    while file_handler != '' and count < 5:
        print(line.rstrip('\n'))
        line = file_handler.readline()
        count += 1
        
    print('Number of lines:', count)
    file_handler.close()

    print('-----------------\nThe data has been read from the file successfully!')

main()