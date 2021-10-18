// --- Directions
// Given an integer, return an integer that is the reverse
// ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9

function reverseInt(n) {
  sign = Math.sign(n);

  absolute_n = Math.abs(n);

  const reversed_int = parseInt(n.toString().split('').reverse().join(''));

  return reversed_int * sign;
}

module.exports = reverseInt;
