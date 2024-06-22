function isPowerOfTwo(n){
  return n > 0 && (n & (n - 1)) === 0;
}

// uses bitwise operator of & to compare bitset, a power of two has exactly one bitset in its binary