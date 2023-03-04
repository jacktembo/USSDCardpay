import os
import requests
from time import sleep
import phone_numbers

base_url = 'https://cards.pridezm.com'
current_phone_number = '0971977252'

select_option = input("""
Welcome To All1Zed Card
1. Topup Card
2. Check Balance
3. Send Money
4. Pay Merchant
5. Resend-Pin
6. Block Card
7. Register Card

""")


def clear():
    os.system('clear')


if select_option == '1':
    clear()
    topup_dialog = input("""
    1. Topup Own Card
    2. Topup Other Card
    
    """)
    if topup_dialog == '1':
        clear()
        amount = input("""
        Enter Amount
        """)
        data = {"phone_number": current_phone_number, "txn_amount": amount}
        if phone_numbers.get_network(current_phone_number) == 'airtel':
            print('Please Wait...')
            r = requests.post(base_url + '/api/payments/airtelPayment/', json=data)
            clear()
            print('Please confirm the payment on your phone...')
            sleep(35)

        elif phone_numbers.get_network(current_phone_number) == 'mtn':
            print('Please Wait...')
            r = requests.post(base_url + '/api/payments/mtnPayment/', json=data)
            clear()
            print('Please confirm the payment on your phone...')
            sleep(35)
        elif phone_numbers.get_network(current_phone_number) == 'zamtel':
            print('Please Wait...')
            r = requests.post(base_url + '/api/payments/zamtelPayment/', json=data)
            clear()
            print(r.text)
            print('Please confirm the payment on your phone...')
            sleep(35)
    elif topup_dialog == '2':
        clear()
        other_card = input("""
        Enter Card Number
        
        """)
        clear()
        amount = input("""
        Enter Amount
        
        """)
        clear()
        data = {"phone_number": current_phone_number, "txn_amount": amount, "card_number": other_card}
        r = requests.post(base_url + '/api/payments/airtelPayment/', json=data)
        print(r.text)
elif select_option == '2':
    clear()
    data = {"phone_number": current_phone_number}
    r = requests.post(base_url + '/api/accounts/card/balance', json=data)
    print(f"You current balance is ZMW {r.json().get('balance', r.text)}")

elif select_option == '3':
    clear()
    send_to = input("""
    Send Money:
    1. To Mobile
    2. To Bank
    
    """)
    if send_to == '1':
        clear()
        network = input("""
        Choose Network:
        1. Airtel
        2. MTN
        3. Zamtel
        
        """)
        clear()
        amount = input("""
        Enter Amount
        
        """)
        data = {"phone_number": current_phone_number, "txn_amount": amount}
        r = requests.post(base_url, json=data)
    elif send_to == '2':
        clear()
        bank = input("""
        Choose Bank:
        1. Absa Bank Zambia
        2. Zanaco
        3. StanChart Zambia
        4. AtlasMara
        5. Access Bank
        6. Investrust 
        7. Indo bank
        """)
        banks_dic = {
            "1": "Absa Bank Zambia", "2": "Zanaco", "3": "StanChart Zambia", "4": "AtlasMara",
            "5": "Access Bank", "6": "Investrust", "7": "Indo Bank",
        }
        clear()
        print(f"Send Money To {banks_dic[bank]}:")
        amount = input("""
        Enter Amount
        """)

elif select_option == '6':
    clear()
    option = input("""
    1. Block Card
    2. Unblock Card
    
    """)
    if option == '1':
        clear()
        phone_number = current_phone_number
        data = {"phone_number": phone_number}
        r = requests.post(base_url, json=data)
        print(r.text)
    elif option == '2':
        clear()
        phone_number = current_phone_number
        data = {"phone_number": phone_number}
        r = requests.post(base_url, json=data)
        print(r.text)
elif select_option == '7':
    clear()
    first_name = input("""
    Enter First Name:
    
    """)
    clear()
    print('Please Wait...')
    sleep(2)
    clear()
    last_name = input("""
    Enter Last Name:
    
    """)
    clear()
    print('Please Wait...')
    sleep(2)
    clear()
    phone_number = input("""
    Enter Phone Number:
    
    """)
    clear()
    print('Please Wait...')
    sleep(2)
    clear()
    card_number = input("""
    Enter Card Number:
    
    """)
    clear()
    print('Please Wait...')
    sleep(2)
    clear()
    print('Please Wait...')
    data = {
        "first_name": first_name, "last_name": last_name, "phone_number": phone_number, "card_number": card_number
    }
    r = requests.post(base_url + '/accounts/card_account/register/', json=data)
    if r.json().get('Success', None) == "Created":
        print("Card Registered Successfully")
    else:
        print("Something Went Wrong")