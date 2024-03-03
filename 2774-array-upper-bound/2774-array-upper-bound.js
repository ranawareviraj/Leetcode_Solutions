/** 
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let result = -1;

    this.forEach((val, index) => {
        if(val == target){
            result = index;
        }
    })

    return result;
};


// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5