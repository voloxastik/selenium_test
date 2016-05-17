import unittest
import os
import sys
import importlib

futures_to_test=['future_1','future_2']

path_to_future=[]
for future in futures_to_test:
    path_to_future.append(os.getcwd()+'/tests/'+future+'/test_suites')

loader=unittest.TestLoader()
suite=unittest.TestSuite()


for future, path in zip(futures_to_test, path_to_future):
    sys.path.append(path)
    importlib.import_module (future+'_default_suite')
    suite.addTest(loader.loadTestsFromName(future+'_default_suite.suite'))
    sys.path.pop()

runner=unittest.TextTestRunner()
runner.run(suite)