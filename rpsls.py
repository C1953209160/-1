#coding:gbk
"""
rpsls小游戏
植产六班程柯举
"""

import random


"""
0 - 石头
1 - 史波克
2 - 纸
3 - 蜥蜴
4 - 剪刀
"""
# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    if name=='石头':
      return 0
    elif name=='史波克':
      return 1
    elif name=='纸':
      return 2
    elif name=='蜥蜴':
      return 3
    elif name=='剪刀':
      return 4
    else:
      return print("Error:No Carrect Name")

   

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
      return '石头'
    elif number==1:
      return '史波克'
    elif number==2:
      return '纸'
    elif number==3:
      return '蜥蜴'
    elif number==4:
      return '剪刀'
    else:
      return print("Error:No Carrect Name")



def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("--------")
    print("游戏者的选择是"+player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print("计算机的选择是"+comp_choice)
    diff=(comp_number-player_number)%5
    if diff==1 or diff==2:
      print("机器赢了")
    elif diff==3 or diff==4:
      print("您赢了")
    elif diff==0:
      print("平局")
    else:
      print("Error:No Carrect Name")

     


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)

