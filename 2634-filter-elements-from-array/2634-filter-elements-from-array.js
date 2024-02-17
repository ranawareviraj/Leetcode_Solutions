/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    filteredArr = [];

    for (const index in arr) {
        if (fn(arr[index], Number(index))) {
            filteredArr.push(arr[index]);
        }
    }

    return filteredArr;
};