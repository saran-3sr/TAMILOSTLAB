import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

app.setWindowIcon(QIcon('python.ico'))

window = QWidget()
window.setWindowTitle("Hello World")
window.setGeometry(100, 100, 300, 200)

layout = QVBoxLayout()

label = QLabel("Hello World!")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("background-color: #f0f0f0;")

button = QPushButton("Close")
button.clicked.connect(app.quit)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
