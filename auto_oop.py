class Auto:
    def __init__(self, model, max_speed):
        self.max_speed = max_speed
        self.model = model
        self.speed = 0
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('engine is working')
        return self.engine

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
        else:
            print('slow down first')
        return self.engine

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f'Your speed is {self.speed}')
        else:
            print('Start engine first')
        return self.speed

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f'Your speed is {self.speed}')
        return self.speed


class Van(Auto):
    def __init__(self, model, max_speed, seats=7):
        super().__init__(model, max_speed)
        self.seats = seats


fiat = Auto('Tipo', 240)
bmw = Auto('e46', 170)
ford = Van('Transit', 90)


def run(car):
    print(car.model, car.speed, car.max_speed, car.engine)
    print(car.speed_up(200))
    print(car.start_engine())
    print(car.speed_up(200))
    print(car.stop_engine())
    print(car.slow_down(270))
    print(car.stop_engine())


run(bmw)
print('----------------------')
print(Auto.start_engine(fiat))
print('----------------------')
run(ford)
