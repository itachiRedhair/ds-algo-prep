// --- Directions
// Print out the n-th entry in the fibonacci series.
// The fibonacci series is an ordering of numbers where
// each number is the sum of the preceeding two.
// For example, the sequence
//  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
// forms the first ten entries of the fibonacci series.
// Example:
//   fib(4) === 3

// function fib(n) {
//   const results = [0, 1];

//   for (let i = 2; i <= n; i++) {
//     results.push(results[results.length - 1] + results[results.length - 2]);
//   }

//   return results[results.length - 1];
// }

// Recursion
function fib(n) {
  const memo = {};

  return fib_memo(n, memo);
}

function fib_memo(n, memo) {
  if (n === 0 || n === 1) {
    return n;
  }

  if (memo[n]) {
    return memo[n];
  }

  return fib(n - 1) + fib(n - 2);
}

module.exports = fib;
