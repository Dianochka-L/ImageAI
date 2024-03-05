from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from app.ui.resources_rc import *


class HellowWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка файла .ui
        loadUi("app/ui/HelloWindow.ui", self)
        
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    window = HellowWindow()
    window.show()
    sys.exit(app.exec())
