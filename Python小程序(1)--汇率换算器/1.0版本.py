#版本：1.0
#日期：2019.4.27
#导读：
"""为了使程序简单，目前只使用一种外币-美元  汇率6.77
设计算法：输入人民币金额→汇率计算→输出相应的美元金额
输出=输入/汇率."""

rmb_str_value = input("请输入人民币金额：")
 
rmb_value = eval(rmb_str_value)
use_vs_rmb = 6.77
 
use_value = rmb_value / use_vs_rmb
 
print('美元金额是:',use_value )
