def luau(name):
    # This main function, 'luau', acts like a factory.
    # It takes one word, 'name' (like "Nigga").

    def outer_function(func):
        # This is the actual function that will be created and named 'name' later.
        # It takes another function (a 'callback') as its input, called 'func'.
        
        # This is the key action: it immediately calls the input function ('func')
        # and passes the original word ('name') as an argument to it.
        func(name)

    # This line is where the magic happens!
    # 'globals()' is a special dictionary in Python that holds ALL global variable names.
    # We add a NEW entry to this dictionary, using the input 'name' (e.g., "Nigga")
    # as the key. The VALUE is the 'outer_function' we just defined.
    # This effectively creates a new function named "Nigga" that can be called anywhere!
    globals()[name] = outer_function


# 1. We call our factory function 'luau' and give it the word "Nigga".
#    This makes a NEW function available globally, now named 'Nigga'.
luau("Nigga")

# 2. We now call the new function, 'Nigga', just like in the Luau example.
#    We pass it an 'anonymous function' (a 'lambda') as its only argument.
#    The 'lambda id: (...)' is the function that 'Nigga' will call back.
#    The variable 'id' will receive the string "Nigga" from inside the 'luau' logic.
Nigga(lambda id: (
    # The 'id' variable is "Nigga" here.
    print(id + "same for py"),
    
    # We run the second print command.
    print("bit harder to do if u got less knowledge in lua"),
))
