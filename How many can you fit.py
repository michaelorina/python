# A shelf has x > 100 cm. Determine how many y < 15 cm product can you fit in it.

length = int(input('Enter the shelf length: '))
product = int(input('Enter the product size: '))

how_many_can_you_fit = length//product

print(f'for a shelf with {length} cm, you can fit {how_many_can_you_fit} products of {product} cm.')