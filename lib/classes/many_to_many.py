class Coffee:

    all = []

    def __init__(self, name):
        if (isinstance(name, str) and len(name) >= 3):
            self._name = name
            Coffee.all.append(self)
        else:
            raise Exception

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (hasattr(self, self._name)):
            if (isinstance(name, str) and len(name) >= 3):
                self._name = name
            else:
                raise Exception
        else:
            raise Exception

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee is self]))

    def num_orders(self):
        return len(self.orders()) if len(self.orders()) > 0 else 0

    def average_price(self):
        prices = [order.price for order in Order.all if order.coffee is self]
        gross_price = 0
        for price in prices:
            gross_price += price
        return float(gross_price / len(prices))


class Customer:

    all = []

    def __init__(self, name):
        if (isinstance(name, str) and 3 < len(name) < 15):
            self._name = name
            Customer.all.append(self)
        else:
            raise Exception

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (not hasattr(self, self._name)):
            if (isinstance(name, str) and 3 < len(name) < 15):
                self._name = name
            else:
                raise Exception
        else:
            raise Exception

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer is self]))

    def create_order(self, coffee, price):
        if (isinstance(coffee, Coffee) and (isinstance(price, float) and 1.0 < price < 10.0)):
            return Order(self, coffee, price)
        else:
            raise Exception

    @classmethod
    def most_aficionado(cls, coffee):
        if (isinstance(coffee, Coffee)):
            who_bought = [
                order for order in Order.all if order.coffee == coffee]
            who_bought_what = {}
            for order in who_bought:
                if (order.customer in who_bought_what):
                    who_bought_what[order.customer] += float(order.price)
                else:
                    who_bought_what[order.customer] = float(order.price)
            customers = list(who_bought_what.keys())
            total_spent = list(who_bought_what.values())
            return customers[total_spent.index(max(total_spent))]
        else:
            raise Exception


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        if (isinstance(price, float) and 1.0 < price < 10.0):
            self._price = price
            Order.all.append(self)
        else:
            raise Exception

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (not hasattr(self, '_price')):
            if (isinstance(price, float) and 1.0 < price < 10.0):
                self._price = price
            else:
                raise Exception
        else:
            raise Exception

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
