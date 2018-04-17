# -*- coding: utf-8 -*-

import sys
import os
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from NewWin import Ui_MainWindow



class IpTools(QMainWindow,  Ui_MainWindow):
    def __init__(self):
        super(IpTools,  self).__init__()
        self.setupUi(self)
        self.pb = self.ping_button
        self.tlb = self.telnet_button
        self.tcb = self.tracert_button
        self.ipdb = self.ipaddress_button
        self.pb.clicked.connect(self.PingClicked)
        self.tlb.clicked.connect(self.TelnetClicked)
        self.tcb.clicked.connect(self.TracertClicked)
        self.ipdb.clicked.connect(self.IPAddressClicked)


    def ResetText(self):
        """初始化文本浏览器"""
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.textBrowser.setFontFamily("宋体")
        self.textBrowser.setFontPointSize(12)
        self.textBrowser.setText(data)
        self.textBrowser.append('正在测试...')
    
    def PingClicked(self):
        """触发Ping测试按钮"""
        global getip
        getip = self.ip.text()
        self.ResetText()
        self.thread1 = Ping_()
        self.thread1.start()
        self.thread1._signal.connect(self.UpdateBrowser)
    
    def TelnetClicked(self):
        """触发telnet测试按钮"""
        Ping_().exit()
        Tracert_().exit()
        global getip, getport
        self.ResetText()
        getip = self.ip.text()
        getport = self.port.text()
        self.thread2 = Telnet_()
        self.thread2.start()
        self.thread2._signal.connect(self.Info)
       
        

    def TracertClicked(self):
        """触发tracert测试按钮"""
        global getip
        self.ResetText()
        getip = self.ip.text()
        self.thread3 = Tracert_()
        self.thread3.start()
        self.thread3._signal.connect(self.UpdateBrowser)
        
        
    
    def IPAddressClicked(self):
        """查询地址按钮触发"""
        global getip
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.textBrowser.setFontFamily("宋体")
        self.textBrowser.setFontPointSize(12)
        self.textBrowser.setText(data)
        self.textBrowser.append('正在查询...')
        QApplication.processEvents
        getip = self.ip.text()
        self.thread4 = IpAddr_()
        self.thread4.start()
        self.thread4._signal.connect(self.Info)
    
    def Info(self, msg):
        if msg == 'e':
            QMessageBox.warning(self, "错误", "请检查输入是否正确",  QMessageBox.Yes)
        elif msg == 'f':
            QMessageBox.warning(self, "错误", "请检查网络是否正常",  QMessageBox.Yes)
        elif msg == 'w':
            w = '输入有误，请检查！'
            QMessageBox.warning(self, "错误", w,  QMessageBox.Yes)
        elif msg == 'wa':
            wa = '端口号必须是0-65535，请检查！'
            QMessageBox.warning(self, "错误", wa,  QMessageBox.Yes)
        else:
            self.textBrowser.append(msg)

    def UpdateBrowser(self, msg):
        """将子线程的信息回传"""
        self.textBrowser.append(msg)

class Ping_(QThread):
    """ping测试的子线程"""
    _signal = pyqtSignal(str)
    def __init__(self,  parent=None):
        super(Ping_,  self).__init__()
    
    def __del__(self):
        self.wait()
    
    def run(self):
        global getip, getport
        item = 'ping -w 1000 -n 10 ' + getip + '\t'
        res = os.popen(item)
        try:
            #p = "ping www.baidu.com"
            for line in res:
                self._signal.emit(line)
        except:
            pass

class Telnet_(QThread):
    """telnet测试的子线程"""
    _signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Telnet_, self).__init__(parent)
        
    def __del__(self):
        self.wait()
    
    def run(self):
        global getip, getport
        import socket
        s = socket.socket()
        socket.setdefaulttimeout(5)
        try:
            s.connect((getip, int(getport)))
            y = 'IP:{} 端口：{} 连接正常'.format(getip, getport)
            self._signal.emit(y) 
        except socket.error:
            n = 'IP:{} 端口：{} 连接失败'.format(getip, getport)
            self._signal.emit(n) 
        except ValueError as w:
            self._signal.emit('w')
        except OverflowError as wa:
            self._signal.emit('wa')

        s.close()

class Tracert_(QThread):
    """tracert测试的子线程"""
    _signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Tracert_, self).__init__(parent)
        
    def __del__(self):
        self.wait()
        
    def run(self):
        global getip
        item = 'tracert -w 10 -h 30 -d '+ getip
        line = os.popen(item)
        try:
            for res in line:
                self._signal.emit(res)
        except:
            pass
            
class IpAddr_(QThread):
    """tracert测试的子线程"""
    _signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(IpAddr_, self).__init__(parent)
        
    def __del__(self):
        self.wait()
        
    def run(self):
        import requests
        import socket
        from bs4 import BeautifulSoup
        global getip

        l = []
        try:
            response = requests.get("http://www.ip138.com/ips1388.asp?ip=%s&action=2"%(getip))
            r = response.content.decode('gbk')
            soup = BeautifulSoup(r, 'lxml')
            result = soup.find_all('li')
            for addr in result:
                adlist = addr.get_text().split('：')
                l.append([adlist[1]])
            self._signal.emit('查询地址一： ' + ''.join(l[0]) )
            self._signal.emit('查询地址一： ' + ''.join(l[1]) )
            self._signal.emit('查询地址一： ' + ''.join(l[2]) )
        except:
            s = socket.socket()
            try:
                s.connect(('www.baidu.com',80))
            except socket.error:
                    self._signal.emit('f')
                    s.close()
            else:
                self._signal.emit('e')



if __name__ == '__main__':
    app =QApplication(sys.argv)
    Run = IpTools()
    Run.show()
    sys.exit(app.exec_())
