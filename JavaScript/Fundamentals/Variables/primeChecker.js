function primes(num) {
  const isPrime = (num) => {
    for (let i = 2, s = Math.sqrt(num); i <= s; i++)
      if (num % i === 0) return false;
    return num > 1;
  };
  if (isPrime(num)) {
    console.log("true");
  } else {
    console.log("false");
  }
}

primes(7)