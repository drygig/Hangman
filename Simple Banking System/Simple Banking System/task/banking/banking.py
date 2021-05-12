# # Write your code here
# import random
# import sqlite3
# conn = sqlite3.connect('card.s3db')
# cur = conn.cursor()
# cur.execute('drop table if exists card;')
# # Executes some SQL query
# cur.execute("CREATE TABLE if not exists card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER default 0);")
#
# # After doing some changes in DB don't forget to commit them!
# conn.commit()
#
#
# card = {"card_number": 0, "pin": 0}
# iin = "400000"
# balance = 0
# while True:
#     print("1. Create an account")
#     print("2. Log into account")
#     print("0. Exit")
#     choice = input()
#     if choice == "0":
#         print()
#         print("Bye!")
#         break
#     elif choice == "1":
#         random_part = random.randint(100000000, 999999999)
#         card_no_15 = iin + str(random_part)
#         card_map = map(int, card_no_15)
#         card_list = list(card_map)
#         # print(card_list)
#         card_list_2 = [card_list[x] * 2 if x % 2 == 0 else card_list[x] for x in range(len(card_list))]
#         # print(card_list_2)
#         card_list_3 = [card_list_2[x] - 9 if card_list_2[x] > 9 else card_list_2[x] for x in range(len(card_list_2))]
#         # print(card_list_3)
#         card_sum = 0
#         for x in range(len(card_list_3)):
#             card_sum += card_list_3[x]
#         card_sum = str(card_sum)
#         # print(card_sum)
#         if int(card_sum) % 10 == 0:
#             check_sum = 0
#         else:
#             check_sum = 10 - int(card_sum[1])
#             # print(check_sum)
#             card["card_number"] = iin + str(random_part) + str(check_sum)
#             print()
#             print("Your card has been created")
#             print("Your card number:")
#             print(card["card_number"])
#             sql_card = int(card["card_number"])
#             print("Your card PIN:")
#             card["pin"] = random.randint(1000, 9999)
#             print(card["pin"])
#             sql_pin = int(card["pin"])
#             print()
#             cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)",(sql_card, sql_pin))
#             conn.commit()
#
#     elif choice == "2":
#         print()
#         print("Enter your card number:")
#         card_number = int(input())
#         print("Enter your PIN:")
#         pin_number = int(input())
#         if int(card["card_number"]) != card_number or int(card["pin"]) != pin_number:
#             print()
#             print("Wrong card number or PIN!")
#             print()
#         else:
#             print()
#             print("You have successfully logged in!")
#             while True:
#                 print()
#                 print("1. Balance")
#                 print("2. Add income")
#                 print("3. Do transfer")
#                 print("4. Close account")
#                 print("5. Log out")
#                 print("0. Exit")
#                 choice_2 = input()
#                 if choice_2 == "1":
#                     print()
#                     print("Balance: {}".format(balance))
#                 elif choice_2 == "2":
#                     print()
#                     print("Enter income:")
#                     income = int(input())
#                     balance += income
#                     cur.execute('UPDATE card SET balance={} WHERE number={}'.format(balance, sql_card))
#                     conn.commit()
#                     print("Income was added!")
#                 elif choice_2 == "3":
#                     print()
#                     print("Do transfer")
#                     print("Enter card number:")
#                     card_number_trans = input()
#                     card_map_trans = map(int, card_number_trans)
#                     card_list_trans = list(card_map_trans[:-1])  #15 first digits
#                     card_list_trans_check = list(card_map_trans[-1])  #last digit
#                     card_list_trans_1 = [card_list_trans[x] * 2 if x % 2 == 0 else card_list_trans[x] for x in range(len(card_list_trans))]
#                     card_list_trans_2 = [card_list_trans_1[x] - 9 if card_list_trans_1[x] > 9 else card_list_trans_1[x] for x in range(len(card_list_trans_1))]
#                     card_sum_trans = 0
#                     for x in range(len(card_list_trans_2)):
#                         card_sum_trans += card_list_trans_2[x]
#                     card_sum_trans += card_list_trans_check[0]
#                     if int(card_number_trans) == int(card["card_number"]):
#                         print("You can't transfer money to the same account!")
#                     elif card_number_trans[0:5] != "400000" or card_sum_trans != 10:
#                         print("Probably you made a mistake in the card number. Please try again!")
#                     elif
#                         print("Such a card does not exist.")
#                     else:
#
#                 elif choice_2 == "4":
#                     cur.execute('DELETE FROM card WHERE number={}'.format(card_number))
#                     conn.commit()
#                     print()
#                     print("The account has been closed!")
#                     exit()
#                 elif choice_2 == "5":
#                     print()
#                     print("You have successfully logged out!")
#                     print()
#                     break
#                 elif choice_2 == "0":
#                     print()
#                     print("Bye!")
#                     exit()
