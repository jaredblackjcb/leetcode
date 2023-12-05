class HashmapToolbox:
    # get the key of the max val in a dict
    def getMaxKey(dictA):
        return max(dictA, key=dictA.get)