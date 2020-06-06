class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('O restaurante ' + self.restaurant_name.title() + ' tem uma cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('O restaurante ' + self.restaurant_name.title() + ' está aberto!')

restaunt = Restaurant('Ragazzo', 'organizada')
restaunt.describe_restaurant()
restaunt.open_restaurant()