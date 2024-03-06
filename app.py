import sys
import os
sys.path.append(os.path.join('UIFiles', 'assets'))
sys.path.append('uiUtils')

os.system('pyside6-rcc {} -o {}'.format(os.path.join('UIFiles', 'assets', 'assets.qrc'), os.path.join('UIFiles', 'assets', 'assets_rc.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'main_UI.ui'), os.path.join('UIFiles', 'main_UI.py')))


from PySide6.QtWidgets import QApplication

from appAPI import main_API
from appUI import mainUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_ui = mainUI()
    API = main_API(main_ui)
    main_ui.show()
    app.exec()