def main():
    userInput = int(input("Enter a 7 digits number: "))
    for lst_item in chargeAccountValidate():
        if userInput == int(lst_item):
            print('The number is valid')
        else:
            print('The number is invalid')

def chargeAccountValidate():
    file_handler = open('C:\\Users\\mrpot\\OneDrive\\Documents\\Self-Studied Document\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 8 - Lists and Tuples\\charge_accounts.txt', 'r')
    cleaned_lst = []
    for line in file_handler:
        lines = file_handler.readlines()
              
    file_handler.close()
    
    for item in lines:
        cleaned_lst.append(item.strip())
    
    return(cleaned_lst)

main()
    