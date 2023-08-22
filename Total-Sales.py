def main():
    sales_list = []
    for day in range(1,8):
        userInput = input("Enter a sale for day {}: ".format(day))
        sales_list.append(userInput)
    
    print("Total sales of a week is:",totalSalesCalc(sales_list))

def totalSalesCalc(lst):
    count = 0
    for sale in lst:
        count += int(sale)
    
    return count

main()