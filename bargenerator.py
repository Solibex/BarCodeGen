try:
    import random
except ImportError:
    print('Failed to import')
    print('Contact to Solibez!')
def generatebarcode(x=20) -> str:
    return ''.join(random.choice(["I", "l"]) for _ in range(x))
# How to use
# print(generatebarcode)