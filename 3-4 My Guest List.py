guests = ['Denis', 'Babcia', 'Mama']
name = guests[0].title()
print(f"Hello {name}, would you like to come to dinner?")
name = guests[1].title()
print(f"Hello {name}, would you like to come to dinner?")
name = guests[2].title()
print(f"Hello {name}, would you like to come to dinner?")
print(f"\nfound a bigger table\n")
guests.insert(0, 'Chris')
guests.insert(int(len(guests)/2), 'Liam')
guests.append('Mason')
guests.sort()
print(guests)
print(f"\nHello {guests[0].title()}, would you like to come to dinner?")
print(f"Hello {guests[1].title()}, would you like to come to dinner?")
print(f"Hello {guests[2].title()}, would you like to come to dinner?")
print(f"Hello {guests[3].title()}, would you like to come to dinner?")
print(f"Hello {guests[4].title()}, would you like to come to dinner?")
print(f"Hello {guests[5].title()}, would you like to come to dinner?")
