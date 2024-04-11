let SIZE = process.argv[2];

// insertion sort of an array of integers
function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let j = i - 1;
        let tmp = arr[i];
        while (j >= 0 && (arr[j] > tmp)) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = tmp;
    }
    return arr;
}

function wait(n) {
    for (let i = 0; i < n; i++);
}

// populate random array of size SIZE
let arr = [];
for (let i = 0; i < SIZE; i++) {
    arr.push(Math.floor(Math.random() * 1000));
}

// time
// wait(SIZE);
let start = new Date().getTime();
insertionSort(arr);
let end = new Date().getTime();
let time = (end - start) / 1000;
console.log('Time taken: ' + time + ' seconds.');