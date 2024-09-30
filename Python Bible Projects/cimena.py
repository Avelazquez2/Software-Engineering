films = {
    "Finding Dory": [3,2],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
}
keys = list(films.keys())

while True:
    print("="*20)
    print("Current Playing:")
    for x in keys:
        print(x)
    print("="*20)
    choice = input("\nWhat movie do you want to watch?: ").strip().title()

    # check choice
    if choice in films:
        # check age
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            # check seats
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!\n")
        else:
            print("You are too young to view the film.\n")
    else:
        print("Movie is not currently playing. Please pick from the currently playing movies :)\n")
            
    
        
