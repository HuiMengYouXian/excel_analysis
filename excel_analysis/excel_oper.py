import os
import pandas as pd
import glob
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pd_set import pd_set


root = None  # 根路径，即文件夹路径
file_path = None  # 点击左侧文件路径名
file_list = None  # 文件名列表
temp_root = None  # 另存到外部路径
qModelIndex = None  # 点击左侧文件索引


# 导入文件并把文件名显示在左侧列表
def input_file(listView, MainWindow):
    print("导入文件")
    global file_path
    global root
    global file_list
    file_list = []  # 文件名列表

    root = QFileDialog.getExistingDirectory(MainWindow, "选择文件夹", "F:/PycharmProjects/ExcelAnalysis/")
    # print(root)  root文件夹路径名
    """
    遍历文件夹文件
    os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。是一个简单易用的文件、目录遍历器
    返回的是一个三元组(root,dirs,files)：root:当前正在遍历的这个文件夹的本身的地址  dirs:该文件夹中所有的目录的名字(不包括子目录)  files:内容是该文件夹中所有的文件(不包括子目录)
    """
    for dir_path, dir_name, file_names in os.walk(root):
        for file_path in file_names:  # 遍历所有文件名
            # print(file_path)   # 1月销售数据.xls
            file_list.append(os.path.join(file_path))  # os.path.join(path1[,path2])把目录和文件名合成一个路径

    # 实例化列表模型，添加数据列表
    model = QtCore.QStringListModel()
    # 添加列表数据
    model.setStringList(file_list)
    listView.setModel(model)


# 点击左侧表格时右侧显示数据
def clicked_display_excel(list_view, excel_display):
    global file_path
    global qModelIndex

    qModelIndex = list_view.currentIndex()
    print(qModelIndex.row())  # 点击的行索引
    # 拼接文件路径：  root文件夹路径 + 取自文件列表的文件名
    file_path = root + "/" + str(file_list[qModelIndex.row()])
    # 读取文件
    df = pd.read_excel(file_path)
    # 转化为str传给文本框显示
    excel_display.setText(str(df))


# 筛选保存
def filter_excel_data(excel_display, rButton1, MainWindow):
    if not qModelIndex:
        QtWidgets.QMessageBox.information(MainWindow, "提示信息", "请选择要筛选的表！", QtWidgets.QMessageBox.Ok)
    else:
        if file_path is not None:
            # 合并excel
            res = common_merge_excel()
            print("显示指定列数据")
            df1 = res[['买家会员名', '收货人姓名', '联系手机', '宝贝标题']]
            # 条件是宝贝标题是零基础学Python
            df2 = df1.loc[df1['宝贝标题'] == '零基础学Python']
            excel_display.setText(str(df2))
            # 调用save_excel函数，保存过滤结果到Excel
            save_excel(df2, rButton1.isChecked(), "filter_data")
        else:
            QtWidgets.QMessageBox.information(MainWindow, "提示信息", "先导入并选择一个Excel文件！", QtWidgets.QMessageBox.Ok)


# 保存数据到excel
def save_excel(df, is_checked, fiel_name):
    if (is_checked):  # 选择保存到原来路径
        writer = pd.ExcelWriter(fiel_name + '.xlsx')
    else:  # 选择另存为
        global temp_root
        writer = pd.ExcelWriter(temp_root + '/' + fiel_name + '.xlsx')
    df.to_excel(writer, 'sheet1')
    writer.save()
    print("excel文件成功保存！")


# 多表汇总
def get_column_data(excel_display, rButton1, MainWindow):
    print("汇总数据")

    if file_path is not None:
        df = pd.DataFrame(pd.read_excel(file_path))
        # 提取数据
        df = df[["买家会员名", "宝贝标题", "收货人姓名", "买家应付货款","联系手机"]]
        # 更新文本框
        excel_display.setText(str(df))
        # 把筛选后的数据命名为column_data并保存
        save_excel(df, rButton1.isChecked(), "column_data")
    else:
        QtWidgets.QMessageBox.information(MainWindow, "提示信息", "先导入并选择一个Excel文件！", QtWidgets.QMessageBox.Ok)


# 公共的合并表格函数
def common_merge_excel():
    print("开始纵向拼接表")
    file_list = []

    """
    用glob模块可以查找符合特定规则的文件路径名
    查找文件只用到三个匹配符："*", "?", "[]"
    "*"匹配0个或多个字符；"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字
    """
    files = glob.glob(root + "\*.xls")  # 查找并返回所有.xls文件名
    for file_name in files:
        file_list.append(file_name)
    res = pd.read_excel(file_list[0])
    for i in range(1, len(file_list)):
        A = pd.read_excel(file_list[i])
        # 拼接表并排序
        res = pd.concat([res, A], ignore_index=False, sort=True)
    return res


# 多表分组统计
def merge_all_excel(excel_display, rButton1, MainWindow):
    global root
    if file_path is not None:
        # 合并excel
        res = common_merge_excel()
        print("合并多表完毕")
        excel_display.setText(str(res))
        # 将合并后的数据保存到Excel
        save_excel(res, rButton1.isChecked(), "all_data")
    else:
        QtWidgets.QMessageBox.information(MainWindow, "提示信息", "先导入并选择一个Excel文件！", QtWidgets.QMessageBox.Ok)


# 多表数据排行
def multi_excel_statistics(excel_display, rButton1, MainWindow):
    if file_path is not None:
        global root
        # 合并excel
        res = common_merge_excel()
        print("分组统计排序")
        # 通过reset_index()函数将groupby()的分组结果转成DataFrame对象
        df = res.groupby(["宝贝标题"])["宝贝总数量"].sum().reset_index()  # 分组求和
        sort_df = df.sort_values(by="宝贝总数量", ascending=False)  # 对分组求和结果降序排序
        excel_display.setText(str(sort_df))
        # 调用SaveExcel函数，将统计排行结果保存到Excel
        save_excel(sort_df, rButton1.isChecked(), "sale_num_sort")
    else:
        QtWidgets.QMessageBox.information(MainWindow, "提示信息", "先导入并选择一个Excel文件！", QtWidgets.QMessageBox.Ok)


# 生成图表
def draw_grap(rButton1, MainWindow):
    if file_path is not None:
        pd_set()
        global root
        # 合并excel
        res = common_merge_excel()
        print("开始绘制图表")
        # 分组统计排序
        # 通过reset_index()函数将groupby()的分组结果转成DataFrame对象
        df = res[(res.类别 == '全彩系列')]
        df1 = df.groupby(["图书编号"])["买家实际支付金额"].sum().reset_index()
        df1 = df1[u'买家实际支付金额'].copy()
        df2 = df1.sort_values(ascending=False)  # 排序
        save_excel(df2, rButton1.isChecked(), "book_pay")
        # 图表字体为华文细黑，字号为12
        plt.rc('font', family='SimHei', size=10)
        plt.figure("贡献度分析")
        df2.plot(kind='bar')
        plt.ylabel(u'销售收入（元）')
        # cumsum()默认按列累加
        p = 1.0 * df2.cumsum() / df2.sum()
        p.plot(color='r', secondary_y=True, style='-o', linewidth=0.5)
        # annotate添加注释
        plt.annotate(format(p[9], '.4%'), xy=(9, p[9]), xytext=(9 * 0.9, p[9] * 0.9),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1"))  # 添加标记，并指定箭头样式。)
        plt.ylabel(u'收入（比例）')
        plt.savefig("贡献度分析.png", dpi=200)
        plt.show
    else:
        QtWidgets.QMessageBox.information(MainWindow, "提示信息", "先导入并选择一个Excel文件！", QtWidgets.QMessageBox.Ok)


# 单击“浏览”按钮选择文件存储路径
def set_out_excel_dir(out_file_dir_text, MainWindow):
    print("另存为......")
    global temp_root
    temp_root = QFileDialog.getExistingDirectory(MainWindow, "选择文件夹", "/")
    # 把保存路径传给file_oper_label文本标签显示
    out_file_dir_text.setText(temp_root)



