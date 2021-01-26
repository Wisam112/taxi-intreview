from classes import *


def main():
    # Execution
    # Step 1
    taxi_station = taxiStation(10)
    # Step 2
    customers_id = 1
    for _ in range(9):
        customer = Customer(customers_id, "Customer " + str(customers_id))
        taxi = taxi_station.order(customer)
        customers_id += 1
    # Step 3
    taxi_station.order(vipCustomer(customers_id, "Customer " + str(customers_id)))
    customers_id += 1
    # Step 4
    for _ in range(2):
        taxi_station.order(Customer(customers_id, "Customer " + str(customers_id)))
        customers_id += 1
    # Step 5
    taxi_station.order(vipCustomer(customers_id, "Customer " + str(customers_id)))
    customers_id += 1
    # Step 6
    taxi_station.taxi_return(1)
    # Step 7
    taxi_station.order(vipCustomer(customers_id, "Customer " + str(customers_id)))
    customers_id += 1
    # Step 8
    taxi_station.taxi_return(2)
    # Step 9
    taxi_station.taxi_return(3)


if __name__ == "__main__":
    main()