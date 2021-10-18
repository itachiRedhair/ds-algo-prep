// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
  const char_count_hash_map = {};

  for (let char of str) {
    if (!char_count_hash_map[char]) {
      char_count_hash_map[char] = 1;
    } else {
      char_count_hash_map[char] += 1;
    }
  }

  let max = 0;
  let max_char = '';


  for (let char in char_count_hash_map) {
    if (char_count_hash_map[char] > max) {
      max = char_count_hash_map[char];
      max_char = char;
    }
  }

  return max_char;
}
maxChar('abcdefghijklmnaaaaa');

module.exports = maxChar;
