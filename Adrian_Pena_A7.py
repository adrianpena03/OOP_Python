# class FCPDCrime(list):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name

#     def countByCrime(self, select='all'):
#         # display a list of reported number for each type of crime, one line per crime , sorted by frequency count.
#         # input parameter select = 'all' or for a specific zip code
#         # output: one line per unique crime code for the selected area ('all' or 'Zip Code')
#         # Return: No return value

#     def countByZip(self):
#         # Displays a report of the number of crimes reported by the zip code in sorted format from highest to lowest
#         # output: displays one line per county zip code with the count and the % of total crimes
#         # return: no return value

#     def load(self, file='CrimeReports-0423.csv'):
#         # open the file in the parameter, read its contents, split each line into a separate data item strings, remove control characters.
#         # output: no display output is produced
#         # returns: number of lines read

#     def printCrimes(self, zip='all'):
#         # Display a formatted report of all lines in the downloaded report or lines for a selected zip code "zip = '22030'.
#         # Input: 'Zip' parameter - 5 digit zip code in string format or 'all' to print for all county zip codes
#         # output: crime reports, one line per incident
#         # returns: nothing is returned

#     def zipCodeList(self, zip='22030'):
#         # return a list of all incident report lines for a selected fairfax county zipcode.
#         # input: 5 digit zip code in string format, default is '22030'.
#         # output: no display output is produced

class FCPDCrime(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def countByCrime(self, select='all'):
        crimes = [line[2] for line in self if select == 'all' or line[7] == select]
        crime_counts = self._count_items(crimes)
        sorted_crimes = self._sort_items(crime_counts)

        for crime, count in sorted_crimes:
            print(f"{crime}: {count}")

    def countByZip(self):
        zip_counts = self._count_items([line[8] for line in self])
        total_crimes = len(self)

        sorted_zips = self._sort_items(zip_counts)

        for zip_code, count in sorted_zips:
            percentage = (count / total_crimes) * 100
            print(f"{zip_code}: {count} ({percentage:.2f}%)")

    def load(self, file='CrimeReports.csv'):
        with open(file, 'r') as file_handle:
            for line in file_handle:
                # Split each line into individual string entries
                line = line.strip().split(',')
                # Append the line to the FCPDCrime object
                self.append(line)
        
        return len(self)

    def printCrimes(self, zip='all'):
        for line in self:
            if zip == 'all' or line[8] == zip:
                print(','.join(line))

    def zipCodeList(self, zip='22030'):
        return [line for line in self if line[8] == zip]

    def _count_items(self, items):
        counts = {}
        for item in items:
            counts[item] = counts.get(item, 0) + 1
        return counts

    def _sort_items(self, counts):
        return sorted(counts.items(), key=lambda x: x[1], reverse=True)


# Example usage:
FC = FCPDCrime(name='My FCPD Crime Reporting Object')
FC.load(file='<fully_qualified_file_name>')
FC.printCrimes()
ZL = FC.zipCodeList(zip='22030')
for c in ZL:
    print(c)
FC.countByZip()
FC.countByCrime(select='all')
