function diagonalSums(matrix = []) {
    let leftDiag = 0;
    let rightDiag = 0;

    let count = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = count; j < matrix[i].length; j++) {
            leftDiag += matrix[i][j];
            count++;
            break;
        }
    }

    count = matrix[0].length - 1;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = count; j >= 0; j--) {
            rightDiag += matrix[i][j];
            count--;
            break;
        }
    }
    console.log(leftDiag, rightDiag);
}

diagonalSums([
    [20, 40],
    [10, 60],
]);

diagonalSums([
    [3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89],
]);
