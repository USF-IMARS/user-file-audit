#!/usr/bin/env python
"""
tests file watch summarizer using fake testdata
"""

import unittest
import os
import subprocess

# dependencies:
from auditparser import filewatch_summary

class Test_on_fake_data(unittest.TestCase):

    # tests:
    #########################
    def test_ty_ls_str(self):
        """
        test summarization of tylar-ls test data
        """
        with open(os.path.join('testdata','tylar-ls.txt'), 'r') as myfile:
            data = myfile.read().replace('\n', '')
            summary = filewatch_summary.summarize_ausearch_string(data)

        self.assertEqual(summary, {'7yl4r': 41, 'testUser': 1, 'tylar': 6})
        #
        # self.assertEqual(params['test1'], 'apple')
        # self.assertEqual(params['test2'], 'bin')

#     def test_ty_ls_main(self):
#         """
#         test summarization using filewatch_summary as command
#         """
#         bashCommand = "grep "" testdata/tylar-ls.txt | auditparser/filewatch_summary.py
# {'7yl4r': 41, 'testUser': 1, 'tylar': 6}"
#         process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#         output, error = process.communicate()
