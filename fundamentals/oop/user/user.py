class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print('\n',
            self.first_name,'\n',
            self.last_name,'\n',
            self.email,'\n',
            self.age,'\n',
            self.is_rewards_member,'\n',
            self.gold_card_points,'\n'
        )
    
    def enroll(self):
        if self.is_rewards_member == True:
            print(f'{self.first_name} is already a member! No need to re-enroll.')
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
    
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print(f'You have {self.gold_card_points} gold card points remaining. You have insufficient funds to spend {amount}. Please add more points. ')
        else:
            self.gold_card_points -= amount
    







rando1 = User('rando1', 'rando1', 'randoEmail@email.com', 28)
rando2 = User('rando2', 'rando2', 'randoEmail2@email.com', 82)
rando3 = User('rando3', 'rando3', 'randoEmail3@email.com', 100)

rando1.enroll()
rando1.spend_points(50)
rando2.enroll()
rando2.spend_points(80)
rando1.enroll()

rando1.display_info()
rando2.display_info()
rando3.display_info()

rando3.spend_points(40)