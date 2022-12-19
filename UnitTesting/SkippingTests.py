

import unittest


class Apptesting(unittest.TestCase):

    @unittest.SkipTest   # It will simply skip without any reason
    def test_Search(self):
        print('This is search test')

    @unittest.skip("Iam skipp bcoz it's not ready")   # Skip by mentioning some reason
    def test_AdvancedSearch(self):
        print('This is advanced search')

    @unittest.skipIf(1==1,"Condition true that's why skipping")      # Skipping based on a condition
    def test_Prepaid(self):
        print('This is Prepaid search')

    def test_Postpaid(self):
        print('This is Postpaid search')


    def test_loginByGmail(self):
        print('This is gmail login')

    def test_loginByTwitter(self):
        print('This is twitter login')


if __name__ == "__main__":
    unittest.main()