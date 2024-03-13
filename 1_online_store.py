class Product:
    def __init__(self,product_id,product_name,price,inventory_count):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.inventory_count = inventory_count


    def apply_discount(self,discount_percentage):
        self.price -= self.price * discount_percentage / 100


    def sell(self,quantity):
        self.inventory_count -= quantity


class DynamicPricing:
    def modified_price(self,product,new_price):
        product.price = new_price


product = Product(1,"Book",7000,30)

product.apply_discount(20)
print("The price after discount:",product.price)

product.sell(7)
print("Inventory count of product1 after selling 7:", product.inventory_count)

dyn_pricing = DynamicPricing()
dyn_pricing.modified_price(product,1300)
