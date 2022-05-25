function matrixEquals(matrix = []) {
    let counts = 0;
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (row === matrix.length - 1) {
                if (col !== matrix[row].length - 1) {
                    if (matrix[row][col] === matrix[row][col + 1]) {
                        counts++;
                    }
                }
            } else {
                if (col !== matrix[row].length - 1) {
                    if (
                        matrix[row][col] === matrix[row + 1][col] &&
                        matrix[row][col] === matrix[row][col + 1]
                    ) {
                        counts += 2;
                    } else if (
                        matrix[row][col] === matrix[row + 1][col] ||
                        matrix[row][col] === matrix[row][col + 1]
                    ) {
                        counts++;
                    }
                } else {
                    if (matrix[row][col] === matrix[row + 1][col]) {
                        counts++;
                    }
                }
            }
        }
    }
    console.log(counts);
}

matrixEquals([
    ["2", "3", "4", "7", "0"],
    ["4", "0", "5", "3", "4"],
    ["2", "3", "5", "4", "2"],
    ["9", "8", "7", "5", "4"],
]);

matrixEquals([
    ["test", "yo", "yo", "ho"],
    ["well", "done", "no", "6"],
    ["not", "done", "yet", "5"],
]);
