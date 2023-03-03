function rotateArray(arr, rotations) {
	rotations = rotations % arr.length;

	const rotatedArr = [...arr.slice(rotations), ...arr.slice(0, rotations)];

	console.log(rotatedArr.join(' '));
}

rotateArray([51, 47, 32, 61, 21], 2);
