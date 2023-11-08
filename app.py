import sys
from src.calc import apply_vat

vat_free_price = sys.argv[1]
percent = sys.argv[2]

new_price = apply_vat(vat_free_price, percent)

print(new_price)
