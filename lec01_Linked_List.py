# lets remember the class
# A class is like a template that we use to create objects that have attributes and methods.
# class _ attributes _ methods _ object
class car:  # class
    def __init__(self, color, speed):  # attributes
        self.color = color
        self.speed = speed

    def drive(self):     # method
        print(
            f"this car has color {self.color} and has speed {self.speed} km/h ")


my_car = car("red ", 100)  # object
my_car.drive()

print("")
print("________________________________________________________________________")
print("")

# Linked list
# stock_ market price
# the price with it's time is node
# opening price in the day is a head node
# closing price in the day is a tail node
# print all the prices in the day or graph them
# we can search the price and get its time
# lets go to our linked list program


class stock_price_Node:
    def __init__(self, price, timestamp):
        self.price = price
        self.timestamp = timestamp
        self.next = None


class stock_price_list:
    def __init__(self):  # initial list
        self.head = None
        self.tail = None

    def add_price_head_node(self, price, timestamp):
        new_price = stock_price_Node(price, timestamp)
        if self.head is None:
            self.head = new_price
            self.tail = new_price
        else:
            new_price.next = self.head
            self.head = new_price

    def add_price_tail_node(self, price, timestamp):
        new_price = stock_price_Node(price, timestamp)
        if self.head is None:
            self.head = new_price
            self.tail = new_price
        else:
            self.tail.next = new_price
            new_price = self.tail

    def print_linked_list(self):
        current_price = self.head
        while current_price is not None:
            print(
                f"{current_price.price} [{current_price.timestamp}] ", end=" -> ")
            current_price = current_price.next
        print("NULL")

    def search_data_node(self, price):
        current_price = self.head
        while current_price is not None:
            if current_price.price == price:
                return current_price.timestamp
            current_price.next
        return None


    # مثال تحليل كمي: تتبع أسعار سهم تسلا
tesla_prices = stock_price_list()

tesla_prices.add_price_head_node(
    300.00, "2025-06-11 08:00")  # سعر افتتاح اليوم
tesla_prices.print_linked_list()

tesla_prices.add_price_tail_node(305.50, "2025-06-11 09:00")  # سعر الساعة 9

tesla_prices.print_linked_list()

tesla_prices.add_price_tail_node(307.75, "2025-06-11 10:00")  # سعر الساعة 10

tesla_prices.print_linked_list()


print(tesla_prices.search_data_node(307.75))  # هتطبع: 2025-06-11 10:00
print(tesla_prices.search_data_node(310.00))  # هتطبع: None
