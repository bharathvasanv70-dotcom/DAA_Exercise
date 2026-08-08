def first_fit(items, capacity=1.0):
    bins = []
    contents = []

    for item in items:
        placed = False

        for i in range(len(bins)):
            if bins[i] >= item:
                bins[i] -= item
                contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(capacity - item)
            contents.append([item])

    return contents


def first_fit_decreasing(items, capacity=1.0):
    items = sorted(items, reverse=True)
    return first_fit(items, capacity)


def best_fit_decreasing(items, capacity=1.0):
    items = sorted(items, reverse=True)

    bins = []
    contents = []

    for item in items:
        best_index = -1
        best_space = float('inf')

        for i in range(len(bins)):
            if bins[i] >= item and bins[i] - item < best_space:
                best_space = bins[i] - item
                best_index = i

        if best_index != -1:
            bins[best_index] -= item
            contents[best_index].append(item)
        else:
            bins.append(capacity - item)
            contents.append([item])

    return contents


def display_bins(name, bins):
    print(f"\n{name}: {len(bins)} bins")

    for i, b in enumerate(bins, 1):
        used = sum(b)
        print(f"Bin {i}: {b} | Used: {used:.1f}")


items = [0.5, 0.7, 0.3, 0.9, 0.2,
         0.6, 0.8, 0.4, 0.1, 0.5]

capacity = 1.0

print("Items:", items)
print("Capacity:", capacity)
print("Sum of items:", sum(items))
print("Lower Bound:", int((sum(items) + capacity - 1) // capacity))

ff = first_fit(items, capacity)
ffd = first_fit_decreasing(items, capacity)
bfd = best_fit_decreasing(items, capacity)

display_bins("First Fit (FF)", ff)
display_bins("First Fit Decreasing (FFD)", ffd)
display_bins("Best Fit Decreasing (BFD)", bfd)

print("\nSummary:")
print("FF =", len(ff))
print("FFD =", len(ffd))
print("BFD =", len(bfd))