def main():
    userInput = input('Enter a name: ')
    print(nameSearch(userInput))

def nameSearch(userInput):
    girls, boys = [], []
    file1_path = 'C:\\Users\\mrpot\\OneDrive\\Documents\\Self-Studied Document\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 8 - Lists and Tuples\\GirlNames.txt'
    file2_path = 'C:\\Users\\mrpot\\OneDrive\\Documents\\Self-Studied Document\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 8 - Lists and Tuples\\BoyNames.txt'
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.readlines()
        cleaned_content1 = [line.strip() for line in content1]
    
        content2 = file2.readlines()
        cleaned_content2 = [line.strip() for line in content2]
    
    if userInput in cleaned_content1 or userInput in cleaned_content2:
        print('Your name is popular')
    else:
        print('Your name is not popular')
        
main()

