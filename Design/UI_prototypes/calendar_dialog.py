from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class CalendarWidget(QDialog):
    """A calendar dialog window for selecting the date of loans and PAT tests"""
    def __init__(self):
        super().__init__()
        
