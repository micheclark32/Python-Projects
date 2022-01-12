import csv

PRODUCT_NUMBER = 0
ITEM_NAME = 1
RETAIL_PRICE = 2


def main():
    try:
        products = read_products('products.csv')
        print('Inkom Emporium:')
        print(products)
        print('')
        process_request('request.csv', products)

    except FileNotFoundError as error:
        filename = error[len(error) - 1]
        print(
            f"The filename of {filename} was not found. Please adjust it and try again.")

    except PermissionError as error:
        print("You do not have access to this file.")

    except KeyError as error:
        print("Error: item missing from request.csv")


def read_products(file_name):
    prod_dict = {}
    with open(file_name, 'rt') as products:
        csv_products = csv.reader(products)
        next(csv_products)  # skips title
        for row in csv_products:  # grabbing dict data and printing
            key = row[PRODUCT_NUMBER]
            name = row[ITEM_NAME]
            retail_price = float(row[RETAIL_PRICE])
            prod_dict[key] = name, retail_price
    return prod_dict


def process_request(request_file, products):
    with open(request_file, mode="rt") as request_file:
        request_list = csv.reader(request_file)

        next(request_list)

        prod_total = 0
        subtotal = 0

        for i in request_list:
            prod_num = i[0]
            prod_quant = int(i[1])

            if prod_num in products:  # checks if the requested item is a real product
                prod_name = products[prod_num][0]
                prod_price = float(products[prod_num][1])

                # adds the number of items to the item total
                prod_total += prod_quant

                # Takes quantity x the price of item
                subtotal += prod_quant * prod_price

                # prints the product name, amount requested and the product price
                print(f"{prod_name}: {prod_quant} @ ${prod_price}")

            else:  # if the requested product doesnt match with one on the list
                print(f"Input error: product {prod_num} not recognized")

    print()

    # displays the amount of items
    print(f"Number of items: {prod_total}")

    # displays the subtotal
    print(f"Your subtotal is: ${subtotal:.2f}")

    # calculates and prints the amount of tax at a 6% rate
    tax = subtotal * .06
    print(f"Tax: ${tax:.2f}")

    # calculates the total and prints
    total = subtotal + tax
    print(f"Total: ${total:.2f}")
    print()

    print("Thank you for shopping at the Inkom Emporium.")
    print({print_time})


def print_time():
    # Import the datatime module so that
    # it can be used in this program.
    from datetime import datetime

    # Call the now() method to get the current date and
    # time as a datetime object from the computer's clock.
    current_date_and_time = datetime.now()

   # Print the current day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")


if __name__ == main():
    main()
