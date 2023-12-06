class FCPDCrime(list):
    """
    FCPDCrime: A class for processing Fairfax County Police Department crime reports.

    Author: Adrian Pena
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def load(self, file='CrimeReports.csv'):
        # Loads crime data from a CSV file into the FCPDCrime object
        with open(file, 'r') as f:
            for line in f:
                # Splitting each line into individual string entries and removing '\n'
                data = line.strip().split(',')
                self.append(data)
        return len(self)

    def printCrimes(self, zip='all'):
        # Prints formatted crime reports for a specified zip code or all zip codes
        for crime in self.zipCodeList(zip):
            print(" ".join(crime))

    def zipCodeList(self, zip='22030'):
        # Returns a list of incident reports for a specified Fairfax County zip code
        return [line for line in self if line[-1] == zip]

    def countByZip(self):
        zip_counter = {}
        total_crimes = len(self)

        for line in self:
            zip_counter[line[-1]] = zip_counter.get(line[-1], 0) + 1

        sorted_zips = sorted(zip_counter.items(), reverse=True)

        for zip_code, count in sorted_zips:
            percentage = (count / total_crimes) * 100
            print(f"{zip_code:<10}{count:<5}{percentage:.2f}%")

    def countByCrime(self, select='all'):
        crime_counter = {}
        total_crimes = len(self)

        for line in self:
            if select == 'all' or line[-1] == select:
                crime_counter[line[1]] = crime_counter.get(line[1], 0) + 1

        sorted_crimes = sorted(crime_counter.items(), reverse=True)

        for crime_code, count in sorted_crimes:
            percentage = (count / total_crimes) * 100
            crime_description = next((line[2] for line in self if line[1] == crime_code), '')
            print(f"{crime_code:<12}{count:<5}{percentage:.2f}%{'':>10}{crime_description}")


# Example usage:
FC = FCPDCrime(name='My FCPD Crime Reporting Object')
FC.load(file='CrimeReports.csv')
FC.printCrimes()
ZL = FC.zipCodeList(zip='22030')
for c in ZL:
    print(c)
FC.countByZip()
FC.countByCrime(select='all')
