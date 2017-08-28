#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "Leooooo Zhu"
__doc__ = "python3面向对象编程第三章练习"

class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email) #用super()方法返回父类的实例化对象，允许我们直接调用父类的方法
        self.phone = phone

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Supplier(Contact):
    def order(self, order):
        print("if this were a real system we would send "
                "{} order to {}".format(order, self.name))

c = Contact("SOme Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net") #继承父类方法，确定名字等

print(c.name, c.email, s.name, s.email)
print(c.all_contacts)
s.order("I need pliers") #属于SUPPLIER类
