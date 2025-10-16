-- local function luau(name)
-- This function acts as a factory, dynamically creating another function.
local function luau(name)
    -- getfenv() is a special function in Luau (and Lua 5.1) that returns 
    -- the current environment table (where all global variables are stored).
    -- getfenv()[name] = ... dynamically creates a new function named after 
    -- the 'name' variable (e.g., "Nigga") in the global scope.
    getfenv()[name] = function(func)
        -- The newly created function (e.g., 'Nigga') takes an input function ('func', the callback).
        
        -- This is the key logic: it calls the input function and passes the
        -- original 'name' (e.g., "Nigga") back to it as an argument.
        func(name)
    end
end


-- 1. Call the factory function 'luau' with the word "Nigga".
--    This action creates a new callable global function named "Nigga".
luau("Nigga")

-- 2. Call the newly created global function "Nigga".
--    We pass it an 'anonymous function' (the callback) as an argument.
--    The variable 'id' inside the callback will receive the string "Nigga".
Nigga(function(id)
    -- The 'id' variable here is "Nigga".
    print(id .. "same for py")
    
    -- Print the second line.
    print("bit harder to do if u got less knowledge in lua")
end)


-- it is for Luau Ts script is the same as the py one still simple print execution explaination if u wanna learn coding . 
