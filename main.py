from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print('Welcome to the coffe machine')
presh_coffe_menu = Menu() #creating an object from the Menu class
names_of_coffe = presh_coffe_menu.get_items() #calling a method to get the drinks available
presh_coffee_maker = CoffeeMaker() #creating a report object
preshy_moneymachine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'What will you like ({names_of_coffe}):  ').lower()
    #calling the method find_drink from menu class, which return a menuitem
    if choice == 'report':
        presh_coffee_maker.report() #calling the report function from the report object
        preshy_moneymachine.report()
    elif choice == 'off':
        is_on = False
    elif choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
        find_coffee = presh_coffe_menu.find_drink(choice)
        resources_enough = presh_coffee_maker.is_resource_sufficient(find_coffee)
        if resources_enough:
            payment_sucessful = preshy_moneymachine.make_payment(find_coffee.cost)
            if payment_sucessful:
                presh_coffee_maker.make_coffee(find_coffee)
    else:
        print('Sorry this coffee is not available')