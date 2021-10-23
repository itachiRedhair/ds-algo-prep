// --- Directions
// Given a linked list, return true if the list
// is circular, false if it is not.
// --- Examples
//   const l = new List();
//   const a = new Node('a');
//   const b = new Node('b');
//   const c = new Node('c');
//   l.head = a;
//   a.next = b;
//   b.next = c;
//   c.next = b;
//   circular(l) // true

function circular(list) {
  let slow_n = list.getFirst();

  let fast_n = list.getFirst();

  while (fast_n.next && fast_n.next.next) {
    slow_n = slow_n.next;
    fast_n = fast_n.next.next;
    if (slow_n === fast_n) {
      return true;
    }
  }
  return false;
}

module.exports = circular;
