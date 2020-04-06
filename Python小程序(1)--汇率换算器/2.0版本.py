#版本：2.0
#新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
#日期：2019.10.21
#导读：
"""判断输入的是美元还是人民币，输入带单位的金额"""

usd_vs_rmb = 6.77
 
#带单位的金额输入
currency_str_value = input("请输入带单位的货币金额：")
 
#获取货币单位
unit = currency_str_value[-3:]
 
if unit == 'CNY':
 
    rmb_str_value = currency_str_value [:-3]
    #将字符串转化为数字
    rmb_value = eval(rmb_str_value )
    usd_value = rmb_value / usd_vs_rmb
    print('美元usd的金额是',usd_value)
 
elif unit == 'USD':
    usd_str_value = currency_str_value [:-3]
    #将字符串转化为数字
    usd_value = eval(usd_str_value )
    rmb_value = usd_value * usd_vs_rmb
    print('人民币rmb的金额是',rmb_value)
 
else:
    #其他情况
    print('目前版本不支持其他货币')
