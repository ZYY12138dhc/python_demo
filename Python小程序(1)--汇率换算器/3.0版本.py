#版本：3.0
#新增功能：程序可以一直运行，直到用户选择退出
#日期：20191026
#导读：
"""增加功能:程序可以一直运行，直到用户选择退出
   方法：循环语句while"""

usd_vs_rmb = 6.77
 
#带单位的金额输入
currency_str_value = input("请输入带单位的货币金额(退出程序请输入Q)：")
 
i = 0
while currency_str_value != 'Q':
    i += 1
    print ("循环次数：",i)
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
 
    print('**********************************')
    # 带单位的金额输入
    currency_str_value = input("请输入带单位的货币金额(退出程序请输入Q)：")
print('程序已退出')
