import os
from nose.tools import assert_equal
import stat
import shutil

def permissions_quiz():
    test_file = os.path.join(os.path.expanduser("~"), 
                             "work",
                             "OutbreakDetection",
                             "Obituaries",
                             "obits.txt")
    try:
        assert_equal( os.path.exists(test_file), True)
        print('obits.txt copied correctly.')
    except:
        print('obits.txt NOT copied correctly')
    try:
        mode = oct(stat.S_IMODE(os.stat(test_file).st_mode))
        assert_equal(mode, oct(0o444))
        print("obits.txt mode set correctly")
    except:
        print("obits.txt mode NOT set correctly. The mode was set to %s"%mode)


