def announce(f): # takes input of function f and retuen a new function. This function will wrap up this function with additional behavior
    def wrapper():
        print("About to run the function...")
        f() # run the function f
        print("Done with the function.")
    return wrapper # return the new function wrapper

@announce # @ adds a decorator, takes hello() function as input to f
def hello():
    print("Hello, world!")

hello() # run the function hello