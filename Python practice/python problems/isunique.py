#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures?

import unittest

def isunique(string):
    calc={}
    ans=True
    for each in string:
        if calc.get(each) is None:
            calc[each]=1
        else:
            calc[each]=calc.get(each)+1
    for each in calc.values():
        if each>1:
            ans=False
    return ans


def isunique_another(input_string):
    hash_table=[False]*128

    for eachchar in input_string:
        index=ord(eachchar)
        if hash_table[index]:
            return False
        hash_table[index]=True
    return  True




class Test(unittest.TestCase):
    def test_isunique(self):
        dataT = [('abcd'), ('s4fad'), ('')]
        dataF = [('23ds2'), ('hb 627jh=j ()')]
        for test_string in dataT:
            actual=isunique_another(test_string)
            self.assertTrue(actual)

        for test_string in dataF:
            actual=isunique(test_string)
            self.assertFalse(actual)

if __name__=="__main__":
    unittest.main()


