/**
 * Filters elements from an array based on the provided function.
 * 
 * @param {number[]} arr - The array to filter.
 * @param {Function} fn - The function to test each element, returning true to keep the element.
 * @return {number[]} - The filtered array.
 */
var filter = function(arr, fn) {
    const result = [];

    // Use forEach to iterate over each element in the array
    arr.forEach((element, index) => {
        if (fn(element, index)) {
            result.push(element);  // Add to result if the callback returns true
        }
    });

    return result;
};




// /**
//  * @param {number[]} arr
//  * @param {Function} fn
//  * @return {number[]}
//  */
// var filter = function(arr, fn) {
//     const result = [];

//     for(let i = 0; i < arr.length; i++){
//         if (fn(arr[i], i)){
//             result.push(arr[i]);
//         }
//     }
//     return result;
// };