#Below is the solution the Checkout Kata problem(Kata09) 

class Checkout:
    def __init__(self, rules):
        self.rules = rules
        self.items = {}

    def scan(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calcTotal(self):
        total = 0
        for item, quantity in self.items.items():
            item_rules = self.rules.get(item, {})
            uPrice = item_rules.get('uPrice', 0)
            sPrice = item_rules.get('sPrice', {})
            if sPrice and quantity >= sPrice.get('quantity', 0):
                total += sPrice.get('price', 0) * (quantity // sPrice['quantity'])
                quantity = quantity % sPrice['quantity']
            total += uPrice * quantity
        return total


rules = {
    'A': {'uPrice': 70, 'sPrice': {'quantity': 3, 'price': 180}},
    'B': {'uPrice': 50, 'sPrice': {'quantity': 3, 'price': 140}},
    'C': {'uPrice': 30},
    'D': {'uPrice': 45},
}

co = Checkout(rules)

co.scan('A')
co.scan('B')
co.scan('A')
co.scan('C')
co.scan('D')

total = co.calcTotal()
print(f"Total price: {total}")
