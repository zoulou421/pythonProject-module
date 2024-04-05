"""module multipli contenant la fonction table"""
import os


def table_internal_module(nb, max=10):
    """multiply_module module containing the table function// but tested in same file not exported"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
# table function test
if __name__ == "__main__":
    table_internal_module(4)
os.system("pause")
