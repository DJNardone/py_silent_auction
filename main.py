from replit import clear
from art import logo

bidder = {}
more_bidding = False
while not more_bidding:
    def add_bidder(name, bid):
        bidder[name] = bid

    print(logo)
    print("Welcome to the Secret Auction program!")   
    name = input("Hello Bidder! What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bidder(name, bid)
    
    go_again = input("Is anyone else bidding? 'yes' or 'no'\n").lower()
    if go_again == "yes":
        clear()
    else:
        more_bidding = True
        high_bid = 0
        for highest in bidder:
            if bidder[highest] > high_bid:
                high_bid = bidder[highest]
                winner = highest
        print(f"Congratulations! {winner} has won with a bid of ${high_bid}!")
       
        
            
        