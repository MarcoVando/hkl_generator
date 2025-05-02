import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple GUI")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        label0 = QLabel("Lambda")
        self.lam = QLineEdit()

        label1 = QLabel("Space Group:")
        self.sg = QLineEdit()

        label2 = QLabel("a:")
        self.uca = QLineEdit()

        label3 = QLabel("b:")
        self.ucb = QLineEdit()

        label4 = QLabel("c:")
        self.ucc = QLineEdit()

        label5 = QLabel("alpha:")
        self.ucal = QLineEdit()

        label6 = QLabel("beta:")
        self.ucbe = QLineEdit()

        label7 = QLabel("gamma:")
        self.ucga = QLineEdit()

        confirm_button = QPushButton("Confirm")
        confirm_button.clicked.connect(self.confirm_values)

        layout.addWidget(label0)
        layout.addWidget(self.lam)
        layout.addWidget(label1)
        layout.addWidget(self.sg)
        layout.addWidget(label2)
        layout.addWidget(self.uca)
        layout.addWidget(label3)
        layout.addWidget(self.ucb)
        layout.addWidget(label4)
        layout.addWidget(self.ucc)
        layout.addWidget(label5)
        layout.addWidget(self.ucal)
        layout.addWidget(label6)
        layout.addWidget(self.ucbe)
        layout.addWidget(label7)
        layout.addWidget(self.ucga)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

    def confirm_values(self):
        """
        This function retrieves the values from four different fields and prints the confirmed values.
        """
        value0 = self.lam.text()
        value1 = self.sg.text()
        value2 = self.uca.text()
        value3 = self.ucb.text()
        value4 = self.ucc.text()
        value5 = self.ucal.text()
        value6 = self.ucbe.text()
        value7 = self.ucga.text()

        print("Confirmed values:")
        print("Lambda:", value0)
        print("SG:", value1)
        print("a axis:", value2)
        print("b axis:", value3)
        print("c axis:", value4)
        print("alpha angle:", value5)
        print("beta angle:", value6)
        print("gamma angle:", value7)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())