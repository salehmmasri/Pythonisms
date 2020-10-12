from decorators import *


@slow_down
def factors1(n):
    results = [ ]
    for k in range(1,n+1):
        if n % k == 0: results.append(k)
    return results
## Generator that produces the same numbers but under each other not in a list
@slow_down
def factors2(n):
    for k in range(1,n+1):
        if n % k == 0: 
            yield k
print(factors1(100))
## output : [1, 2, 4, 5, 10, 20, 25, 50, 100]
for factor in factors2(100):
    print(factor)
