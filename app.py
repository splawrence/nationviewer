import nation
import pickle

def main():
    partA()
    dashes()

    partB()
    dashes()

    partC()

def partA():
    infile = open("Static/UN.txt","r")
    nationList = [line.rstrip() for line in infile]
    infile.close()

    nationDict = {}
    for line in nationList:
        line = line.split(",")
        nationObj = nation.Nation(line[0],line[1],eval(line[2]),eval(line[3]))
        nationDict[line[0]]=nationObj

    outfile = open ("nationsDict.dat", 'wb')
    pickle.dump(nationDict,outfile)
    outfile.close

def partB():
    nationDict = pickle.load(open("nationsDict.dat",'rb'))
    foundFlag = False

    while not foundFlag:
        country = input("Enter a country: ")
        if country not in nationDict.keys():
            print("not found")
        else:
            print("{:<12}".format("Continent: "),nationDict[country].getContinent())
            print("{:<12}".format("Population: "), "{:,}".format(int(nationDict[country].getPopulation()*1000000)))
            print("{:<12}".format("Area: "), "{:,}".format(nationDict[country].getArea()))
            foundFlag=True

def partC():
    nationDict = pickle.load(open("nationsDict.dat",'rb'))
    foundFlag = False
    nationsList = []
    while not foundFlag:
        inputContinent = input("Enter a continent: ")
        for name,continent in nationDict.items():
            if (nationDict[name].getContinent().upper()==inputContinent.upper()):
                foundFlag = True
                temp =(nationDict[name].getName(),nationDict[name].popDensity())
                nationsList.append(temp)
        nationsList.sort(key=lambda r:r[1], reverse=True)
        nationsList = [x[0] for x in nationsList]
        for nation in nationsList[:5]:
            print ("  ",nation)

def dashes():
    print ("-"*25)

while True:
    main()

class Nation:
    def __init__(self,name, continent, population, area):
        self._name = name
        self._continent = continent
        self._population = population
        self._area = area

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setContinent(self, continent):
        self._continent = continent

    def getContinent(self):
        return self._continent

    def setPopulation(self, population):
        self._population = population

    def getPopulation(self):
        return self._population

    def setArea(self, area):
        self._area = area

    def getArea(self):
        return self._area

    def popDensity(self):
        return (self._population*1000000)/self._area

