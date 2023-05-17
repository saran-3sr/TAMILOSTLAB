import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

app.setWindowIcon(QIcon('python.ico'))

label = QLabel("Hello World!")
label.setGeometry(100, 100, 300, 200)

# Add padding to the label
label.setContentsMargins(20, 20, 20, 20)

# Set font properties
font = QFont()
font.setPointSize(16)
label.setFont(font)

label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("background-color: #f0f0f0;")

label.show()

sys.exit(app.exec_())
