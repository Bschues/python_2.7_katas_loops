sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712, 71, 456, 21, 398, 339, 882, 848, 179, 535, 940, 472]

print (' 1. ----------------------------')

for i in range(1,21):
    print(i)

print (' 2. ----------------------------')

for i in range(1,21):
    if not i % 2:
        print(i)

print (' 3. ----------------------------')

for i in range(1,21):
    if i % 2:
        print(i)

print (' 4. ----------------------------')

for i in range(1,101):
    if not i % 5:
        print(i)

print (' 5. ----------------------------')

for i in range(1,11):
    print(i * i)

print (' 6. ----------------------------')

i = 20

while i > 0:
    print(i)
    i -= 1

print (' 7. ----------------------------')

i = 20

while i > 0:
    if not i % 2:
        print(i)
    i -= 1

print (' 8. ----------------------------')

i = 20

while i > 0:
    if i % 2:
        print(i)
    i -= 1

print (' 9. ----------------------------')

i = 100

while i > 0:
    if not i % 5:
        print (i)
    i -= 5

print (' 10. ----------------------------')

i = 10

while i > 0:
    print( i * i )
    i -= 1

print (' 11. ----------------------------')

for num in sampleArray:
    print(num)

print (' 12. ----------------------------')

for num in sampleArray:
    if not num % 2:
        print(num)

print (' 13. ----------------------------')

for num in sampleArray:
    if num % 2:
        print(num)

print (' 14. ----------------------------')

for num in sampleArray:
    print(num ** 2)

print (' 15. ----------------------------')

sum = 0

for i in range(1,21):
    sum += i
    if i >=20:
        print(sum)

print (' 16. ----------------------------')

sum = 0

for num in sampleArray:
    sum += num

print(sum)

print (' 17. ----------------------------')

smallest = sampleArray[0]

for num in sampleArray:
    if num <= smallest:
        smallest = num
print(smallest)

print (' 18. ----------------------------')

largest = sampleArray[0]

for num in sampleArray:
    if num >= largest:
        largest = num
print(largest)
