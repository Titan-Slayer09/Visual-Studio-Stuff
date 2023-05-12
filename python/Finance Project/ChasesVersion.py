"""current goals include: 
1. DONE
2. Add more news options! (such as a news option that randomly boosts or drops multiple stocks at once)
3. allow players to buy things, like houses and cars and stuff
4. allow player to use things like crypto in a fluctuating market.
5. Create a way to see their Net Worth (their money in all even tied up in houses, cars, crypto, or stock)
6. make the list of stocks you own only show companies you have money in
7. When you check your stock portfolio, it should tell you if you are overall 
                                                    gaining or loosing money since your last check
                                                    
*IMPORTANT CHANGE I WANT TO MAKE WITH THE NEWS and other stuff*
    instead of having companies randomly go up and down the headlines should instead be like 
    'It is going to be A good week for _______' then instead of having "option 1." be check your money, 
    1 will instead be advance to next day, every day you make 10 dollars passively (which can be increased later)
    and the stock markets will randomly increase (or decrase depending on the headline) for that week and every 
    company will get a headline per (length of time), also the length of time should vary.
Good Luck!
"""

from time import time
import random

class Company:
    '''Create a company that can hold stocks'''
    
    def __init__(self, name:str, base_stock_price:float):
        self.name = name
        self.stock_price = base_stock_price
        self.stocks = 0
        
    def update_stocks(self, change_amount:float):
        '''Update Stocks by a float 
        (Add or subtract to corrent cost)'''
        
        self.stock_price += change_amount
    
    def buy_stocks(self, update_stocks:int):
        '''Update Stocks to buy or sell them'''
        self.stocks += update_stocks

# Initialize Varibles
cash = 500.00
cash_per_day = 10
day = 1
changing = [0, 0, 0, 0] # Name, Days Left, Amount Per Day
reference_news = ['Good', 'Great', 'Bad', 'Terrible']

# Stocks
companies = []
# Semi-Real values right now
companies.append(Company('Amazon', round(random.uniform(90.00, 170.00), 2))) # Create Amazon
companies.append(Company('Walmart', round(random.uniform(100.00, 160.00), 2))) # Creat Walmart
companies.append(Company('Microsoft', round(random.uniform(0.00, 500.00), 2))) # Create Microsoft
companies.append(Company('Publix', round(random.uniform(50.00, 100.00), 2))) # Create Publix
companies.append(Company("McDonald's", round(random.uniform(200.00, 350.00), 2))) # Create McDonald's
companies.append(Company('Tesla', round(random.uniform(1000.00, 2000.00), 2))) # Create Tesla
companies.append(Company('Dow Jones Industrial', round(random.uniform(28000.00, 35000.00), 2))) # Create Dow Jones
companies.append(Company('Meta', round(random.uniform(89.00, 325.00), 2))) # Create Meta
companies.append(Company('Advanced Micro Devices (AMD)', round(random.uniform(55.00, 120.00), 2))) # Create AMD
companies.append(Company('Netflix', round(random.uniform(292.00, 385.00), 2))) # Create Netflix

# Game Loop
while True:
    start_time = time()
    
    print('What would you like to do?')
    print('1. Go to next day') 
    print('2. Look at the stock Market')
    print('3. Look at the news')
    print('4. Look at your stocks ')
    print('5. Check your money')
    user_input = input('')
    print()

    match user_input:

        # Go to next day
        case '1':
            
            if changing[1] > 0:
                
                match changing[2]:       
                    case 1:
                        companies[changing[0]].update_stocks(round(random.uniform(0, 1.50), 2))
                    
                    case 2:
                        companies[changing[0]].update_stocks(round(random.uniform(0, 10.50), 2))
                    
                    case 3:
                        companies[changing[0]].update_stocks(round(random.uniform(0, -1.50), 2))
                    
                    case 4:
                        companies[changing[0]].update_stocks(round(random.uniform(0, -10.50), 2))
                
                changing[1] -= 1
            
            cash += cash_per_day
            
            if day % 7 == 0:
                for y, x in enumerate(companies):
                    companies[y].update_stocks(round(random.uniform(-0.50, 0.50), 2))
            
            day += 1

        # Investing In Stocks
        case '2':
            # Updating the cash 
            print(f'You have: ${cash}')
            print()

            #stock Market stuff
            print("Some stocks that are out right now: ")

            for y, x in enumerate(companies):
                print(f'{y + 1}. The company {x.name} has a current stock value of {x.stock_price}')
            print()

            invest = input('Would you like to invest? y/n: ')
            if invest == 'y':

                company = int(input("What company would you like to invest in? "))

                # Checks if Valid Company
                if company > len(companies) or company < 1:
                    print('Invalid Company')

                else:
                    buy_or_no = input(f"Would You Like to Buy a {companies[company - 1].name} Stock for {companies[company - 1].stock_price} y/n: ")
                    
                    if buy_or_no == 'y':
                        if cash > companies[company - 1].stock_price:

                            amount = int(input(f"How many {companies[company - 1].name} stocks would you like to buy? "))

                            if amount * companies[company - 1].stock_price <= cash:
                                cash -= companies[company - 1].stock_price * amount
                                companies[company - 1].buy_stocks(amount)
                                print()
                                print(f'You now have {companies[company - 1].stocks} stocks in {companies[company - 1].name}')

                            elif amount * companies[company - 1].stock_price > cash:
                                print("You can't afford that many Amazon Stocks")
                            
                        else:
                            print(' you can\'t afford one right now! ')
                    
                    else:
                        print(f'You do not buy {companies[company - 1].name}')

            # Nothing happens
            else:
                print('Just looking today I see.')
                
        # Watch the News
        case '3':
            if changing[1] > 0:                       
                print(f'{companies[changing[0]].name} is going to do {reference_news[changing[2] - 1]} over the the next {changing[1]} days')
                
            elif changing[2] == 5:
                print('You see the news, nothing is happening')
                
            else:    
                news = random.randint(1, len(companies))

                match random.randint(1,5):

                    # Good
                    case 1:
                        print(f'You see the news, looks like the company {companies[news - 1].name} has Released a new product that is going well!')

                        changing = [news - 1, random.randint(4, 7), 1]

                    # Really Good
                    case 2:
                        print(f'You see the news, looks like the company {companies[news - 1].name} has a released a new product that is going really well!')

                        changing = [news - 1, random.randint(2, 10), 2]

                    # Nothing happens
                    case 3:
                        print('You see the news, nothing is happening')
                        changing = [0, 0, 5]

                    # Bad
                    case 4:
                        print(f'you see the news, looks like the company {companies[news - 1].name} is loosing money on some projects')

                        changing = [news - 1, random.randint(4, 7), 3]

                    # Really bad
                    case 5:
                        print(f'you see the news, looks like the company {companies[news - 1].name} has workers on strike!')

                        changing = [news - 1, random.randint(2, 10), 4]

        # Look at Your Stocks
        case '4':
            total = 0

            for x in companies:
                print(f"You have {x.stocks} stocks in {x.name} worth $" + str(x.stocks * x.stock_price))

                total += x.stocks * x.stock_price
            print()
            print(f"Your total stock portfolio value is ${total}")
            print()

            sell = input("would you like to sell any stock? y/n ")

            if sell == 'y':
                print('You can sell')

                for y, x in enumerate(companies):
                    print(f'{y + 1}. {x.name}')
                
                print()
                which_one = input('Which Do You Sell? ')

                try:
                    which_one = int(which_one)
                except:
                    print('Sorry, You Must Choose A Number')

                if which_one > len(companies) or which_one < 1:
                    print('Invalid Company')

                else:
                    how_many = int(input(f'How many do you want to sell? '))
                    
                    if how_many > companies[which_one - 1].stocks:
                        print('You don\'t have that many stocks in WallMart!')
                    elif how_many <= companies[which_one - 1].stocks:
                        print(f"You sold {how_many} stocks in {companies[which_one - 1].name}")

                        cash += how_many * companies[which_one - 1].stock_price
                        companies[which_one - 1].buy_stocks(how_many * -1)
        
        # Check Money              
        case '5':
            # Updating cash and showing the user their balance
            print(f'You have: ${cash}')
            
    print()