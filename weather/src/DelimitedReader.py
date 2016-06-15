import csv

"""Reads delimited files"""


class DelimitedReader:
    def __init__(self):
        pass

    def read(self, filename, func):
        with open(filename, 'rb')as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')

            #            lastyear = None
            for row in tsvin:
                func(row)
            #                if row[0]!=lastyear:
            #                    lastyear = row[0]
            #                    print lastyear
            #                else:
            #                    print "hat"
            # ===============================================================
            # func(row)
            # ===============================================================
