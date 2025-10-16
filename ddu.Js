// The 'luau' function acts as our function factory.
function luau(name) {
    // 1. Define the function that will be created and globally exposed.
    // This function (e.g., 'Nigga') takes a 'func' (the callback) as its argument.
    const outerFunction = function(func) {
        // 2. The core logic: immediately call the input function ('func')
        // and pass the original 'name' (e.g., "Nigga") back to it.
        func(name);
    };

    // 3. This line injects 'outerFunction' into the global scope.
    // 'globalThis' is the standard way to reference the global object (like 'window' in a browser, 
    // or 'global' in Node.js), which is the equivalent of Luau's 'getfenv()' 
    // or Python's 'globals()'.
    globalThis[name] = outerFunction; 
}

// Usage
// still an simple print in JavaScript and not java ! It is not the same Like Luau and Lua skids ! 
// it's for learnin print in javascript

// . Call the factory function 'luau' with the desired name.
//    This creates a new callable function named "Nigga" globally.
luau("Nigga");

// 2. Call the newly created global function "Nigga".
//    We pass it an anonymous function (the callback) as its argument.
Nigga(function(id) {
    // The 'id' variable receives the string "Nigga" from the outer function.
    console.log(id + "same for py");
    console.log("bit harder to do if u got less knowledge in lua");
});

// u might have seen the functions r still Luau bc I was lazy to change em
