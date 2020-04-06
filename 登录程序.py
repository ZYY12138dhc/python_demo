user = 'hello world'
paswd = 123456
username = input("请输入用户名：")
password = input("请输入密码:")
for i in range(3):
  if username == user and int(password) == paswd: #判断用户名和密码是否都匹配
    print("欢迎您的到来")
    break
  elif i < 2:
    username = input("请输入用户名：")
    password = input("请输入密码")
  elif i == 2:
    print("账户已锁定")
    break
