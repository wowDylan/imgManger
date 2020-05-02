import sys
import os
import shutil
from windowUi import Ui_MainWindow
from About import Ui_Dialog


from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView, QMessageBox, QDialog
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QTransform, QIcon


# 槽函数，以及槽的绑定，都在这里进行，需要自定义函数。过多的内容，则需要开一个libs，然后在此py文件中导入（参照labelimg）
# 这是主窗口类
class imgManger(QMainWindow, Ui_MainWindow):
    # 自定义信号书写处
    def __init__(self, parent=None):
        super(imgManger, self).__init__(parent)
        self.setupUi(self)
        self.initUI()  # 初始化界面

    def initUI(self):
        # 初始化整个界面的图标
        # 初始化相关参数
        self.namelist_index = 0  # 记录访问第几个图片
        self.namelist_len = 0 # 初始化存储图片名称的列表的长度为0
        self.showimg.setFrameShape(QtWidgets.QFrame.Box)  # 显示Qlabel的边框
        self.showimg.setAlignment(Qt.AlignCenter)  # 图片居中显示,也即设置Qlabel中的内容居中显示
        self.setWindowIcon(QIcon('./icons/app.png'))
        # 为控件设置相应的提示信息
        self.openfolder.setToolTip('打开Logo图像文件夹')
        self.openimg.setToolTip('打开单个Logo图像')
        self.preimgbutton.setToolTip('前一张图片')
        self.nextimgbutton.setToolTip('下一张图片')
        self.markgood.setToolTip('将图片标记为好的Logo')
        self.markbad.setToolTip('将图片标记为没有Logo的图像')
        self.imglist.setToolTip('显示文件夹下的所有Logo图像')
        self.labelname.setToolTip('显示当前的标签')
        self.labellist.setToolTip('显示所有的标签')

        # 各种信号
        self.openfolder.clicked.connect(self.openfolder_click)  # 打开文件夹按钮的连接
        self.openimg.clicked.connect(self.openimg_click)  # 打开图片按钮的连接
        self.nextimgbutton.clicked.connect(self.nextimgbutton_clicked)  # 下一张图片的连接
        self.preimgbutton.clicked.connect(self.preimgbutton_clicked)  # 上一张图片的连接
        self.markgood.clicked.connect(self.markgood_clicked)  # 标记为good图像的连接
        self.markbad.clicked.connect(self.markbad_clicked)  # 标记为bad图像的连接

        self.actionAbout.triggered.connect(self.aboutdialog)
        self.actionHelp.triggered.connect(self.helplink)

    # 在浏览器中打开百度
    def helplink(self):
       import webbrowser
       webbrowser.open('http://www.baidu.com/')

    # 弹出关于对话框
    def aboutdialog(self):
        dialog.show()

    #图片的加载显示事件，打开图片按钮
    def loadimg(self, picture):
        self.img = QtGui.QImage(picture)  # 读取图片
        # 输出图片的大小，名称，所在位置。图片的深度如何获取？有待研究。
        print(self.path.split('/')[-1])  # 输出工作目录
        print(self.namelist[self.namelist_index])  # 输出Logo图像名称
        print(self.path + '/' + self.namelist[self.namelist_index])  # Logo图像的完整路径
        print(self.img.height(), self.img.width(), int(self.depth()/8))
        # 对图片进行缩放
        self.width_prop = self.showimg.width() / self.img.width()  # 宽度的比例
        self.height_prop = self.showimg.height() / self.img.height()  # 高度的比例
        self.prop = min(self.width_prop, self.height_prop)  # 宽度和高度比例的最小值
        #  对于显示在Label标签中的图像的边距的计算：(Label的宽度-图片的宽度)/2;(Label的高度-图片的高度)/2
        self.left_margan = (self.showimg.width() - (self.img.width()*self.width_prop)) / 2  # 计算图片距离Label的左边距
        self.up_margan = (self.showimg.height() - (self.img.height()*self.height_prop)) / 2   # 计算图片距离Label的上边距
        trans = QTransform()  # 实例化QTransform()，QTransform 用于指定坐标系的 2D 转换 - 平移、缩放、扭曲（剪切）、旋转或投影坐标系。绘制图形时，通常会使用。
        trans.scale(self.prop, self.prop)  # 设置图片的缩放比例
        img_result = self.img.transformed(trans)  # 图片缩放
        transpicture = QtGui.QPixmap.fromImage(img_result)  # 将缩放的图片转化为QPixmap格式
        self.showimg.setPixmap(transpicture)  # 在QLabel中显示QPixmap格式的图片
        #鼠标释放事件的连接，获取标注框的坐标
        self.showimg.release_signal.connect(self.print_axis)
        # 鼠标按下事件的连接，获取图像的基本信息
        self.showimg.press_signal.connect(self.print_YOLO_VOC)

    # 输出坐标, 对应鼠标的释放事件
    def print_axis(self, x0, y0, x1, y1):
        # 对标注框相对于图片的位置进行计算
        xmin = (x0 - self.left_margan) / self.prop
        xmax = (x1 - self.left_margan) / self.prop
        ymax = (y0 - self.up_margan) / self.prop
        ymin = (y1 - self.up_margan) / self.prop
        # 对标注框的坐标进行四舍五入
        print(int(xmin+0.5))
        print(int(xmax+0.5))
        print(int(ymin+0.5))
        print(int(ymax+0.5))
        print('--------------------')
        # self.showimg.release_signal.disconnect(self.print_axis)

    # 对应鼠标的按下事件
    def print_YOLO_VOC(self):
        # 输出标注框对应的标签
        print(self.selected_label)

    # openfolder按钮的单击事件
    def openfolder_click(self):
        # 打开文件夹，选取指定类型的图像。
        self.path = QFileDialog.getExistingDirectory(self, "请选取Logo图像文件夹", ".")  # 返回值为文件夹的绝对地址
        self.namelist = []  # 存储所有的图像文件名
        for name in os.listdir(self.path):
            if len(name.split('.jpg')) == 2:
                self.namelist.append(name)
        self.namelist_len = len(self.namelist)  # 获取图像文件的个数
        self.loadimg(self.path + '/' + self.namelist[0])
        # 在控件中显示所有的图片文件名
        listModel = QStringListModel()
        listModel.setStringList(self.namelist)
        self.imglist.setModel(listModel)
        self.imglist.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置双击不可改变
        # 需要自行创建good与bad文件夹，因为shutil.move的目标地址只能是存在的目录
        # 在控件中显示所有的标签名称（标注文件夹下面需要有label.txt）
        label_list_model = QStringListModel()
        self.lines = []  # 开一个list，记录所有的标签信息
        label_txt = self.path + '/' + 'label.txt'
        with open(label_txt, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                self.lines.append(line)
        label_list_model.setStringList(self.lines)
        self.labellist.setModel(label_list_model)
        self.labellist.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置双击不可改变
        # 设置默认显示的label
        self.selected_label = self.lines[0]
        self.labelname.setText(self.selected_label)
        # 发生双击信号连接
        self.labellist.doubleClicked.connect(self.checkItem)

    # label列表的双击事件
    def checkItem(self, index):
        self.selected_label = self.lines[index.row()]  # 获取当前选择的label，在图片加载时，默认选择第一个标签
        self.labelname.setText(self.selected_label)

    # openimg按钮的单击事件
    def openimg_click(self):
        #  获取单个文件的绝对路径
        path = QFileDialog.getOpenFileName(self,"选取单Logo图像", ".", "Img Files (*.bmp *.jpg *.jpeg *.png)")
        self.loadimg(path[0])

    # preimgbutton事件的书写,上一张图片
    def preimgbutton_clicked(self):
        if self.namelist_index < 1:
            # 弹出已经是最后一张图片的错误提示对话框
            QMessageBox.warning(self, "Warning", "已经是第一张图片", QMessageBox.Yes | QMessageBox.No)
            pass
        else:
            self.namelist_index -= 1
            self.loadimg(self.path + '/' + self.namelist[self.namelist_index])

    # 下一张图片
    def nextimgbutton_clicked(self):
        if self.namelist_index+2 > self.namelist_len:
            # 弹出已经是最后一张图片的错误提示对话框
            QMessageBox.warning(self, "Warning", "已经是最后一张图片", QMessageBox.Yes | QMessageBox.No)
            pass
        else:
            # 需要先断开信号与槽的连接，不然会多次输出标注框坐标值
            self.showimg.release_signal.disconnect(self.print_axis)
            self.showimg.press_signal.disconnect(self.print_YOLO_VOC)

            self.namelist_index += 1
            self.loadimg(self.path + '/' + self.namelist[self.namelist_index])

    # 标记为好的图片
    def markgood_clicked(self):
        # 将图片移动到图片目录下面的good文件夹，并在此文件夹下面的good.txt下面进行记录
        movename = self.path + '/' + self.namelist[self.namelist_index]
        targetname = self.path + '/' + 'good/'
        # 将图片路径写入工作工作目录下的good.txt
        filewrite = open(r''+self.path + '/good.txt', 'a')  # 加‘r’ 为了防止字符转义,python内部代码创建字符串才需要考虑转义问题，如果是从外部、客户端接收到的字符串是不需要再转义的。
        filewrite.write(movename)
        filewrite.close()
        # 将图片移动到工作目录下的good目录
        shutil.move(movename, targetname)

    # 标记为坏的图片
    def markbad_clicked(self):
        # 将图片移动到图片目录下面的bad文件夹，并在此文件夹下面的bad.txt下面进行记录
        movename = self.path + '/' + self.namelist[self.namelist_index]
        targetname = self.path + '/' + 'bad/'
        print(targetname)
        # 将图片路径写入工作工作目录下的good.txt
        filewrite = open(r''+self.path + '/bad.txt', 'a')  # 加‘r’ 为了防止字符转义,python内部代码创建字符串才需要考虑转义问题，如果是从外部、客户端接收到的字符串是不需要再转义的。
        filewrite.write(movename)
        filewrite.close()
        # 将图片移动到工作目录下的good目录
        shutil.move(movename, targetname)

class About(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)


# 用于窗口的启动，固定的写法
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = imgManger()  # 初始化主窗口
    window.show()  # 显示主窗口
    # window.setWindowIcon()
    dialog = About()  # 初始化About窗口
    sys.exit(app.exec_())