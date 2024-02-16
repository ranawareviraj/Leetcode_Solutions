/**
 * @return {Function}
 */
let createHelloWorld = function() {
    f = function() {
        return "Hello World";
    }
    return f;
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */