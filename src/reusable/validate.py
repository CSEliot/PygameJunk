def debug(debugBool, info):

    if (debugBool):
        print "\nDEBUG INFO: ", info
        return True
    return False

def cvalidate(vtype, comparator, comparatee=None):
    '''
    # This function takes the wanted type, and the wanted type, both as a string
    # and an option 3rd input. This function is intended for use with raw_input 
    # is used for any type. If the type matches, it will return the string
    # converted to the type, otherwise False. (can be used simply for convert).
    # for strings, the 3rd input MAY be a string to compare to
    # for number types, the 3rd comparatee MAY be a list of range
    # if the 3rd option is used, it will always return a boolean.
    '''

    valid = False
    if vtype == 'str':
        if comparatee is not None:
            if comparator == comparatee:
                return True
            else:
                return False
        elif type(comparator) is str:
            return comparator
        else:
            return False
    elif vtype == 'int':
        # make sure the user gave us an int, if true, change comp. to an int
        if comparator.isdigit():
            try:
                comparator = int(comparator)
                valid = True
            except:
                None
        if comparatee is not None and valid is True:
            rList = comparatee
            if  rList[0] <= comparator <= rList[1]:
                return True
            else:
                return False
        if type(comparator) is int:
            return comparator
        else:
            return False
    elif vtype == 'long':
        # make sure the user gave us an int, if true, change comp. to an int
        if comparator.isdigit():
            valid = True
            comparator = long(comparator)
        if comparatee is not None and valid is True:
            # comparatee is put into rList for readability purposes.
            rList = comparatee
            if  rList[0] <= comparator <= rList[1]:
                return True
            else:
                return False, comparator
        if type(comparator) is long:
            return comparator
        else:
            return False
    elif vtype == 'float':
        # if it can't be turned into a float, it isn't a word. . .
        try:
            temp = float(comparator)
        except ValueError:
            return False
        # and if it can't be turned into an int, then it is a float.
        # and we are looking for a float, so we WANT this to throw an exception
        try:
            comparator = int(comparator)
            return False
        except ValueError:
            valid = True
            comparator = float(comparator)
        if comparatee is not None and valid is True:
            # comparatee is put into rList for readability purposes.
            rList = comparatee
            if  rList[0] <= comparator <= rList[1]:
                return True
            else:
                return False
        if type(comparator) is float:
            return comparator
        else:
            return False
    elif vtype == 'list':
        if type(comparator) is list:
            valid = True
            comparator = list(comparator)
        if comparatee is not None and valid is True:
            if comparator == comparatee:
                return True
            else:
                return False
        elif type(comparator) is list:
            return comparator
        else:
            return False
    elif vtype == 'bool':
        # this only takes a True or False
        if type(comparator) is bool:
            valid = True
            comparator = bool(comparator)
        if comparatee is not None and valid is True:
            if comparator == comparatee:
                return True
            else:
                return False
        elif type(comparator) is bool:
            return comparator
        else:
            return False
    elif comparator == 'Quit...':
        return True
    else:
        raise Exception('Invalid data type given')

def main():

    intg = 1

    DEBUG = False
    test = False
    while test == False:
        usrInput = raw_input('enter an int between 1 and 10: \n')
        test = cvalidate('int', usrInput, [1, 10])
        debug(DEBUG, (type(usrInput), usrInput, type(test), test))

    test = False
    while test == False:
        usrInput = raw_input('enter a float between 1 and 10: \n')

        test = cvalidate('float', usrInput, [1, 10])
        debug(DEBUG, (type(usrInput), usrInput, type(test), test))

    test = False
    while test == False:
        usrInput = raw_input('Testing! str. . .: \n')

        test = cvalidate('str', usrInput)
        debug(DEBUG, (type(usrInput), usrInput, type(test), test))

    test = False
    while test == False:
        usrInput = raw_input('Testing! long. . .: \n')

        test = cvalidate('long', usrInput)
        debug(DEBUG, (type(usrInput), usrInput, type(test), test))



main()


