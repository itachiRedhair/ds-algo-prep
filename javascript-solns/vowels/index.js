// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

function vowels(str) {
  const vowels_checker = 'aieou';

  let counter = 0;
  for (char of str.toLowerCase().split('')) {
    if (vowels_checker.includes(char)) {
      counter += 1;
    }
  }
  return counter;
}

module.exports = vowels;
