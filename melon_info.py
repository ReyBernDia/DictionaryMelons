"""Print out all the melons in our inventory."""



from melons import melons


def print_melon(melon):
    """Print each melon with corresponding attribute information."""

    for melon_name, info in melons.items():
        print(melon_name.upper())

        for info, value in info.items():
            print(f"{info}: {value}")

        print('===================================')

print_melon(melons)
