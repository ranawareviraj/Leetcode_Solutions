/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    filteredArr = new Array(arr.length);

    for(const index in arr){
        if(fn(arr[index], Number(index))){
            filteredArr[index] = arr[index];
        }
    }

    return filteredArr;
};