#coding=utf-8
import re
import copy
import time
import codecs
import sys

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，．！【】（）、。：；’‘……￥·"""
#功能模块部分
def CheckFrequency(file, check_list):
  check_result  = {}

  #解决换行问题
  lines=file.readlines()
  txt = ''
  for line in lines:
    txt += line.strip()  # strip()是去掉每行末尾的换行符\n

  #解决中文标点问题
  dicts = {i: ' ' for i in punctuation}
  punc_table = str.maketrans(dicts)
  new_txt = txt.translate(punc_table)
  sentences = new_txt.split()

  #对每个句子查询
  IsPast80 = 0
  for i in sentences:
    if i !='第八十一回':
      for j in check_list:
        if j in i:
          check_result.setdefault(j,[0,0])
          check_result[j][IsPast80]+=1
    else:
      IsPast80 = 1

  #返回字典
  return check_result

########################################################################################
#matplotlib部分
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
def showChart(res):     #res为文本分析结果，以字典形式传入
    #表格数据以列表形式传入
    xs=[]
    ys1=[]
    ys2=[]
    if res:
        for i in res:
            xs.append(i)
            ys1.append(res[i][0])
            ys2.append(res[i][1])

        #设置柱状图
        width = 0.35
        plt.bar(xs, # 横坐标
                ys1, # 柱⾼
                width, # 线宽
                yerr=4, # 误差条
                label='前80回')#标签
        plt.bar(xs, ys2, width, yerr=2, bottom=ys1,label='后40回')

        #其他的说明
        plt.ylabel('出现频次')
        plt.xlabel('单词')
        plt.title('单词词频分析')
        plt.legend()
        plt.show()
    else:
        print('查询结果为空')


#########################################################################################################
# -*- coding: utf-8 -*-
#gui部分
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextAnalyze(object):
    def setupUi(self, TextAnalyze):
        TextAnalyze.setObjectName("TextAnalyze")
        TextAnalyze.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TextAnalyze)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(120, 170, 93, 28))
        self.checkBox_1.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 240, 93, 28))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(120, 310, 93, 28))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(270, 170, 93, 28))
        self.checkBox_4.setObjectName("checkBox_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(270, 240, 93, 28))
        self.checkBox_5.setObjectName("checkBox_6")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(270, 310, 93, 28))
        self.checkBox_6.setObjectName("checkBox_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(430, 170, 93, 28))
        self.checkBox_7.setObjectName("checkBox_9")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(240, 460, 101, 51))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 70, 171, 61))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 390, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 390, 151, 21))
        self.label_2.setObjectName("label_2")
        TextAnalyze.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TextAnalyze)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        TextAnalyze.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TextAnalyze)
        self.statusbar.setObjectName("statusbar")
        TextAnalyze.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(TextAnalyze)
        #self.commandLinkButton.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(TextAnalyze)

        self.commandLinkButton.clicked.connect(self.Query)

    def retranslateUi(self, TextAnalyze):
        _translate = QtCore.QCoreApplication.translate
        TextAnalyze.setWindowTitle(_translate("TextAnalyze", "GUI实现"))
        self.checkBox_1.setText(_translate("TextAnalyze", "之"))
        self.checkBox_2.setText(_translate("TextAnalyze", "笑"))
        self.checkBox_3.setText(_translate("TextAnalyze", "乎"))
        self.checkBox_4.setText(_translate("TextAnalyze", "然"))
        self.checkBox_5.setText(_translate("TextAnalyze", "工夫"))
        self.checkBox_6.setText(_translate("TextAnalyze", "淚"))
        self.checkBox_7.setText(_translate("TextAnalyze", "悔"))
        self.commandLinkButton.setText(_translate("TextAnalyze", "查询"))
        self.label.setText(_translate("TextAnalyze", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">红楼梦文本分析</span></p></body></html>"))
        self.label_2.setText(_translate("TextAnalyze", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">手动输入查询单词</span></p></body></html>"))
        self.menu.setTitle(_translate("TextAnalyze", "红楼梦文本分析"))
        self.menuhelp.setTitle(_translate("TextAnalyze", "help"))
    def Query(self):
        checkList=[]
        for pipe in range(1,8):
            m = getattr(self, "checkBox_%d"%pipe)
            if m.isChecked():
                checkList.append(m.text())
        if self.lineEdit.text()!='':
            checkList.append(self.lineEdit.text())
        if checkList:
            Word_Query(checkList)
            if  self.lineEdit.text()!='':
                checkList.remove(self.lineEdit.text())
                self.lineEdit.clear()
        return


##################################################################################################
#单词查询
def Word_Query(check_list):
    file = open('dreamofredmaison.txt', 'r', encoding='UTF-8')
    # 开始分析
    st = time.time()
    res = CheckFrequency(file, check_list)
    print(res)
    ed = time.time()
    print(ed - st)
    showChart(res)
    # 写入文件
    if res:
        with codecs.open('output.txt', 'w', 'utf-8') as fp:
            fp.write('单词  前80回出现次数  后40回出现次数')
            for i in res:
                line = '\n' + i + '       ' + str(res[i][0]) + '                  ' + str(res[i][1])
            fp.write(line)

###########################################################################################################
#主函数为gui部分
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = QtWidgets.QMainWindow()
    ui = Ui_TextAnalyze()
    ui.setupUi(MyWindow)
    MyWindow.show()
    sys.exit(app.exec_())

