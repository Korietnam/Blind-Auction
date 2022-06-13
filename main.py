from art import logo

restart = True
bidders = {}

while restart == True:
  print(logo)
  bidder_name = input("What is your name? ")
  bidder_bid = int(input("What is your bid? $"))
  bidders[bidder_name] = bidder_bid
  add_another_user = input("Are there other users who want to bid? (Yes or No) ").lower()
  if add_another_user == "no":
    restart = False
    name = "name"
    bid = 0
    for each_bid in bidders:
      bid_amount = bidders[each_bid]
      if bid_amount > bid:
        name = each_bid
        bid = bid_amount
    print("\n" * 80)
    print(logo)
    print(f"The highest bid goes to {name} with a bid of ${bid}!")
  elif add_another_user == "yes":
    restart = True
    print("\n" * 80)
  else:
    add_another_user = input("Are there other users who want to bid? (Yes or No) ").lower()
    print("\n" * 80)