// --- Directions
// Given a linked list, return the element n spaces
// from the last node in the list.  Do not call the 'size'
// method of the linked list.  Assume that n will always
// be less than the length of the list.
// --- Examples
//    const list = new List();
//    list.insertLast('a');
//    list.insertLast('b');
//    list.insertLast('c');
//    list.insertLast('d');
//    fromLast(list, 2).data // 'b'

function fromLast(list, n) {
  let slow_n = list.getFirst();
  let fast_n = list.getFirst();

  let i = n;
  while (fast_n.next && i > 0) {
    fast_n = fast_n.next;
    i--;
  }

  while (fast_n.next) {
    slow_n = slow_n.next;
    fast_n = fast_n.next;
  }

  return slow_n;
}

module.exports = fromLast;
