def main():
    userAnswer = []
    value = ''
    print('Please enter a number for your answer: \n1 = A | 2 = B | 3 = C | 4 = D')

    for answer in range(1, 21):
        userInput = int(input("Enter your answer of question {}: ".format(answer)))
        if userInput == 1:
            value = 'A'
        elif userInput == 2:
            value = 'B'
        elif userInput == 3:
            value = 'C'
        elif userInput == 4:
            value = 'D'
        else:
            print('Please only enter number from 1 to 4!')
            break

    userAnswer.append(value)
    print(examChecker(userAnswer))

def examChecker(answerList):
    correct, wrong = 0, 0
    
    testAnswer = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    
    
    for index in range(20):
        if answerList[index] == testAnswer[index]:
            correct += 1
        else:
            wrong += 1
    
    if correct >= 15:
        print('You have passed the exam')
    else:
        print('Try again!')

    print('The number of correct answer is:', correct, '\nThe number of wrong answer is:', wrong, '\nYour answer is:', answerList)

main()