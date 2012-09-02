import subprocess
import unittest


class ErrorMessageTest(unittest.TestCase):

    def test_gists_delete(self):
        """
        Tests that a missing gist number results in
        the correct error message
        """
        cmd = ['octogit', 'gists', 'delete']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        expected_error = "octogit. You need to pass a gist number to delete\n"
        self.assertEqual(expected_error, stdout)

    def test_gists_create(self):
        """
        Tests that not passing any files outputs
        the correct error message
        """
        cmd = ['octogit', 'gists', 'create']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        expected_error = "octogit. You need to pass files as well to create a gist\n"
        self.assertEqual(expected_error, stdout)

    def test_invalid_file(self):
        """
        Tests that a non-existant file raises
        promt to pass files
        """
        cmd = ['octogit', 'gists', 'create', 'doesnt_exist.txt']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        expected_error = "octogit. You need to pass files as well to create a gist\n"
        self.assertEqual(expected_error, stdout)




if __name__ == "__main__":
    unittest.main()
