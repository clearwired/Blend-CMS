#! /usr/bin/env python
from unittest import main, TestSuite

def test_suite():
    import Zope
    if hasattr(Zope,'startup'):
        Zope.startup()
    suite = TestSuite()
    from test_AcquireUsage import test_suite
    suite.addTest(test_suite())
    from test_Creation import test_suite
    suite.addTest(test_suite())
    from test_PythonScriptUsage import test_suite
    suite.addTest(test_suite())
    from test_ContainedUsage import test_suite
    suite.addTest(test_suite())
    from test_SQLUsage import test_suite
    suite.addTest(test_suite())
    from test_SubclassUsage import test_suite
    suite.addTest(test_suite())
    from test_Unconfigured import test_suite
    suite.addTest(test_suite())
    from test_Broken import test_suite
    suite.addTest(test_suite())
    from test_User import test_suite
    suite.addTest(test_suite())
    return suite
        
if __name__ == '__main__':
    main(defaultTest='test_suite')
