class Car:
    def __init__(self, color = None, type = None, year = None):
        self.color = color
        self.type = type
        self.year = year
        self.carState = 'Car is turned off'

    def launching(self):
        self.carState = 'Car is started'
        return print('Car has been started')

    def breaking(self):
        self.carState = 'Car is turned off'
        return print('Car has been stopped')

    def get_carState(self):
        return print(self.carState)

    def set_car_color(self, color):
        self.color = color

    def set_car_type(self, type):
        self.type = type

    def set_car_release(self, year):
        self.year = year

def main():
    honda = Car('black', 'sedan', 1990)
    honda.get_carState()
    honda.launching()
    honda.get_carState()

if __name__ == '__main__':
    main()


