# excel_analysis

## 简介
Excel虽然可以非常方便地处理数据，但数据量大时速度就变慢了，本项目把Excel数据分析的常用功能：筛选、多表合并、多表汇总、多表分组，通过Python+Pandas重新实现，因为Pandas处理数据更快且能处理大的数据，此工具还可根据业务需求灵活修改少量代码实现通用。

## 开发环境Python-v3(3.6)
-pandas==0.25.1
-matplotlib==2.2.2
-glob2==0.6
另外还需安装pyqt5

## 用法
下载excel_analysis项目到本地，PyCharm导入项目并配好运行环境以及安装上述依赖包，运行Main.py，出现如下界面：

![image](https://github.com/HuiMengYouXian/excel_analysis/blob/master/image-folder/%E5%88%9D%E5%A7%8B.png)

1.导入要处理的数据文件夹

![image](https://github.com/HuiMengYouXian/excel_analysis/blob/master/image-folder/%E5%AF%BC%E5%85%A5.png)

导入后左侧文件列表出现文件夹里的文件名

![image](https://github.com/HuiMengYouXian/excel_analysis/blob/master/image-folder/%E5%AF%BC%E5%85%A5%E5%90%8E.png)

2.筛选保存：选择要筛选的表，这里筛选的列是代码写好的，可根据业务改变，这里筛选指定列，即指定显示的列，其余列统统丢掉

![image](https://github.com/HuiMengYouXian/excel_analysis/blob/master/image-folder/%E7%AD%9B%E9%80%89%E6%9D%A1%E4%BB%B6.png)

筛选前

![image](https://github.com/HuiMengYouXian/excel_analysis/blob/master/image-folder/%E7%AD%9B%E9%80%89%E5%89%8D.png)

筛选后

![image](https://github.com/HuiMengYouXian/excel_analysis/blob/master/image-folder/%E7%AD%9B%E9%80%89%E5%90%8E.png)





