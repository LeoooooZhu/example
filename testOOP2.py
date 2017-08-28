#! /usr/bin/env python3
# -*- coding:utf-8

__author__ = "Leooooo Zhu"
__doc__ = "py3 OOP 第四章部分练习.展示异常的处理情况。P95-P96"

#demo1
'''
import random 
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" % (e.__class__.__name__))
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")
'''

#demo2
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
#        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I am sorry, but your withdrawal is "
            "more than your balance by "
            "${}".format(e.overage()))


#demo3
#一个库存模型
class Inventory:
    def lock(self, item_type):
        pass
    def unlock(self, item_type):
        pass
    def purchase(self, item_type):
        pass

item_type = 'widget'
inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("Sorry, we do not sell {}".format(item_type))
except OuyOfStock:
    print("Sorry, that item is out of stock.")
else:
    print("Purchase complete. There are "
            "{} {}s left".format(num_left, item_type))
finally:
    inv.unlock()
