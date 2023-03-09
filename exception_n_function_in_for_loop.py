def create_groups(items, n):
    try:
        size = len(items) // n
    except ZeroDivisionError as e:
        print("WARNING: Please use a nonzero number. Error returned is {}".format(e))
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(n))

print("Creating 6 groups...")
for group in create_groups(range(64), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))