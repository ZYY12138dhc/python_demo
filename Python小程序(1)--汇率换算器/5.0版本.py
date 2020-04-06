#版本：5.0
#新增功能：增加功能：(1)使程序结构化(2)简单函数的定义
#lambda 函数<函数名> = lambda <参数列表>: <表达式>• 用于简单的、能够在一行内表示的函数，计算结果为返回值

 
 
# def converter_currency(im,er):
#     out = im * er
#     return out
 
def main():
    '''
    主函数
    '''
 
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
        #使用lambda定义函数
        converter_currency2 = lambda x:x*exchange_rate
 
        # #调用函数
        # out_money = converter_currency(in_money,exchange_rate )
 
        #调用lambda函数
        out_money = converter_currency2 (in_money )
        print('转换后的金额：',out_money )
 
    else:
        print('不支持该种货币！')
 
if __name__ == '__main__':
    main()
