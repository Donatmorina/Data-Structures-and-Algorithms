
#This document is a little bit all over the place, this is my preperation for the exam (coding part)


#Payapp linked with a bank assignment
from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

class PayingCustomer(Customer):
    def __init__(self, full_name, national_ID_number, address):
        self.__full_name = full_name
        self.__national_ID_number = national_ID_number
        self.__address = address
    
    def get_full_name(self):
        return self.__full_name
    
    def get_address(self):
        return self.__address
    
    def change_address(self, new_address):
        self.__address = new_address

class BankApp(ABC):
    @abstractmethod
    def bank_account_info(self):
        pass

class PayApp(BankApp):
    def __init__(self, full_name, address, national_ID_number, password, max_deposit):
        self.__customer_object = PayingCustomer(full_name, national_ID_number, address)
        self.__password = password
        self.__max_deposit = max_deposit
        self.__balance = 0
    
    def bank_account_info(self):
        print(self.__customer_object.get_full_name(), self.__customer_object.get_address())
    
    def set_password(self, current_password, new_password):
        if self.__password == current_password:
            self.__password = new_password
            print("New password is set!")
        else:
            print("Password is not correct")
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > self.__max_deposit:
            print("Limit exceeded")
        else:
            self.__balance += amount
            print("Successful deposit")

# Create PayApp object and test bank account information
pay_app = PayApp("John Doe", "123 Main St", "123456789", "password123", 10000)
pay_app.bank_account_info()
pay_app.deposit(5000)
pay_app.deposit(15000)




#ElectricDevice assignment
class ElectricDevice:
    def __init__(self, type, brand, serial_number, production_year):
        self.type = type
        self.brand = brand
        self.serial_number = serial_number
        self.production_year = production_year
        self.turned_on = False
    
    def get_brand(self):
        return self.brand
    
    def get_production_year(self):
        return self.production_year

class House:
    total_num_of_devices = 0
    def __init__(self):
        self.list_of_devices = []
        
    def add_device(self, type, brand, serial_number, production_year):
        electricdevice_object = ElectricDevice(type, brand, serial_number, production_year)
        self.list_of_devices.append(electricdevice_object)
        House.total_num_of_devices += 1
    
    @classmethod
    def print_num_of_devices(cls):
        print(cls.total_num_of_devices)

# Test House and ElectricDevice classes
house = House()
house.add_device("Washing Machine", "LG", "12345", 2020)
house.add_device("Refrigerator", "Samsung", "67890", 2019)
house.print_num_of_devices()

for device in house.list_of_devices:
    print(f"{device.type}, {device.get_brand()}, {device.get_production_year()}")




#Artist and Artgallery assignment
from abc import ABC, abstractmethod

class AbstractArtist(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

class Artist(AbstractArtist):
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
    
    def get_full_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone_number

class ArtistGallery(ABC):
    @abstractmethod
    def gallery_info(self):
        pass

class OnlineArtGallery(ArtistGallery):
    def __init__(self, name, phone_number, password, address, total_num_of_followers):
        self.__artist_object = Artist(name, address, phone_number)
        self.__password = password
        self.__total_num_of_followers = total_num_of_followers
        self.list_of_art_items = []
    
    def gallery_info(self):
        print(self.__artist_object.get_full_name(), self.__artist_object.get_phone())
    
    def set_password(self, current_password, new_password):
        if self.__password == current_password:
            self.__password = new_password
            print("New password is set!")
        else:
            print("Sorry! Password is incorrect")

    def get_sold_items(self):
        return self.list_of_art_items
    
    def add_new_art_item(self, title_of_art_item):
        self.list_of_art_items.append(title_of_art_item)
        if len(self.list_of_art_items) > 10:
            print("This list is now full!")
        else:
            print("The list is added and the list is not full!")

# Test OnlineArtGallery and Artist classes
gallery = OnlineArtGallery("Jane Doe", "1234567890", "art123", "456 Gallery St", 1000)
gallery.gallery_info()
gallery.add_new_art_item("Mona Lisa")




#Person assignment
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        print("Happy Birthday")
        self.age += 1

class Employee(Person):
    def __init__(self, name, age, id):
        self.id = id
        super().__init__(name, age)
    
    def pay(self, hours):
        rate_of_pay = 150
        payment = hours * rate_of_pay
        return payment
    
class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        self.region = region
        self.sales = sales
        super().__init__(name, age, id)
    
    def bonus(self):
        return self.sales * 0.5

# Test Person, Employee, and SalesPerson
person_1 = Person("John", 20)
employee_1 = Employee("Sara", 22, 7766)
salesperson_1 = SalesPerson("David", 19, 9090, "UK", 10000)
print(person_1.name, person_1.age)
print(employee_1.name, employee_1.age, employee_1.pay(10))
print(salesperson_1.name, salesperson_1.age, salesperson_1.bonus())




#Smartphone assignment
class Smartphone:
    def __init__(self, brand_name, colour, serial_number, production_year):
        self.brand_name = brand_name
        self.colour = colour
        self.serial_number = serial_number
        self.production_year = production_year
        self.is_available = True
    
    def get_brand(self):
        return self.brand_name
    
    def get_production_year(self):
        return self.production_year

class Store:
    total_num_smartphones = 0
    total_sold_smartphones = 0
    
    def __init__(self):
        self.inventory = []
    
    def add_smartphone(self, brand_name, colour, serial_number, production_year):
        smartphone_instance = Smartphone(brand_name, colour, serial_number, production_year)
        self.inventory.append(smartphone_instance)
        Store.total_num_smartphones += 1
    
    def sell_smartphone(self):
        Store.total_sold_smartphones += 1
    
    @classmethod
    def print_total_sold_smartphones(cls):
        print(cls.total_sold_smartphones)

# Test Store and Smartphone
object_2 = Smartphone("Nokia", "red", 4456, 1994)
print(object_2.get_brand(), object_2.get_production_year())
object_3 = Store()
object_3.add_smartphone("Iphone", "black", 8884462, 2018)
object_3.add_smartphone("Samsung", "blue", 4442242, 1992)
object_3.sell_smartphone()
object_3.print_total_sold_smartphones()




#Football player assignment
from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_number = id_number
    
    def get_full_name(self):
        return self.__first_name, self.__last_name
    
    def get_id_number(self):
        return self.__id_number

class Team(ABC):
    @abstractmethod
    def team_info(self):
        pass

class FootballTeam(Team):
    def __init__(self, team_name, first_name, last_name, id_number, home_stadium, num_of_players):
        self.__team_name = team_name
        self.__home_stadium = home_stadium
        self.__num_of_players = num_of_players
        self.__captain = FootballPlayer(first_name, last_name, id_number)
        self.list_of_players = []
    
    def team_info(self):
        print(self.__team_name, self.__captain.get_full_name())
        
    def get_players(self):
        return self.list_of_players
    
    def add_new_player(self, id_of_football_player):
        self.list_of_players.append(id_of_football_player)
        if len(self.list_of_players) > 25:
            print("Football Player added and the list is now full!")
        else:
            print("Football Player added and the list is not full!")

# Test FootballPlayer and FootballTeam
object_player = FootballPlayer("John", "Rodgers", 5542)
print(object_player.get_full_name(), object_player.get_id_number())
football_team = FootballTeam("Team A", "John", "Rodgers", 5542, "Stadium A", 11)
football_team.team_info()
football_team.add_new_player(5555)
