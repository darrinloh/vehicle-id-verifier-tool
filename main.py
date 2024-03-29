import string

map_checksum = {
    0: "A",
    1: "Z",
    2: "Y",
    3: "X",
    4: "U",
    5: "T",
    6: "S",
    7: "R",
    8: "P",
    9: "M",
    10: "L",
    11: "K",
    12: "J",
    13: "H",
    14: "G",
    15: "E",
    16: "D",
    17: "C",
    18: "B",
}
def process_combination(combination):
    if str.isalpha(combination[:3]):
        processed = combination[1:]
    elif str.isalpha(combination[:2]):
        processed = combination
    else:
        processed = '@' + combination

    zero_padding = 7 - len(processed)
    processed = processed[:2] + str('0' * zero_padding) + processed[2:]
    return processed


def validate_combinations(combinations):
    valid_combinations = []
    for combination in combinations:
        processed_combination = process_combination(combination)

        sum = 0
        sum += (ord(processed_combination[0]) - ord('@')) * 9
        sum += (ord(processed_combination[1]) - ord('@')) * 4

        sum += int(processed_combination[2]) * 5
        sum += int(processed_combination[3]) * 4
        sum += int(processed_combination[4]) * 3
        sum += int(processed_combination[5]) * 2

        mod = sum % 19
        checksum = map_checksum[mod]
        if checksum is processed_combination[6]:
            valid_combinations.append(combination)
    return valid_combinations


alphabet = string.ascii_uppercase
numbers = list(range(10))


def generate_combinations(vehicle_id):
    possible_license_id = []
    missing_letters_index = []
    missing_numbers_index = []
    for index in range(len(vehicle_id)):
        if vehicle_id[index] == '*':
            missing_letters_index.append(index)
        if vehicle_id[index] == '_':
            missing_numbers_index.append(index)

    for index in missing_letters_index:
        possible_license_id = generate_alphabet_combination(possible_license_id, vehicle_id, index)
    for index in missing_numbers_index:
        possible_license_id = generate_number_combination(possible_license_id, vehicle_id, index)
    return possible_license_id

def generate_alphabet_combination(possible_license_ids, license_id, index):
    new_possible_license_ids = []
    if len(possible_license_ids) == 0:
        for letter in alphabet:
            temp_string = license_id[:index] + letter + license_id[index+1:]
            new_possible_license_ids.append(temp_string)

    for id_ in possible_license_ids:
        for letter in alphabet:
            temp_string = id_[:index] + letter + id_[index+1:]
            new_possible_license_ids.append(temp_string)
    return new_possible_license_ids


def generate_number_combination(possible_license_ids, license_id, index):
    new_possible_license_ids = []
    if len(possible_license_ids) == 0:
        for number in numbers:
            temp_string = license_id[:index] + str(number) + license_id[index+1:]
            new_possible_license_ids.append(temp_string)

    for id_ in possible_license_ids:
        for number in numbers:
            temp_string = id_[:index] + str(number) + id_[index+1:]
            new_possible_license_ids.append(temp_string)
    return new_possible_license_ids


def main():
    vehicle_id = input("Enter vehicle id: ")
    if vehicle_id == "":
        print("doesn't exist")
        return
    vehicle_type = input("Enter vehicle type (bike, car): ")
    if vehicle_type not in ("bike", "car"):
        print("wrong input, doesn't exist")
        return
    
    if vehicle_type == "car":
        combinations = generate_combinations(vehicle_id)
        valid_combinations = validate_combinations(combinations)
        print(valid_combinations)

if __name__ == "__main__":
    main()
