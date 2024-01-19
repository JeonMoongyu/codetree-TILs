class Product:
    def __init__(self, name=0, code=0):
        self.name = name
        self.code = code

prod1 = Product()
prod2 = Product()

prod1.name = "codetree"
prod1.code = 50

name, code = input().split()
prod2.name = name
prod2.code = int(code)

print(f"product {prod1.code} is {prod1.name}")
print(f"product {prod2.code} is {prod2.name}")