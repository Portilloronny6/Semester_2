def calculate(data, findall):
    matches = findall(r"([abc])([+-]?=)([abc])?([+-]?\d+)?")
    for v1, s, v2, n in matches:
        if n == "":
            n = 0
        if s == "=" and v2 == "":
            data[v1] = int(n)
        elif s == "=" and v2 != "":
            data[v1] = data[v2] + int(n)
            print("eee")
        elif s == "+=" and v2 == "":
            data[v1] += int(n)
        elif s == "+=" and v2 != "":
            data[v1] += data[v2] + int(n)
        elif s == "-=" and v2 == "":
            data[v1] -= int(n)
        elif s == "-=" and v2 != "":
            data[v1] -= data[v2] + int(n)
    return data
