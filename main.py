import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.layout = QVBoxLayout(self)


        # Create QLineEdit and QLabel pairs individually and set their echo modes
        self.line_edit1 = QLineEdit()
        self.label1 = QLabel()
        self.line_edit1.setEchoMode(QLineEdit.Normal)
        self.line_edit1.textChanged.connect(self.label1.setText)
        self.layout.addWidget(self.line_edit1)
        self.layout.addWidget(self.label1)


        self.line_edit2 = QLineEdit()
        self.label2 = QLabel()
        self.line_edit2.setEchoMode(QLineEdit.NoEcho)
        self.line_edit2.textChanged.connect(self.label2.setText)
        self.layout.addWidget(self.line_edit2)
        self.layout.addWidget(self.label2)


        self.line_edit3 = QLineEdit()
        self.label3 = QLabel()
        self.line_edit3.setEchoMode(QLineEdit.Password)
        self.line_edit3.textChanged.connect(self.label3.setText)
        self.layout.addWidget(self.line_edit3)
        self.layout.addWidget(self.label3)


        self.line_edit4 = QLineEdit()
        self.label4 = QLabel()
        self.line_edit4.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.line_edit4.textChanged.connect(self.label4.setText)
        self.layout.addWidget(self.line_edit4)
        self.layout.addWidget(self.label4)


        self.line_edit5 = QLineEdit()
        self.label5 = QLabel()
        self.line_edit5.setInputMask('9999-99-99')
        self.line_edit5.textChanged.connect(self.label5.setText)
        self.layout.addWidget(self.line_edit5)
        self.layout.addWidget(self.label5)


        self.line_edit6 = QLineEdit()
        self.label6 = QLabel()
        self.line_edit6.setInputMask('000 . 000 . 000 . 000;_')
        self.line_edit6.textChanged.connect(self.label6.setText)
        self.layout.addWidget(self.line_edit6)
        self.layout.addWidget(self.label6)


        self.line_edit7 = QLineEdit()
        self.label7 = QLabel()
        self.line_edit7.setInputMask('HH : HH : HH : HH : HH : HH;_')
        self.line_edit7.textChanged.connect(self.label7.setText)
        self.layout.addWidget(self.line_edit7)
        self.layout.addWidget(self.label7)


        self.line_edit8 = QLineEdit()
        self.label8 = QLabel()
        self.line_edit8.setInputMask('>AAAA-AAAA-AAAA-AAAA-AAAA;#')
        self.line_edit8.textChanged.connect(self.label8.setText)
        self.layout.addWidget(self.line_edit8)
        self.layout.addWidget(self.label8)


        self.line_edit9 = QLineEdit()
        self.label9 = QLabel()
        self.line_edit9.setInputMask('')
        self.line_edit9.textChanged.connect(self.label9.setText)
        self.layout.addWidget(self.line_edit9)
        self.layout.addWidget(self.label9)


        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

