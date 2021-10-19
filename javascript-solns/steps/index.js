// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the # character.  Make sure the
// step has spaces on the right hand side!
// --- Examples
//   steps(2)
//       '# '
//       '##'
//   steps(3)
//       '#  '
//       '## '
//       '###'
//   steps(4)
//       '#   '
//       '##  '
//       '### '
//       '####'

function steps(n) {
  for (let i = 0; i < n; i++) {
    let to_be_printed = '';
    for (let k = 0; k < n; k++) {
      if (k <= i) {
        to_be_printed += '#';
      } else {
        to_be_printed += ' ';
      }
    }
    console.log(to_be_printed);
  }
}

module.exports = steps;
