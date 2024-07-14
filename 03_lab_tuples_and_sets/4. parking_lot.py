number_of_cars = int(input())

parking_lot = set()

for _ in range(number_of_cars):
    action, plate_number = input().split(', ')

    if action == 'IN':
        parking_lot.add(plate_number)

    elif action == 'OUT':
        parking_lot.remove(plate_number)

if len(parking_lot) < 1:
    print("Parking Lot is Empty")
else:
    for plate_number in parking_lot:
        print(plate_number)
