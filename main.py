from app.controllers.main_controller import MainController
from app.controllers.hello_controller import HelloController

from app.ui.hello_window import HellowWindow
from app.ui.main_window import MainWindow

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    hello_window = HellowWindow()
    
    main_controller = MainController(main_window)
    hello_controller = HelloController(view=hello_window, main_controller=main_controller)
    hello_controller.show()
    
    sys.exit(app.exec())
