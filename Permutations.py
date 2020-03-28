def permutations(strin):
    from itertools import permutations
    import re

    arr= set(permutations(strin))
    arr2= {strin}
    for entry in arr:
        arr2.add(re.sub(r"\(|'|\)|,| ", "", str(entry)))

    return arr2


print(permutations("aabb"))