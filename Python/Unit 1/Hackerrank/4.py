# Swap 2 Numbers:

## Method 1 (Using mathematical operators):

a = int(input())
b = int(input())

a = a + b;
b = a - b;
a = a - b;

print(a);
print(b);


## Method 2 (Using Xor):

a = int(input())
b = int(input())

a = a ^ b;
b = a ^ b;
a = a ^ b;

print(a);
print(b);
