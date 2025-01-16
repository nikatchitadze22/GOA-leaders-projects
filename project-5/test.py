import math

count = 5
while count > 0:
    user_input = input("""Choose sides:
    a/b
    a/c
    b/c > """)

    if user_input.lower() == "ab" or user_input == "a/b":
        input_a = int(input("Enter the length of side a> "))
        input_b = int(input("Enter the length of side b> "))
        side_c = input_a ** 2 + input_b ** 2
        result_1 = math.sqrt(side_c)

        print("side (c) is " + str(result_1))
        break

    elif user_input.lower() == "ac" or user_input == "a/c":
        input_a2 = int(input("Enter the length of side a> "))
        input_c = int(input("Enter the length of side c> "))
        side_b = input_c ** 2 - input_a2 ** 2
        result_2 = math.sqrt(side_b)

        print("side (b) is " + str(result_2))
        break

    elif user_input == "bc" or user_input == "b/c":
        input_b2 = int(input("Enter the length of side b> "))
        input_c2 = int(input("Enter the length of side c> "))
        side_a = input_c2 ** 2 - input_b2 ** 2
        result_3 = math.sqrt(side_a)

        print("side (a) is " + str(result_3))
        break
        
    else:
        print("Invalid option. Please try again.")
        count -= 1
        print(f"you have {count} tries left")

