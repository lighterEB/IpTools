# IpTools(ip测试工具)
## 说明
### 4ep为项目资源文件可以用eric6打开
### 打包方法:
#### 1.python -m pip install pyinstaller
#### 2.pyinstaller -w -F iptools.py
#### 3.生成exe文件在dist文件夹里
#### 4.将图标文件和exe文件放在同一目录




# 运行截图
![image](https://raw.githubusercontent.com/lighterEB/IpTools/master/img-folder/running.png)

# 已知问题（待解决）
在开启其中一个线程并且还未结束时再开启另一个工作线程之前的线程不会暂停或结束。导致输出显示时会出现混乱的现象。

# 尝试
加入线程开启判定变量，若有线程开启先暂停输出再进行新的工作线程。

