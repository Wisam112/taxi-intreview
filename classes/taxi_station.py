from dataclasses import dataclass
from classes.taxi import Taxi
from classes.customer import Customer
from classes.vip_customer import vipCustomer



class taxiStation:

    # Constructor
    def __init__(self, num_of_taxis):
        self.taxis_available = num_of_taxis
        self.taxis_list = [Taxi(i + 1, True) for i in range(num_of_taxis)]
        self.customers_queue = []
        self.vip_queue = []


    # Order a taxi for a customer
    def order(self, customer):
        if not isinstance(customer, Customer) and not isinstance(customer, vipCustomer):
            raise "Illegal customer type!" 
        if self.taxis_available > 0:
            for taxi in self.taxis_list:
                if taxi.available:
                    self.taxi_pickup(taxi, customer)
                    break
        else:
            if isinstance(customer, vipCustomer):
                self.vip_queue.append(customer)
                print(f"VIP Customer Name: {customer.name} requested a taxi and is waiting in the VIP list.")
            else:
                self.customers_queue.append(customer)
                print(f"Customer Name: {customer.name} requested a taxi and is waiting in the list.")

    
    # Send the taxi to the customer
    def taxi_pickup(self, taxi, customer):
        self.taxis_available -= 1
        taxi.available = False
        if isinstance(customer, vipCustomer):
            print(f"Taxi ID {taxi.taxi_id} picked up a VIP customer {customer.name}.")
        else:
            print(f"Taxi ID {taxi.taxi_id} picked up a customer {customer.name}.")

    

    # Find the taxi object from its id
    def get_taxi_from_id(self, taxi_id):
        for taxi in self.taxis_list:
            if taxi.taxi_id == taxi_id:
                return taxi
        return None


    # Taxi has returned to the station
    def taxi_return(self, taxi_id):
        taxi = self.get_taxi_from_id(taxi_id)
        if not taxi:
            return
        self.taxis_available += 1
        taxi.available = True
        print(f"Taxi ID: {taxi.taxi_id} has returned to the station.")
        if not self.check_vip_list(taxi):
            self.check_regular_list(taxi)


    # Check if there is someone waiting in the VIP queue
    def check_vip_list(self, taxi):
        if len(self.vip_queue) == 0:
            return False
        customer = self.vip_queue.pop(0)
        self.taxi_pickup(taxi, customer)
        return True

    
    # Check if there is someone waiting in the regular queue
    def check_regular_list(self, taxi):
        if len(self.customers_queue) == 0:
            return False
        customer = self.customers_queue.pop(0)
        self.taxi_pickup(taxi, customer)
        return True