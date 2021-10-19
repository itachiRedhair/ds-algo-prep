// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'
//   pyramid(4)
//       '   #   '
//       '  ###  '
//       ' ##### '
//       '#######'

function pyramid(n) {
  for (let i = 0; i < n; i++) {
    let pounds = '';
    let spaces = '';
    for (let k = 0; k < n - (i + 1); k++) {
      spaces += ' ';
    }
    for (let k = 0; k < 2 * (i + 1) - 1; k++) {
      pounds += '#';
    }

    const to_be_printed = spaces + pounds + spaces;

    console.log(to_be_printed);
  }
}

pyramid(4);

module.exports = pyramid;
