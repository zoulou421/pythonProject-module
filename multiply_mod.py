"""multiply_mod module containing the table function"""
def table(nb, max=10):
 """Function displaying the multiplication table by number of
1 * nb up to max * n"""
 i = 0
 while i < max:
   print(i + 1, "*", nb, "=", (i + 1) * nb)
   i += 1