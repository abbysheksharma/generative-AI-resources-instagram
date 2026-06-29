# L → Local
# E → Enclosing
# G → Global
# B → Built-in
name = "Abhishek"
def greet():
    
    print(name)

greet()
print(name)

def outer():
    name = "Abhishek"
    def inner():
        print(name)
    inner()

outer()