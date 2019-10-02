from product import Product


class Execution:
    item1 = Product(1, "Milk", 30)
    item2 = Product(2, "Bread", 40)
    item3 = Product(3, "Butter", 50)
    item4 = Product(4, "Egg", 50)

    def show_menu(self):
        print(self.item1.p_id, self.item1.name, self.item1.price)
        print(self.item2.p_id, self.item2.name, self.item2.price)
        print(self.item3.p_id, self.item3.name, self.item3.price)
        print(self.item4.p_id, self.item4.name, self.item4.price)

    list1 = []

    def cart(self):
        p_id = int(input("enter id"))
        if p_id == 1:
            self.list1.append(self.item1.name)
            self.list1.append(self.item1.price)
            print(self.item1.name, self.item1.price)
        if p_id == 2:
            self.list1.append(self.item2.name)
            self.list1.append(self.item2.price)
            print(self.item2.name, self.item2.price)
        if p_id == 3:
            self.list1.append(self.item3.name)
            self.list1.append(self.item3.price)
            print(self.item3.name, self.item3.price)
        if p_id == 4:
            self.list1.append(self.item4.name)
            self.list1.append(self.item4.price)
            print(self.item4.name, self.item4.price)
        choice = input("do u want to buy more items")
        if choice == 'y':
                self.cart()
        elif choice == 'n':
                pass

    def show_cart(self):
        print(self.list1)
        price = self.list1[1:len(self.list1):2]
        self.total_price = sum(price)
        print("total amount is", self.total_price)

    def billing(self):
        print("billed amount", self.total_price)
        paid_amount = int(input("enter amount u want to pay"))
        if paid_amount == self.total_price:
            print("THANKS FOR SHOPPING WITH US")
        elif paid_amount < self.total_price:
            due_amount = self.total_price-paid_amount
            print("YOUR PENDING AMOUNT IS:", due_amount)
            self.total_price = due_amount
            #print("total amount to be paid is:",self.total_price)
            self.billing()
        elif paid_amount > self.total_price:
            refund_amount = paid_amount - self.total_price
            print("AMOUNT REFUNDABLE IS:", refund_amount)


# obj = Execution()
# obj.show_menu()
# obj.cart()
# obj.show_cart()
# obj.billing()







