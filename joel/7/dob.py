import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DOB Selection")
        self.setGeometry(100, 100, 400, 200)
        self.setWindowIcon(QIcon('python.ico'))

        self.create_menu()
        self.create_label()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_menu(self):
        menu_bar = self.menuBar()

        dob_menu = menu_bar.addMenu("Select DOB")

        jan_action = QAction("January 1, 2000", self)
        jan_action.triggered.connect(lambda: self.display_dob("January 1, 2000"))
        dob_menu.addAction(jan_action)

        feb_action = QAction("February 14, 1995", self)
        feb_action.triggered.connect(lambda: self.display_dob("February 14, 1995"))
        dob_menu.addAction(feb_action)

        mar_action = QAction("March 30, 1988", self)
        mar_action.triggered.connect(lambda: self.display_dob("March 30, 1988"))
        dob_menu.addAction(mar_action)

    def create_label(self):
        self.label = QLabel("No DOB selected")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; color: blue;")

    def display_dob(self, dob):
        self.label.setText(f"Selected DOB: {dob}")


app = QApplication(sys.argv)
app.setWindowIcon(QIcon('python.ico'))
window = MainWindow()
window.show()
sys.exit(app.exec())
