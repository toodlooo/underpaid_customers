MELON_COST = 1

number_of_customers_underpaid = 0
number_of_customers_overpaid = 0
number_of_customers_ok = 0
total_customers = 0

def customers_in_debt(file):
    """ Calculates whether the paid price from the customers was the full price. If not, how much do they owe. """
    
    global number_of_customers_underpaid
    global number_of_customers_overpaid
    global number_of_customers_ok
    global total_customers

    orders = open(file)

    for order in orders:
        data = order.split("|")
        
        customer_name = data[1]
        number_of_melons = float(data[2])
        actual_pay = float(data[3])
        
        expected_pay = number_of_melons * MELON_COST
        
        if expected_pay > actual_pay:
            number_of_customers_underpaid += 1
            print "UNDERPAID! {} paid ${:.2f}, but was expected to pay ${:.2f}. They owe ${:.2f}".format(customer_name, actual_pay, expected_pay, expected_pay-actual_pay)

        elif expected_page < actual_pay:
            number_of_customers_overpaid += 1
            print "OVERPAID! {} paid ${:.2f}, but was expected to pay ${:.2f}. We owe them ${:.2f}".format(customer_name, actual_pay, expected_pay, expected_pay-actual_pay)

        elif actual_pay == expected_pay:
            number_of_customers_ok += 1
            print "JUST RIGHT! {} paid ${:.2f} and was expected to pay ${:.2f}.".format(customer_name, actual_pay, expected_pay)    

        total_customers += 1

    orders.close()


customers_in_debt("customer-orders.txt")
print "\nOkay, so we've got {} customers".format(total_customers)
print "{} customers still owe money!".format(number_of_customers_underpaid)
print "We need to pay back {} customers their money :/".format(number_of_customers_overpaid)
print "{} customers paid juuuust right".format(number_of_customers_ok)
