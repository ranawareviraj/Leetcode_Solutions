/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let originalValue = init;
    let counter = init;

    return {
        increment: () => ++counter,
        decrement: () => --counter,
        reset: () => counter = originalValue
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */