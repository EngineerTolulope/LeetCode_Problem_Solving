/**
 * Applies a function to each element in an array and returns a new array.
 * @param {number[]} arr - The array to be mapped over.
 * @param {Function} fn - The function to apply to each element, taking two arguments: the element and its index.
 * @return {number[]} - A new array with the results of applying `fn` to each element.
 */
var map = function (arr, fn) {
    const result = new Array();

    for (let i = 0; i < arr.length; i++) {
        result[i] = fn(arr[i], i);
    }

    return result;
};
