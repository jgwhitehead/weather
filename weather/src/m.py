'''
Created on 21 Aug 2015

@author: James
'''
from HottestDay import HottestDay

if __name__ == '__main__':
    hottestDay = HottestDay()
    years = hottestDay.assembleYears("../resources/weather.tsv")
    
    print years
    hottestDay.retainHottestDays(years)
