def main():
    print(populationCalc())

def populationCalc():
    file_path = 'C:\\Users\\mrpot\\OneDrive\\Documents\\Self-Studied Document\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 8 - Lists and Tuples\\USPopulation.txt'
    cleaned_file1 = []
    sum, count = 0, 0
    with open(file_path, 'r') as file1:
        for item in file1:
            cleaned_file1.append(int(item.strip()))
    
    for item in cleaned_file1:
        sum += item
        count += 1
    
    avg =  sum/count
    maximum = max(cleaned_file1)
    minimum = min(cleaned_file1)

    return(avg, maximum, minimum)
main()