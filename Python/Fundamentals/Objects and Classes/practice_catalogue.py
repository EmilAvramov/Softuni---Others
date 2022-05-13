class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        result_list = [product for product in self.products if product.startswith(first_letter)]
        return result_list

    def __repr__(self):
        result = "Items in the {0} catalogue:\n" \
                "{1}".format(self.name, '\n'.join(sorted(self.products)))
        return result
