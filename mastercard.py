mastercard = {
    '5636543678':('Jefferson Orji','173675363636','03/21','563'),
    '6365436790':('Joseph Ogbu','273695363637','12/23','004')
}

acct_no = input('Enter account number \n')
if acct_no in mastercard:
    card_no = input('Enter card number \n')
    while mastercard[acct_no][1] != card_no:
        print('You entered a wrong card number')
        card_no = input('Try again \n')
    name_on_card = mastercard[acct_no][0]
    print(f'Name on card {name_on_card}')
    expiry = input('Enter expiry date \n')
    cvv = input('Enter CVV \n')
    
    if mastercard[acct_no][2] == expiry and mastercard[acct_no][3] == cvv:
        from random import randrange
        token = randrange(100000,999999)
        print(token)
        re_token = int(input('Enter token \n'))
        if re_token == token:
            print('Transaction completed!')
        else:
            print('Failed transaction: incorrect token')
else:
    print('Unidentified account')
