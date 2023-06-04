from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QMainWindow,
    QLineEdit,
    QVBoxLayout,
    QLabel
    )
from PyQt6.QtGui import QPixmap #display images, can use QLabel widget


class MainWindow(QWidget): #configure window details
    def __init__(self):
        super().__init__()

        self.setWindowTitle("python-pkghelp")

        #--CREATE WIDGETS--
        button = QPushButton("press this", clicked=self.button1) # 'connecting a signal to a slot'. Signal is when button pushed. Slot is the function button1
        #button.clicked.connect(self.button1) | ^you can include this line as a keyword when creating button instance intead
        label = QLabel() #create a simple label
        line_edit = QLineEdit() #create a box where you can type
        label.setText('hello') #simple label
        # line_edit.textChanged.connect(label.setText) use setText to tell label what to display, and it comes from the line_edit signal

        #--PLACE WIDGETS--
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)
        self.setLayout(layout)
        
        #--SHOW WINDOW--
        self.show() #we can do show() here instead of outside the class (make sense ig)


    def button1(self):
        print('it works')


if __name__ == "__main__":
    app = QApplication([])
    MainWindow = MainWindow()
    # MainWindow.show() : moved it into the class


    app.exec() #think of PyQt like working with nodes on DavinciResolve or Blender shade editor