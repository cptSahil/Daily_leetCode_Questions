Array.prototype.last = function() {
  const [lastElement = -1] = this.slice(-1);
  return lastElement;
}