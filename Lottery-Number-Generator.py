import random
DEGIT = 7
def main():
    elements = lotteryGenerator()
    for element in elements:
        print("The lottery number is:", element)

def lotteryGenerator():
    lottery = []
    for degits in range(DEGIT):
        for number in str(random.randint(0,9)):
            lottery.append(number)
    return(lottery)
main()