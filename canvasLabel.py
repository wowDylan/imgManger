from PyQt5.QtCore import QRect, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QLabel


class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    # 自定义信号
    release_signal = pyqtSignal(int, int, int, int)
    press_signal = pyqtSignal()

    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        # 发送鼠标的按下事件，鼠标按下，进行图片信息的写入
        self.press_signal.emit()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        # 发送鼠标释放事件的信号，将矩形的两个对角坐标传送到主页面
        self.release_signal.emit(self.x0, self.y0, self.x1, self.y1)

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)  # 这一点非常重要，调用父类的paintEvent为了显示'背景'!
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(rect)


