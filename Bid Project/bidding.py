import os
import sys
from art import logo 
print(logo)

bid_dic = {}
bidding_end = False

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def find_height(bidding_record):
    height_bid = -sys.maxsize - 1
    winner = ""
    for bid_key in bidding_record:
        bid_ammount = bidding_record[bid_key]
        if bid_ammount > height_bid:
            height_bid = bid_ammount
            winner = bid_key
    clear_console()
    print("*************************************************************")
    print()
    print()
    print(f'The winner is: {winner} with a bid amount of ${height_bid}.')
    print()
    print()
    print("*************************************************************")

while not bidding_end:
    name = input("Enter Bidder Name : ")
    price = int(input("Enter Bidder Bid Price : $"))
    bid_dic[name] = price

    ans = input("Are there any other bidders? Type 'Yes' or 'No'. ")
    if ans.lower() == "no":
        bidding_end = True
        find_height(bid_dic)
    elif ans.lower() == "yes":
        clear_console() 
