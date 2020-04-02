import sys
import imgManger

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建了主窗口
    mainWindow = QMainWindow()
    # 调用imgManger里面的Ui_imgManger()
    ui = imgManger.Ui_imgManger()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())