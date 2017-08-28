#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Leooooo Zhu"
__doc__ = "集合身份验证和授权一体的系统，重点考虑异常的学习而不是系统的安全。不过在以后的改进过程中，基本框架不会动"

#User类来存储用户名和密码
import hashlib

class User:
    def __init__(self, username, password):
        '''Create a new user object. The password will be encrypted before storing.'''
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        '''Encrypt the password with the username and return the sha digest.'''
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf-8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        '''Return True if the password is valid for this user, false otherwise.'''
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

#定义异常，检测重名，密码过短等问题
class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass
class PasswordTooShort(AuthException):
    pass
#检测登入时的异常
class InvalidUsername(AuthException):
    pass
class InvalidPassword(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass
class NotPermittedError(AuthException):
    pass
#在权限映射的类中，异常不需要用户名，直接扩展到exception
class PermissionError(Exception):
    pass

#处理用户管理及登入登出
class Authenticator:
    def __init__(self):
        '''Construct an authenticator to manage users logging in and out.'''
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
authenticator = Authenticator() #默认的认证器实例

#把权限映射到用户
class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}
    #创建新用户，除非已存在
    def add_permission(self, perm_name):
        '''Create a new permission that users can be added to'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")
    #给用户添加权限，除非用户或权限不存在
    def permit_user(self, perm_name, username):
        '''Grant the given permission to the user'''
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)
    #检查用户是否具有特定权限
    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True
Authorizor = Authorizor(authenticator)

