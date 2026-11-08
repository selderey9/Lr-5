encoded_str = (input("Enter your string: "))
decoded_str = ""
current_num = ""
for char in encoded_str:
    if char.isdigit():
        current_num += char
    else:
        if current_num:
            count = int(current_num)
        else:
            count = 1
        decoded_str += char * count
        current_num = ""
print("Data:")
print(decoded_str)
