from PyQt4.QtGui import *

from C3_Media_DBMS import *
import sys

class RadioButtonWidget(QDialog):
    """this class creates a group of radio buttond from a given list of labels"""

    #construcor
    def __init__(self,label,instruction,button_list):
        super().__init__()
        self.selected = True
        #create widgets
        self.title_lable = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()

        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set the default checked item
        self.radio_button_list[0].setChecked(True)

        #create layout for radio buttons and add them
        self.radio_button_layout = QVBoxLayout()

        #add buttons to the layout group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter +=1

        #add radio buttons to the group box
        self.radio_group_box.setLayout(self.radio_button_layout)


        #create buttons
        self.cancel_button = QPushButton("Cancel")
        self.select_button = QPushButton("Select")
        self.cancel_button.setAutoDefault(False)
        self.select_button.setAutoDefault(True)

        self.buttons_layout = QHBoxLayout()
        self.buttons_widget = QWidget()
        self.buttons_layout.addWidget(self.cancel_button)
        self.buttons_layout.addWidget(self.select_button)
        self.buttons_widget.setLayout(self.buttons_layout)

        #create a layout for whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_lable)
        self.main_layout.addWidget(self.radio_group_box)
        self.main_layout.addWidget(self.buttons_widget)

        #set the layout for this widget
        self.setLayout(self.main_layout)

        #connections
        self.cancel_button.clicked.connect(self.close)
        self.select_button.clicked.connect(self.close)
        self.cancel_button.setShortcut("Ctrl+W")

##    def get_button_clicked(self):
##        if self.select_button.clicked:
##            return True
##        elif self.cancel_button.clicked:
##            return False


    #method to find out the selected button
    def selected_button(self):
        return self.radio_button_group.checkedId()

def main_menu_main():
    application = QApplication(sys.argv)
    window = RadioButtonWidget()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main_menu_main()
