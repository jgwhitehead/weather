'''
Created on 21 Aug 2015

@author: James
'''
import copy
import csv
import collections

class HottestDay(object):
    yearColIndex = 0
    dayOfMonthColIndex = 1
    janColIndex = 2
    febColIndex = 3
    marColIndex = 4
    aprColIndex = 5
    mayColIndex = 6
    junColIndex = 7
    julColIndex = 8
    augColIndex = 9
    sepColIndex = 10
    octColIndex = 11
    novColIndex = 12
    decColIndex = 13

    years = {}

    '''
        Constructor
        '''

    def __init__(self):
        pass

    def assembleYears(self, filename):
        with open(filename, 'rb')as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')

            lastyear = ""
            years = collections.OrderedDict()
            year = collections.OrderedDict()
            #            lastyear = None
            first = True
            for row in tsvin:
                # for row in....

                if row[0] != lastyear:
                    if (lastyear != ""):
                        years[lastyear] = year

                    # if not first:
                    #                        print lastyear
                    #                        print year['jan']
                    lastyear = row[0]
                    year = collections.OrderedDict()
                    first = False

                year.setdefault("jan", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.janColIndex]
                year.setdefault("feb", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.febColIndex]
                year.setdefault("mar", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.marColIndex]
                year.setdefault("apr", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.aprColIndex]
                year.setdefault("may", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.mayColIndex]
                year.setdefault("jun", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.junColIndex]
                year.setdefault("jul", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.julColIndex]
                year.setdefault("aug", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.augColIndex]
                year.setdefault("sep", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.sepColIndex]
                year.setdefault("oct", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.octColIndex]
                year.setdefault("nov", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.novColIndex]
                year.setdefault("dec", collections.OrderedDict())[row[HottestDay.dayOfMonthColIndex]] = row[HottestDay.decColIndex]

            return years

    def retainHottestDays(self, years):
        strippedYears = copy.deepcopy(years)

        for year in years:
            hottest_temp_so_far = -999999
            hottest_day_count = 0
            for month in years[year]:
                # print month
                for day in years[year][month]:
                    # print day + ':' + years[year][month][day]
                    temp = years[year][month][day]
                    if int(temp) > int(hottest_temp_so_far):
                        hottest_temp_so_far = temp
                        hottest_day_count += 1
            print year + ':', hottest_day_count


                    # read row - save all columns into collection
                    # read next tow - if same year, continue saving
                    # if new year, start new collection and evaluate built up year

                    # outut of script:list day of year which are hottest so far per year
