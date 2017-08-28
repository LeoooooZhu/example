#! /usr/bin/env
# -*- coding:utf-8 -*-

__author__ = "Leooooo Zhu"
__doc__ = "py3面向对象编程第三章案例学习.房地产应用程序，允许一个代理来管理用于购买或者租赁的房产.卡住了，P79页。 练习git status and git diff"

from get_valid_input import get_valid_input

class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def promptinit():
        return dict(square_feet=input("Enter the square feet: "),
                beds=input("Enter number of bedrooms: "),
                baths=input("Enter number of baths: "))
    promptinit = staticmethod(promptinit) #静态方法，只和一个类关联，而不是具体对象实例

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def promptinit():
        parentinit = Property.promptinit()
        laundry = get_valid_input(
                "What laundry faciliaties does"
                "the property have?",
                Apartment.valid_laundries)

        bacony = get_valid_input(
                "Does the property have a balcony? ",
                Apartment.valid_balconies)
        parentinit.update({
            "laundry": laundry,
            "balcony": balcony
            })
        return parentinit
    promptinit = staticmethod(promptinit)

class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def promptinit():
        parentinit = Property.promptinit()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parentinit.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
            })
        return parentinit
    promptinit = staticmethod(promptinit)

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def promptinit():
        return dict(
                price = input("What is the selling price? "),
                taxes = input("What are the estimated taxes? "))
        promptinit = staticmethod(promptinit)

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def promptinit():
        return dict(
                rent = input("What is the monthly rent? "),
                utilities = input("What are the estimated utilities? "),
                furnished = get_vaild_input("Is the property furnished? ",("yes", "no")))
        promptinit = staticmethod(promptinit)


class HouseRental(Rental, House):
    def promptinit():
        promptinit = House.promptinit()
        promptinit.update(Rental.promptinit())
        return promptinit
    promptinit = staticmethod(promptinit)
