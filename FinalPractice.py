class MovieDict (dict):
    validCats = ('comedy', 'drama', 'scifi', 'historical')
    def addLine (self, line):
            x = line.split(',')
            x[0] = x[0].strip()
            x[1] = x[1].strip()
            x[2] = x[2].strip()
            if x[2] in MovieDict.validCats:
                    self [int(x[0] ) ] = x[1:]
                    return True
            return False