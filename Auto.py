def auto_init(model, max_speed):
    return {
        'model': model,
        'max_speed': max_speed,
        'speed': 0,
        'engine': False
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('engine is working')


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
    else:
        print('slow down first')


def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        print(f'Your speed is {car["speed"]}')
    else:
        print('start engine first')


def slow_down(car, amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f'Your speed is {car["speed"]}')


fiat = auto_init('Tipo', 240)
bmw = auto_init('e46', 170)


def run(car):
    print(car)
    print(speed_up(car, 200))
    print(start_engine(car))
    print(speed_up(car, 200))
    print(stop_engine(car))
    print(slow_down(car, 270))
    print(stop_engine(car))


run(bmw)
