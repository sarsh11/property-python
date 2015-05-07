"""
def helloWorld(n):
    print "Hello World!\n" * n
n = raw_input("Enter n:")
n = int(n)
helloWorld(n)
"""
import datetime
from datetime import *
import time
import pickle
class propertySale:
    propertyID = 0
    def __init__(self,reserve):
        self.reserve = 0
        self.reserve = reserve
        self.propertyID = propertySale.propertyID + 1
        propertySale.propertyID = self.propertyID
        self.bids = 0
        self.currBid = 0
        self.reserveFlag = False
        self.bidsList = []
        self.DoA = datetime.now()
        oneday = timedelta(days=1)
        self.DoE = self.DoA + oneday*7
    def placeBid(self, amount):
        self.bidsList.append(amount)
        self.bids = self.bids + 1
        if self.currBid < amount:
            self.currBid = amount
            if self.currBid >= self.reserve:
                self.reserveFlag = True;
    def showStats(self):
        print "ID:",self.propertyID
        print "Start of Auction:", self.DoA, "\nEnd of Auction:", self.DoE
        print "\nBid History:",self.bidsList
        if self.reserveFlag == True:
            print "Reserve value reached!"
        else:
            print "Reserve value not reached!"
        print "-----------\n\n"
"""
prop = propertySale(0)
prop2 = propertySale(100)
propertyList = []
propertyList.append(prop)
propertyList.append(prop2)
propertyList[0].placeBid(10)
prop.placeBid(100)
prop2.placeBid(99)
prop.showStats()
prop2.showStats()
"""
propertyList = []
while True:
    print "What do you want to do?"
    print "[1] See available properties","[2] List new property","[3] Bid on existing property"
    print "[4] Remove listing","[5] Exit"
    choice = int(raw_input("Enter your choice:"))
    if choice == 5:
        print "Tata!"
        break
    elif choice == 1:
        """
        with open('property_data.pkl', 'rb') as input:
            property1 = pickle.load(input)
            property1.showStats()
            property2 = pickle.load(input)
        """
        if len(propertyList) > 0:
            print "\n\nListing existing properties--------"
            for prop in propertyList:
                prop.showStats()

        else:
            print "\nNo properties listed!\n"
    elif choice == 2:
        reserve = int(raw_input("Enter reserve value for property:"))
        propertyList.append(propertySale(reserve))
    elif choice == 3:
        selection = int(raw_input("Enter property number:"))
        if selection <= len(propertyList):
            p = propertyList[selection-1]
            bidamount = int(raw_input("Enter bid amount:"))
            p.placeBid(bidamount)
        else:
            print "\nError! No such property!\n"
    elif choice == 4:
        selection = int(raw_input("Enter property number:"))
        if selection <= len(propertyList):
            del propertyList[selection-1]
    elif choice == 6:
        with open('property_data.pkl', 'wb') as output:
            for prop in propertyList:
                pickle.dump(prop, output, pickle.HIGHEST_PROTOCOL)
