
def calculate_discount(price, discount_percent):
    if price <= 0:
        print('Enter value greater than 0:')
        return 0
    
    if discount_percent >= 20:
        calculate_dis = price * discount_percent / 100
        return price - calculate_dis
    else:
        return price

def main():
    try:
        price = float(input('Enter the original price: '))
        discount_percent = float(input('Enter the discount given in percentage: '))
    except ValueError:
        print('Enter valid numeric values')
        return
    
    new_price = calculate_discount(price, discount_percent)
    print('The discounted price is:', new_price)

if __name__ == '__main__':
    main()