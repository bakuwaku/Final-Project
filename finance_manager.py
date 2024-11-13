""" Determining financial information regarding a users input.

Driver/Navigator: Shelly Parra, 
Assignment: Project
Date: 11/11/2024

Challenges Encountered: 
"""

class Person:
    """A user of the app who can track expenses, income, and savings."""

    def __init__(self, username: str):
        """Initializes the financial tracker with user details and empty lists for expenses, income, and savings.

        Args:
            username (str)
        """
        assert isinstance(username, str), "Username must be a string."
        assert username != "", "Username cannot be empty."

        self.username = username
        self.expenses = []
        self.income = 0.0
        self.savings = 0.0

    def register_user(self):
        """Registers a new user by setting initial financial information for the user."""
        assert hasattr(self, 'username'), "User must have a username."
        assert isinstance(self.expenses, list), "Expenses should be initialized as a list."
        assert isinstance(self.income, float), "Income should be initialized as a float."
        assert isinstance(self.savings, float), "Savings should be initialized as a float."

    def display_information(self):
        """Displays the financial information of the user."""
        print(f"Username: {self.username}")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Savings: ${self.savings:.2f}")
        print("Expenses:")
        for expense in self.expenses:
            print(f"- {expense}")

        
        assert self.income >= 0, "Income cannot be negative."
        assert self.savings >= 0, "Savings cannot be negative."
        assert all(isinstance(expense, (int, float)) and expense >= 0 for expense in self.expenses), \
            "All expenses must be non-negative numbers."

person = Person("Alice")
person.register_user()
person.display_information()
        
def want_add_expenses(self, amount: float, category: str):
    """Adds expenses to a list of desired purchases. Used when the person wants to track things they intend to spend money on, such as a new iphone or a trip to Dunkin' Donuts.

    Args:
        amount (float): Amount of money spent on desired expense.
        category (str): Description or category of the expense, such as entertainment or fast food 
        
    Raises:
        AssertionError: If amount is not a positive number or category is an empty string 
        """
    
def need_expenses
    """Adds essential expenses to a list of necessary spending. Used to track money spent on necessities, such as food, utilities, or housing

        Args:
        amount (float): The amount of money spent on necessary expense. 
        category (str): Description or category of the expense, such as "food," "electricity," or "housing."
    
        Raises:
        AssertionError: If amount is not a positive number or category is an empty string.
    """
