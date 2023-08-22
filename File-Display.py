def main():
    fileWrite()

    fileRead()

def fileWrite():
    file_handle = open('numbers.txt', 'w')
    userInput = int(input('How many number do you want to write to a file: '))
    for i in range (0, userInput):
        file_handle.write(str(i) + '\n')
    
    file_handle.close()
    print('The data has been written to the file successfully!\n-----------------')

def fileRead():
    file_handle = open('numbers.txt', 'r')
    
    print('***READING FILES***')
    for lines in file_handle:
        num = int(lines)
        print(num)
    
    file_handle.close()
    print('-----------------\nThe data has been read from the file successfully!')

main()