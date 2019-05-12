#!/usr/bin/env python3
# -*- config: utf-8 -*-

def factorial(n: int) -> int:
    return 1 if n < 1 else n * factorial(n-1)

if __name__ == '__main__':
    import sys
    print(factorial(int(sys.argv[-1])))