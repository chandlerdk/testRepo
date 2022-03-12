#Chandler Duke
#Final Program Assignment
#CSC1192H1 - Deherrera
#This program will read data from files that have information about population and area,
#which will then be used to compute density

print('Hello! We are going to be calculating some spooky information')
print('To begin, I will need to know what files we will be using...')

AREA_FILE = input('Please enter the file name for the ghost town area: ')
POPULATION_FILE = input('Please enter the file name for the population: ')
REPORT_FILE = input('Thank you! How would will you like to name the \n'
                            'file where the information will be stored?: ')
def main():
    areaFile = open(AREA_FILE, 'r')
    popFile = open(POPULATION_FILE, 'r')
    denFile = open(REPORT_FILE, 'w')
    popData= extractDataRecord(popFile)
    while len(popData)== 2:
        areaData = extractDataRecord(areaFile)
        Town = popData[0]
        Population = popData[1]
        Area = areaData[1]
        density = 0.0
        if Area >0:
            Density = Population / Area
            denFile.write("%-25s%10.2f\n" % (Town, Density))
            popData = extractDataRecord(popFile)
    popFile.close()
    areaFile.close()
    denFile.close()

def extractDataRecord(inFile):
    line = inFile.readline()
    if line == "" :
        return []
    else :
        parts = line.rsplit(" ", 1)
        parts[1] = int(parts[1])
        return parts
if __name__ == '__main__':
    main()





