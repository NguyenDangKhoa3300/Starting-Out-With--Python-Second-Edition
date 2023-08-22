def main():
    print(rainfallStatistics())

def rainfallStatistics():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    count, averageAmount = 0, 0
    rainfall = []
    for month in months:
        userInput = int(input('Enter the rainfall amount of {} : '.format(month)))
        count += userInput
        averageAmount = count/len(months)
        rainfall.append(userInput)
        maximum = max(rainfall)
        minimum = min(rainfall)
    

    return(count, averageAmount, maximum, minimum)

main()