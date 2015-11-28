'''
Created on 21 Aug 2015

@author: James
'''
import csv, copy
class HottestDay(object):
    '''
    classdocs
    '''
    yearColIndex=0;
    dayOfMonthColIndex=1;
    janColIndex=2;
    febColIndex=3;
    marColIndex=4;
    aprColIndex=5;
    mayColIndex=6;
    junColIndex=7;
    julColIndex=8;
    augColIndex=9;
    sepColIndex=10;
    octColIndex=11;
    novColIndex=12;
    decColIndex=13;

    years={}


    def __init__(self):
        '''
        Constructor
        '''
    def assembleYears(self,filename):
        with open(filename,'rb')as tsvin:
            tsvin = csv.reader(tsvin,delimiter='\t')
            
            lastyear="";
            years={}
            year={};
#            lastyear = None
            first=True
            for row in tsvin:
        #for row in....
        
                if row[0]!=lastyear:
                    if(lastyear!=""):
                        years[lastyear]=year
                    
#                    if not first:
#                        print lastyear
#                        print year['jan']
                    lastyear=row[0]
                    year={}
                    first=False
                    
                year.setdefault("jan",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.janColIndex]
                year.setdefault("feb",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.febColIndex]
                year.setdefault("mar",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.marColIndex]
                year.setdefault("apr",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.aprColIndex]
                year.setdefault("may",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.mayColIndex]
                year.setdefault("jun",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.junColIndex]
                year.setdefault("jul",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.julColIndex]
                year.setdefault("aug",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.augColIndex]
                year.setdefault("sep",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.sepColIndex]
                year.setdefault("oct",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.octColIndex]
                year.setdefault("nov",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.novColIndex]
                year.setdefault("dec",{})[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.decColIndex]
                
            return years
    
    
    def retainHottestDays(self,years):
        strippedYears = copy.deepcopy(years)
        
        for year in years:
            hottestTempSoFar=-999999
            print year
            for month in years[year]:
                print month
                for day in years[year][month]:
                    print day
                
            
            #read row - save all columns into collection
            #read next tow - if same year, continue saving
            #if new year, start new collection and evaluate built up year
            
            #outut of script:list day of year which are hottest so far per year 