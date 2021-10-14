import sys
from PyQt5.QtWidgets import *
#some colour for your life 

if __name__ == "__main__":

    app = QApplication([])
    w = QWidget()
    w.setWindowTitle("DeskFood.com")

    btn1 = QPushButton("POP's Dining")
    btn2 = QPushButton("Starbucks")
    btn3 = QPushButton("Aramis")
    btn4 = QPushButton("Freshëns Fresh Food Studio")
    btn5 = QPushButton("Campus Center Market")
    btn6 = QPushButton("Burger Studio")
    btn7 = QPushButton("Street Food")
    btn8 = QPushButton("TCP")
    btn9 = QPushButton("Boar's Head")
    btn10 = QPushButton("Book n' Beans Cafe")


    vb = QVBoxLayout(w)

    vb.addWidget(btn1)
    vb.addWidget(btn2)
    vb.addWidget(btn3)
    vb.addWidget(btn4)
    vb.addWidget(btn5)
    vb.addWidget(btn6)
    vb.addWidget(btn7)
    vb.addWidget(btn8)
    vb.addWidget(btn9)
    vb.addWidget(btn10)


    w.show()


    sys.exit(app.exec_())

