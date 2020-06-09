import module

# When you want to import a module file within a package(folder)
# Write the name of the package(folder) followed by a dot and then the module name
import shopping.shopping_cart

# To reference it we also have to write it the same way e.g.
# from shopping package(folder) and shopping.py file, and buy function, add apple
print(shopping.shopping_cart.buy("apple"))
