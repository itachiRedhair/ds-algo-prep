// --- Directions
// Return the 'middle' node of a linked list.
// If the list has an even number of elements, return
// the node at the end of the first half of the list.
// *Do not* use a counter variable, *do not* retrieve
// the size of the list, and only iterate
// through the list one time.
// --- Example
//   const l = new LinkedList();
//   l.insertLast('a')
//   l.insertLast('b')
//   l.insertLast('c')
//   midpoint(l); // returns { data: 'b' }

function midpoint(list) {
  let slow_n = list.getFirst();
  let fast_n = list.getFirst();

  while (fast_n.next && fast_n.next.next) {
    slow_n = slow_n.next;
    fast_n = fast_n.next.next;
  }

  return slow_n;
}

module.exports = midpoint;
