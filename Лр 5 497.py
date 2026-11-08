while True:
    try:
        a = input("Enter your String")
        b = input("Enter your Substring:")
    except EOFError:
        break
    positions = []
    start = 0
    while True:
        pos = a.find(b, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    if len(positions) > 0:
        print(*positions)
    else:
        print(-1)