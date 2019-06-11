import json

file = open("skychallenge_accounting_input.txt", 'r')
data = file.read()
parsed = json.loads(data)


def find_int(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, int) and isinstance(v, int):
                yield k, v
            elif isinstance(k, int):
                yield k
            elif isinstance(v, int):
                yield v
            else:
                yield from find_int(v)
    elif isinstance(obj, int):
        yield obj
    elif isinstance(obj, list):
        for item in obj:
            if not isinstance(obj, int):
                yield from find_int(item)
            else:
                yield item


rec_func = find_int(parsed)


result = 0
for i in rec_func:
    result += i

print(result)