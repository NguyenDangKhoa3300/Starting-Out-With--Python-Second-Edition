def main():
    print(numAnalysis())

def numAnalysis():
    numbers = []
    count, avgNum = 0, 0
    for number in range(20):
        userInput = int(input("Enter the number: "))
        count += userInput
        numbers.append(userInput)
    
    avgNum = count/len(numbers)
    print('Total number:', count, '\nAverage:', avgNum, '\nMax number:', max(numbers), '\nMin number:', min(numbers))

main()