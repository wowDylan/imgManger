import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QPushButton
# import PyQt5.QtWidgets
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    # 用于初始化
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        # 设置窗口尺寸
        self.setWindowTitle('主窗口应用')
        self.resize(400, 300)
        # 添加button
        self.button1 = QPushButton('退出')
        # 将信号与槽关联
        self.button1.clicked.connect(self.onclick_button)
        # 设定水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        # 将button放置在mainframe
        mainframe = QWidget()
        mainframe.setLayout(layout)
        # 将mainframe放置在主窗口上
        self.setCentralWidget(mainframe)

    # 相当于是一个槽，用来接受点击传过来的信息
    def onclick_button(self):
        sender = self.sender()
        print(sender.text() + " 按钮被按下")
        app = QApplication.instance()
        app.quit()

    def center(self):
        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口尺寸
        size = self.geometry()
        newWidth = (screen.width() - size.width()) / 2
        newHeight = (screen.height() - size.height()) / 2
        self.move(newWidth, newHeight)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstMainWin()
    main.show()
    main.center()
    sys.exit(app.exec_())
