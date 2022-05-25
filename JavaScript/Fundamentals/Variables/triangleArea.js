function triangleArea(sideA, sideB, sideC) {
  const semiPerimeter = (sideA + sideB + sideC) / 2;
  const triangleArea = Math.sqrt(
    semiPerimeter *
      (semiPerimeter - sideA) *
      (semiPerimeter - sideB) *
      (semiPerimeter - sideC)
  );
  console.log(triangleArea);
}

triangleArea(2, 3.5, 4);
