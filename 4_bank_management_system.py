from datetime import datetime, timedelta
import pytz

class TimeZone:
    def __init__(self, timezone_name, offset_hours, offset_minutes ):
        self.timezone_name = timezone_name
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes

    def offset(self):
        time_offset = timedelta(hours = self.offset_hours, minutes = self.offset_minutes)
        return time_offset

class Account:
    interest_rate = 0.005
    transaction_id = 0

    def __init__(self, account_number, first_name, last_name, time_zone = None, balance=0):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._time_zone = time_zone
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, amount):
        self._first_name = amount

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, amount):
        self._last_name = amount

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @property
    def balance(self):
        return self._balance
    
    # def display_balance(self):
    #     print(f"Current balance is {self._balance}.")

    def generate_confirmation_number(self,transaction_code):
        Account.transaction_id += 1
        time_utc = datetime.now(pytz.utc)
        local_time = time_utc + self._time_zone.offset()
        return f"{transaction_code}-{self.account_number}-{time_utc.strftime('%Y%m%d%H%M%S')}-{Account.transaction_id}"
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            #self.display_balance()
            confirmation_number = self.generate_confirmation_number('D')
            return confirmation_number

    def withdraw(self, amount):
        if self._balance >= amount and amount > 0:  
            self._balance -= amount
            #self.display_balance()
            confirmation_number = self.generate_confirmation_number('W')
            return confirmation_number
        else:
            confirmation_number = self.generate_confirmation_number('X')
            return confirmation_number

    def add_interest(self):
        balance_interest = self._balance * self.interest_rate
        self._balance += balance_interest
        #print(f"After adding interest rate {balance_interest}, current balance is {self._balance}")
        confirmation_number = self.generate_confirmation_number('I')
        return confirmation_number
    
    def return_confirmation_number(self, confirmation_number, time_zone = None):
        all_info = confirmation_number.split('-')
        transaction_code = all_info[0]
        account_number = all_info[1]
        parsed_utc_time = datetime.strptime(all_info[2], '%Y%m%d%H%M%S')
        utc_time = parsed_utc_time.strftime('%Y-%m-%dT%H:%M:%S')
        local_time = parsed_utc_time + timedelta(hours=time_zone) if time_zone else None
        transaction_id = all_info[3]
        return f"Transaction code: {transaction_code},\n \
                Account_number: {account_number},\n \
                Time UTC: {utc_time},\n \
                Local Time: {local_time},\n \
                Transaction ID: {transaction_id}"
    
        
account_time_zone = TimeZone(timezone_name='MST', offset_hours=4, offset_minutes=0)
account = Account(account_number="247045", first_name="Bob", last_name="Marley", balance=1000, time_zone = account_time_zone )

# Deposit
deposit_confirmation = account.deposit(700)
print("Deposit Confirmation:", deposit_confirmation)

# Withdraw
withdraw_confirmation = account.withdraw(300)
print("Withdraw Confirmation:", withdraw_confirmation)

# Withdraw (failed)
failed_withdraw_confirmation = account.withdraw(2000.0)
print("Withdrawal Confirmation:", failed_withdraw_confirmation)

# Interest
interest_confirmation = account.add_interest()
print("Interest Confirmation:", interest_confirmation)

confirmation_number = "D-247045-20240323193223-1"
time_zone = 4
parsed_confirmation = account.return_confirmation_number(confirmation_number, time_zone)
print("\nParsed information:\n",parsed_confirmation)

