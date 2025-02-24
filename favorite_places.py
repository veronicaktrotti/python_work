favorite_places={
    "mason": "Chicago",
    "liam": "New York",
    "chris": "Orlando"
}
for person in favorite_places:
    print("The favorite place of "+person+" is "+favorite_places[person]+".")
#version 2
favorite_places={
    "mason": ["Chicago","New York","Orlando"],
    "liam": ["Naples","Los Angeles","Washington DC"],
    "chris": ["Warsaw","Paris","London"]
}
for person in favorite_places:
    print(person+"'s favorite places are:")
    for place in favorite_places[person]:
        print(place)
        