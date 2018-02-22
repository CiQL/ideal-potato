#!/usr/bin/env python3
# -*- config: utf-8 -*-

def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n-1)
