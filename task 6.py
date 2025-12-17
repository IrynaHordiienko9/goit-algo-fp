from functools import lru_cache

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    result = []
    for name, info in sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True):
        if info['cost'] <= budget:
            result.append(name)
            budget -= info['cost']
    return result


def dynamic_programming(items, budget):
    names = list(items)
    costs = [items[n]['cost'] for n in names]
    calories = [items[n]['calories'] for n in names]

    @lru_cache(None)
    def dp(i, b):
        if i == len(names) or b == 0:
            return 0, ()
        skip = dp(i+1, b)
        take = (0, ())
        if costs[i] <= b:
            calor, chosen = dp(i+1, b-costs[i])
            take = (calor + calories[i], chosen + (names[i],))
        return max(skip, take, key=lambda x: x[0])

    return list(dp(0, budget)[1])


budget = 100
print("Greedy (functional):", greedy_algorithm(items, budget))
print("Dynamic programming (recursion):", dynamic_programming(items, budget))
