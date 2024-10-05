def is_valid_plate(plate):
    if len(plate) < 2 or len(plate) > 6:
        return "Invalid"
    
    if not plate[0].isalpha() or not plate[1].isalpha():
        return "Invalid"

    num_part = False
    for i in range(2, len(plate)):
        if plate[i].isdigit():
            if num_part == False:
                if plate[i] == '0':
                    return "Invalid"
                num_part = True
        elif num_part == True:
            return "Invalid"

    for char in plate:
        if char in "IOQU" and not char in ["I", "O", "Q", "U"]:
            return "Invalid"

    return "Valid"

print(is_valid_plate("AAA222"))  # Valid
print(is_valid_plate("AAA22A"))  # Invalid
print("Good is ",is_valid_plate("GOOD"))    # Invalid
print(is_valid_plate("AB123"))   # Valid
print(is_valid_plate("A01234"))  # Invalid
print(is_valid_plate("TOY22"))   # Valid
print(is_valid_plate("CAR0"))    # Invalid
