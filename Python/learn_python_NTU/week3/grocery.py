d = {}
def grocery():
    while True:
        try:
            item = input().strip().upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            sorted_d = {k: d[k] for k in sorted(d.keys())}
            # sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
            for key, value in sorted_d.items():
                print(f"{value} {key}")
            break
grocery()