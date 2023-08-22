import random

def main():
    userInput = int(input('How many times do you want to generate random numbers: '))
    randomNum(userInput)

def randomNum(userInput):
    file_handle = open('random_numbers.txt', 'w')
    for i in range(0, userInput):
        ranNum = random.randint(1, 100)
        file_handle.write(str(ranNum) + '\n')
    
    print('Random number has written successfully to the file')
    file_handle.close()

main()
