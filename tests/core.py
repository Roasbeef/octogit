import unittest
import os
import re
import subprocess


class Create_Delete_Test(unittest.TestCase):

    @classmethod
    def setUp(cls):
        '''create temp file for gist creation'''
        with open('test_gist.txt', 'w') as f:
            f.write('Testing create gists')

    @classmethod
    def tearDown(cls):
        '''delete file after tests execute'''
        os.remove('test_gist.txt')

    def test_create_and_delete_gist(self):
        cmd = ['octogit', 'gists', 'create', 'test_gist.txt']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        success_msg = re.match(r'octogit.\sgist:\s(\d+)\screated\ssuccessfully',
                               stdout)

        self.assertTrue(success_msg)
        gist_id = success_msg.group(1)

        cmd = ['octogit', 'gists', 'delete', gist_id]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        success_msg = 'octogit. gist: %s deleted successfully\n' % gist_id

        self.assertEqual(stdout, success_msg)

    def test_invalid_gist_id(self):
        """
        Tests that an invalid or not proprietary
        gist_id raises the correct message
        """
        cmd = ['octogit', 'gists', 'delete', '12']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        expected_error = "octogit. You either passed a gist that isn't yours or you need to login silly.\n"
        self.assertEqual(expected_error, stdout)


if __name__ == "__main__":
    unittest.main()
