price   = float(input())
quantity   = float(input())
num   = float(input())
sub=price*quantity
dis=sub*num/100
tot=sub - dis
print(f"{"subtotal":<10} {sub:>6.2f}")
print(f"{"discount":<10} {dis:>6.2f}")
print(f"{"total"} {tot:>6.2f}")
