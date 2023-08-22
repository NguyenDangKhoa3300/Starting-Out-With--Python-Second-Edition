def main():
    fileName = input('Enter a file name: ')
    avgNum(fileName)

def avgNum(fileName):
    try:
        file_handle = open(r'C:\\Users\\mrpot\\OneDrive\\Documents\\For Study\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 7 - Files and Exceptions\\' + fileName, 'r')

        count = 0
        sum = 0

        for lines in file_handle:
            count += 1
            sum += int(lines)
        
        avg = sum/count
        print('The average number is:', sum, '/', count, '=', avg)
        file_handle.close()
    
    except ValueError:
        print('File contains string is incorrect')
    
    except IOError:
        print('Cannot read the file or file may not exist')

main()
