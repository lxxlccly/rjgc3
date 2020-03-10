import coverage
import unittest
import os

cov = coverage.coverage(source=["game_map"])
cov.start()
suite = unittest.defaultTestLoader.discover(os.getcwd(), "test_game_map.py")
unittest.TextTestRunner().run(suite)
cov.stop()
cov.report()
#cov.html_report(directory="report_html_01")