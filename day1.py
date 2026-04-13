data = [10, None, 20, 10, "", 30, None, 40]

clean_list = []
seen = set()
removed = 0

for x in data:
    if not x or x in seen:
        removed += 1
        continue
    seen.add(x)
    clean_list.append(x)

print("Clean List:", clean_list)
print("Removed Count:", removed)