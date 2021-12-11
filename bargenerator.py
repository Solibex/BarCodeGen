try:
    import random
except ImportError:
    print('Failed to import')
    print('Contact to Solibez!')
print_times = 1
barcode_length = 20
def generatebarcode() -> str:
    return ''.join(random.choice(["I", "l"]) for _ in range(barcode_length))
print(generatebarcode())
