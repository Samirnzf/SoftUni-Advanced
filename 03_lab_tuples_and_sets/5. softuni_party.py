number_of_guests = int(input())
regular_reservation = set()
vip_reservation = set()

for _ in range(number_of_guests):
    reservation = input()

    if reservation[0].isdigit():
        vip_reservation.add(reservation)
    else:
        regular_reservation.add(reservation)

guests_at_party = set()

while True:
    reservation_number = input()

    if reservation_number == "END":
        break

    guests_at_party.add(reservation_number)

all_guests = vip_reservation.union(regular_reservation)
absent_guests = all_guests.difference(guests_at_party)
sorted_absent_guests = sorted(absent_guests)

print(len(absent_guests))
sorted_absent_guests = sorted(absent_guests)
for guest in sorted_absent_guests:
    print(guest)
