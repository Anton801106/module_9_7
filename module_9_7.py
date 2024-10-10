# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_ = func(*args, **kwargs)
        for i in range(2, int(sum_ + 1) // 2):
            if sum_ % 2 == 0 and sum_ % i != 0:
                res = 'Простое'
            else:
                res = 'Составное'
        return res

    return wrapper

@is_prime
def sum_three(*args, **kwargs):
    print(sum(args))
    return sum(args)

result = sum_three(2, 3, 6, 5, 8.8)
print(result)
