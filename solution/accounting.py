MELON_COST = 1.00


def melon_payment_calculator(payment_data_filename):
    """Calculate cost of melons and determine who has underpaid."""

    payment_data = open(payment_data_filename)

    for line in payment_data:
        order = line.split('|')

        customer_name = order[1]
        customer_first = customer_name.split(" ")[0]
        customer_melons = float(order[2])
        customer_paid = float(order[3])

        customer_expected = customer_melons * MELON_COST

        if customer_expected < customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected)
            print "{} has overpaid for their melons.".format(customer_first)

        elif customer_expected > customer_paid:
            print "{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_expected)
            print "{} has underpaid for their melons.".format(customer_first)

    payment_data.close()

melon_payment_calculator("customer-orders.txt")
