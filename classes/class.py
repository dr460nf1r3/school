#!/usr/bin/env python


class finances:
    """Defines the financial aspects of our real estate."""

    def __init__(self, total_price, price_per_sq, needs_fix, rent):
        self.needs_fix = needs_fix
        self.total_price = total_price
        self.price_per_sq = price_per_sq
        self.rent = rent

    def calc_rent(self, room_count, price_per_sq):
        self.rent = room_count * self.price_per_sq

    def calc_price_per_sq(self, total_price, size):
        self.price_per_sq = total_price / size


class owner:
    """Defines the owner data our real estate."""

    def __init__(self, name, address, telephone, email):
        self.address = address
        self.email = email
        self.name = name
        self.tel_number = email


class availability:
    """Defines the availability aspects of our real estate."""

    def __init__(self, move_in, on_market):
        self.move_in = move_in
        self.on_market = on_market


class real_estate:
    """Defines the general aspects of our real estate"""

    def __init__(
        self,
        name,
        address,
        size,
        description,
        room_count,
        floor_count,
        owner,
        availability,
        finances,
    ):
        self.address = address
        self.description = description
        self.floor_count = floor_count
        self.name = name
        self.room_count = room_count
        self.size = size

        self.room_sizes = []

    def add_room(self, room_size):
        self.room_sizes.append(room_size)


my_real_estate_1 = real_estate(
    "Real Home",
    "My street 42",
    200,
    "appartement",
    8,
    2,
    owner("Nico", "My street 1", "123456", "email@my.server"),
    availability(True, True),
    # finances(100000, finances.calc_rent(self, room_count, price_per_sq), False, 0),
)

my_real_estate_2 = real_estate(
    "Sweet Life", "Onlystreet 1", 90000, 68, "appartement", 3, 1
)


print(
    "The real estate has been created with the following information:"
    f"Name: {real_estate.name}"
    f"Address: {real_estate.address}"
    f"Price: {real_estate.price}"
    f"Size: {real_estate.size}"
    f"Description: {real_estate.description}"
    f"Room count: {real_estate.room_count}"
    f"Floor count: {real_estate.floor_count}"
)
