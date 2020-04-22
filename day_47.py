"""
《python常用模块（5）》
知识点：
1..dat文件
2. 
"""
>>> import pickle
>>> game_data={'life':158,'weapon':['fire-gun','knife','axe'],'wealth':['3golds','6diamonds']}
>>> save_data=open('C:/Users/15064/Desktop/01.dat','wb')#wb,以二进制的形式存储数据
>>> pickle.dump(game_data,save_data)
>>> save_data.close()


>>> load_data=open('C:/Users/15064/Desktop/01.dat','rb')#读取
>>> read_load_data=pickle.load(load_data)#反编译
>>> load_data.close()
>>> print(read_load_data)
{'life': 158, 'weapon': ['fire-gun', 'knife', 'axe'], 'wealth': ['3golds', '6diamonds']}
>>> 
