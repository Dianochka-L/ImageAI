from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from app.ui.resources_rc import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка файла .ui
        loadUi("app/ui/MainWindow.ui", self) # Первый аргумент - путь к файлу .ui
        
        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
