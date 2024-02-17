/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = new Int32Array(arr.length);

    for(const index in arr){
        newArr[index] = fn(arr[index], Number(index));
    }
    
    return newArr;
};