import art

move_on = True
bids_dictionary = {}

def find_highest_bid(bids):
    print("\n" * 100)
    highest_bid = 0
    highest_bidder = ""
    for key, value in bids.items():
        working_value = int(value)
        if highest_bid < working_value:
            highest_bid = working_value
            highest_bidder = key
        else:
            continue

    print(f"The highest bid is {highest_bidder} with ${highest_bid}.")

while(move_on):
    print(art.logo)
    current_name = input("What is your name?\n")
    print(f"Welcome {current_name}!\n")
    current_bid = input("What would you like to bid? \n$")
    bids_dictionary[current_name] = current_bid
    is_next = input("Are there more bids? Y/n\n")

    if(is_next == "Y"):
        print("\n" * 100)
    elif(is_next == "n"):
        move_on = False
    else:
        print("Try again")

find_highest_bid(bids_dictionary)






