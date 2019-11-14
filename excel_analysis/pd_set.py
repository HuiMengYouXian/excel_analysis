import pandas as pd


def pd_set():
    # 设置显示数据的最大列数，防止出现省略号…，导致数据显示不全
    pd.set_option('display.max_columns', 100)
    # pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行
    # 设置Dataframe对象列宽为200，默认为50
    pd.set_option('max_colwidth', 200)