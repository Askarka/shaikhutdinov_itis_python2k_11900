import random
from pprint import pprint


def generate_table_of_views():
    users = []
    for i in range(10):
        user = []
        for j in range(10):
            user.append(random.randint(0, 1))
        users.append(user)
    return users


def compare_vectors(vector_1, vector_2):
    crossing = 0
    for i in range(10):
        if vector_1[i] == vector_2[i]:
            crossing += 1
    return 2 * (crossing / 20)


def create_table_of_matches(table_of_views):
    comparisons = []
    for i in range(10):
        comparison = []
        for j in range(10):
            if i == j:
                val = '-'
            else:
                val = compare_vectors(table_of_views[i], table_of_views[j])
            comparison.append(val)
        comparisons.append(comparison)
    return comparisons


print('Table of views:')
table_1 = generate_table_of_views()
pprint(table_1)

print('Table of matches:')
pprint(create_table_of_matches(table_1))
