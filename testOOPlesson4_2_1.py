#! /usr/env/bin python3
# -*- coding:utf-8 -*-

__author__ = "Leooooo Zhu"
__doc__ = "用户菜单接口，运行特定用户去改变或测试程序"

import testOOPlesson4_2

#创建一个测试用户并设置权限
testOOPlesson4_2.authenticator.add_user("joe", "joepassword")
testOOPlesson4_2.Authorizor.add_permission("test program")
testOOPlesson4_2.Authorizor.add_permission("change program")
testOOPlesson4_2.Authorizor.permit_user("test program", "joe")

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
                "login": self.login,
                "test": self.test,
                "change": self.change,
                "quit": self.quit}

        def login(self):
            logged_in = False
            while not logged_in:
                username = input("username: ")
                password = input("password: ")
                try:
                    logged_in = testOOPlesson4_2.authenticator.login(username, password)
                except testOOPlesson4_2.InvalidUsername:
                    print("Sorry, that username does not exist")
                except testOOPlesson4_2.InvalidPassword:
                    print("Sorry, incorrect password")
                else:
                    self.username = username

        def is_permitted(self, permission):
            try:
                testOOPlesson4_2.Authorizor.check_permission(permission, self.username)
            except testOOPlesson4_2.NotLoggedInError as e:
                print("{} is not logged in".format(e.username))
                return False
            except testOOPlesson4_2.NotPermittedError as e:
                print("{} cannot {}".format(e.username, permission))
                return False
            else:
                return True

        def test(self):
            if self.is_permitted("test progeam"):
                print("Testing program now...")
        def change(self):
            if self.is_permitted("change program"):
                print("Changing program now...")
        def quit(self):
            raise SystemExit()
        def menu(self):
            try:
                answer = ""
                while True:
                    print("""
                    Please enter a command:
                    \tlogin\tLogin
                    \ttest\tTest the program
                    \tchange\tChange the program
                    \tquit\tQuit
                    """)
                    answer = input("enter a command: ").lower()
                    try:
                        func = self.menu_map[answer]
                    except KeyError():
                        print("{} is not a valid option".format(answer))
                    else:
                        func()
            finally:
                print("Thank you for testing the testOOPlesson4_2 module")

    Editor().menu()
