# -*- coding: utf-8 -*-
"""
@Author: Cinja
@Software: PyCharm
@File: main.py
@Date: 2022/5/19
"""

def calu_total(dic):
    summary = 0
    for i in dic.values():
        summary += i
    return summary


def balance(dic, each_cost):
    new_dic = {}
    for i in dic.keys():
        values = dic[i] - each_cost
        new_dic.update({i: values})
    return new_dic


if __name__ == '__main__':
    dic = {}
    while True:
        name = input("Please input a Name (Type 'exit' to exit):")

        if name == 'exit':
            break

        while True:
            value = input("Please input a Value (Type '-1' to return to previous level):")
            value = float(value)
            if value != -1:
                if dic.get(name) != None:
                    dic[name] += value
                else:
                    dic.update({name: value})
            else:
                break

    # test_dic = {'a': 132, 'b': 123}
    people = len(dic)
    total_cost = calu_total(dic)
    each_cost = total_cost / people
    balance_dic = balance(dic, each_cost)

    print("========================================")
    print("Each cost is :{}".format(each_cost))
    print("========================================")
    print("Balance per one: ")
    print(balance_dic)