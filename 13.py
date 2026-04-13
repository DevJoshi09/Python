# Decorator : A function that extends the behavirour of another function without modifying the base function

# decorator function
def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        sprinkles = input("Select sprinkles: 1.choclate, 2.vanilla, 3.tuttifruity :- ")
        
        print(f"you add {sprinkles} sprinkles...")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("you add fudge...")
        func(*args,**kwargs)
    return wrapper
    

# Decorator 
@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"here is your {flavour} ice cream...")


# call base function
get_ice_cream("choclate")