def main():
    userInput = input('Enter a team name: ')
    print(worldChamsCalc(userInput))

def worldChamsCalc(teamName):
    count = 0
    year_range = []
    cleaned_team = []
    for year in range(1903, 1995):
        if year != 1904 and year != 1994:
            year_range.append(year)
    file_path = 'C:\\Users\\mrpot\\OneDrive\\Documents\\Self-Studied Document\\CODE BOOKS\\[Exercises] STARTING OUT WITH ® Python Second Edition\\Chapter 8 - Lists and Tuples\\WorldSeriesWinners.txt'
    with open(file_path, 'r') as file1:
        for item in file1:
            cleaned_team.append(item.strip())
    
    for item1, item2 in zip(year_range, cleaned_team):
        print(item1, ':', item2) 
    
    for teamNames in cleaned_team:
        if teamName == teamNames:
            count += 1
    
    print('---------------------------\nThat team has won', count, 'times')
main()