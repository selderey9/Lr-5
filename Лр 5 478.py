count = 0
while True:
    d_or_w = input("d or w or click space to finish:")
    d_or_w_lower = d_or_w.lower()
    if d_or_w_lower == "d":
        money = int(input("D: "))
        count = count + money
    elif d_or_w_lower == "w":
        money = int(input("W: "))
        count = count - money
    elif d_or_w_lower == " ":
        print("process is finished")
        break
    print("Your current balance:", count)
    d_or_w = None
