// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
  constructor(element, next = null) {
    this.data = element;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  insertFirst(element) {
    this.head = new Node(element, this.head);
  }

  size() {
    let counter = 0;

    let n = this.head;
    while (n.next) {
      n = n.next;
      counter++;
    }
    return counter;
  }

  getFirst() {
    return this.head;
  }

  getLast() {
    if (!this.head) {
      return null;
    }

    let n = this.head;

    while (n.next) {
      n = n.next;
    }
    return n;
  }

  clear() {
    this.head = null;
  }

  removeFirst() {
    if (!this.head) {
      return;
    }
    this.head = this.head.next;
  }

  removeLast() {
    if (!this.head) {
      return;
    }

    if (!this.head.next) {
      this.head = null;
      return;
    }

    prev_node = this.head;
    node = this.head.next;

    while (node.next) {
      prev_node = node;
      node = node.next;
    }

    prev_node.next = null;
  }

  insertLast(element) {
    if (!this.head) {
      this.head = new Node(element);
    }

    last_node = this.getLast();

    last_node.next = new Node(element);
  }

  getAt(index) {
    if (!this.head) {
      return null;
    }

    let counter = 0;
    let node = this.head;

    while (node) {
      if (counter === index) {
        return node;
      }

      counter++;
      node = node.next;
    }
  }

  removeAt(index) {
    if (!this.head) {
      return;
    }

    if (index === 0) {
      this.head = this.head.next;
    }

    prev_node = this.getAt(index - 1);

    if (!prev_node.next) {
      return;
    }

    prev_node.next = prev_node.next.next;
  }

  insertAt(element, index) {
    if (!this.head) {
      this.head = new Node(element);
    }

    if (index === 0) {
      this.insertFirst(element);
    }
    prev_node = this.getAt(index - 1) || this.getLast();

    prev_node.next = new Node(element);
  }

  
}

module.exports = { Node, LinkedList };
