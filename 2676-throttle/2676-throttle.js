/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let timeoutId = null, restTime = 0;
    return function(...args) {
        const currentTime = Date.now();
        const delay = Math.max(0, restTime - currentTime);
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => { 
            fn(...args);
            restTime = Date.now() + t;
        }, delay);
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */