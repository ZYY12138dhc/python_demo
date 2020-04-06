#版本：4.0
#新增功能：增加功能：将汇率兑换功能封装到函数中
#日期：2019.10.30
#导读：增加功能：将汇率兑换功能封装到函数中，使程序模块化
 
 
def converter_currency(im,er):
    out = im * er
    return out
 
usd_vs_rmb = 6.77
 
#带单位的金额输入
currency_str_value = input("请输入带单位的货币金额：")
 
unit = currency_str_value[-3:]
 
if unit == 'CNY':
    exchange_rate = 1 / usd_vs_rmb
 
elif unit == 'USD':
    exchange_rate = usd_vs_rmb
 
else:
    exchange_rate = -1
 
if exchange_rate != -1:
    in_money = eval(currency_str_value [:-3])
 
    #调用函数
    out_money = converter_currency(in_money,exchange_rate )
    print('转换后的金额：',out_money )
 
else:
    print('不支持该种货币！')
