
string = "this is is just a  a wonder, wonder why do I have this in mind"

def firstduplicate(String):
    import re
    cleanstr=re.sub("[^a-zA-Z -]","",string)
    print(cleanstr)
    cleanset=set()
    for eachword in cleanstr.lower().split(' '):
        if eachword in cleanset:
            return eachword
        else:
            cleanset.add(eachword)
    return False
print(firstduplicate(string))


