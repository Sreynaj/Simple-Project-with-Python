class Bar:
    menu = {
        # item and its price
        'wine': 10,
        'beef': 5,
        'soft drink': 5,
        'chicken': 10,
    }
    print("Here are the items we have in stock for you!\n",menu)

    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.totalPrice = 0
        self.items = []

    def add(self):
        while True:
            item = input("What do you want to pick?:")
            if item in self.menu:
              self.items.append(item)
              self.totalPrice += self.menu[item]
            else:
               print(f"{item} is not available.")
            print("Will you pick another item?")
            answer = input("For 'Yes' press '1' for 'No' press '0'")
            if answer == '1':
              continue
            elif answer == '0':
              break
            else:
              print("Not in the option!")
            

    def print_bill(self):
        service = int(input("Service charge $?: "))
        service = (service / 100) * self.totalPrice
        totalPrice = self.totalPrice + service

        print(f" Name: {self.name}")

        for item in self.items:
            print(f'{item} ${self.menu[item]}')
        print(f'Total Price = ${totalPrice}')
        print("Thank You!!")



customer = Bar()
customer.add()
customer.print_bill()
