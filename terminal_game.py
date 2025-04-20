print("🌌 Welcome to Loop Galaxy Explorer!")
name = input("Enter your captain's name: ")
print(f"\nCaptain {name}, get ready to explore 5 mysterious planets in the galaxy...\n")

fuel = 5  # You can explore 5 planets (or iterations)
planet_number = 1

while fuel > 0:
    print(f"\n🪐 Planet {planet_number}")
    print("What would you like to do?")
    print("1. Explore the planet")
    print("2. Skip to the next one")
    print("3. Rest and observe from orbit")

    choice = input("Enter your choice (1/2/3): ")

    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ")

    if choice == '1':
        print("🔍 You explored the planet and found an alien artifact!")
    elif choice == '2':
        print("🚀 You skipped this planet.")
    else:
        print("🔭 You observed stunning celestial events from orbit.")

    planet_number += 1
    fuel -= 1

print("\n✨ Mission complete! You've explored the galaxy using nothing but loops!")
