import unittest
import travis_API as ta

class UnitTest(unittest.TestCase):
    """
    Will run unittests for functions
    """

    ########################################
    #Testing the functions in travis-API.py#
    ########################################

    def test_get_build_repo_status(self):
        """
        Tests the get_build_repo_status function
        """
        result = ta.get_build_repo_status("Matt-Gleich/Get-Temperature")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
