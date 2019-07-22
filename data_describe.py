#数据挖掘第一周
#数据的描述性统计
import math
import numpy as np
#众数
def zhongshu(num_list):
    counts=np.bincount(num_list)
    return np.argmax(counts)
#中位数
def zhongweishu(num_list):
    return np.median(num_list)
#分位数
def fenweishu_25(num_list):
    return np.percentile(num_list, 25)
def fenweishu_75(num_list):
    return np.percentile(num_list, 75)
#算术平均数
def pingjunshu(num_list):
    return np.mean(num_list)
#几何平均数
def jihepingjun(num_list):
    for num in num_list:
        numbynum=numbynum*num
    return pow(numbynum,len(num_list))

#加权平均数
def jiaquanpinjun(num_list):
    return np.average(num_list,1,2,3,2,1,1)
#方差
def fangcha(num_list):
    return np.var(num_list)
#标准差
def biaozhuncha(num_list):
    return np.std(num_list)
#极差
def jicha(num_list):
    return np.max(num_list)-np.min(num_list)
#平均差
def pingjuncha(num_list):
    num_mean = np.mean(num_list)
    newnum_list = []
    for num in num_list:
        newnum_list.append(abs(num-num_mean))
    return np.mean(newnum_list)

#四分位差
def fenweicha(num_list):
    return fenweishu_75(num_list)-fenweishu_25(num_list)
#异众比率
def yizhongbilv(num_list):
    counts =np.bincount(num_list)
    return 1-(np.max(counts)/len(num_list))
#离散系数
def lisanxishu(num_list):
    return np.std(num_list)/np.mean(num_list)
#偏态系数

#峰态系数




if __name__ == '__main__':
    list = [2, 10, 60, 6, 5, 6]
    print(pingjunshu(list))
    print(pingjuncha(list))
    print(jiaquanpinjun(list))