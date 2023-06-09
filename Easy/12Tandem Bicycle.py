# we have people with red & Blue shirt & their  speeds
#
#We are given two arrays of positive integers: the first one represents the speeds of riders
# with red shirts and the second one represents the speeds of riders with blue shirt.

# Both array have the same length. We will also receive a Boolean `fastest`.

# We are asked to write a function that is going to pair every red-shirt rider with a blue-shirt rider to operate a tandem bicycle.
# A tandem bicycle is a bicycle operated by two people. The speed of the bicycle is dictated by the rider who pedals faster,
# for instance, if the speed of one rider is `5` and the speed of the other rider is `3`, then the speed of the bicycle is `5`.

# If the Boolean `fastest` is `true`, the function should return the total maximum speed of all tandem bicycles being ridden;
# otherwise return the total minimum speed.



def findFastest(rred, bblue, MxOrMn):
    # arr2 = arr1.copy()
    # red = red.sort(reverse=True)
    rred.sort(reverse=True)
    red = rred.copy()
    print("20-red=", red);

    if MxOrMn:
        bblue.sort()
        blue = bblue.copy();
        print("27-blue=", blue);
    else:
        bblue.sort(reverse=True)
        blue = bblue.copy();
        print("31-blue=", blue);


    print(red); print(blue); print(MxOrMn)
    print( max(5,2) )
    list = [];

    for i, RedVal in enumerate(red):
        print("i =", i  ,"val =", RedVal)
        list.append( max(RedVal, blue[i]))
        print("28-list =", list)
        print(sum(list))
    return sum(list);




redShirtSpeeds = [5, 5, 3, 9,2]
blueShirtSpeeds =[3, 6, 7, 2,1]

# copiedAar = redShirtSpeeds.copy();
# print("43-copiedAar =", copiedAar)
# redShirtSpeeds.pop()
# print("45-copiedAar =", copiedAar)

fastest = True  # total maximum speed of all tandem bicycles being ridden
               # Max [5,6,7,9,2] = total = 29
               # Min [3,5,3,2,1] = total = 7
res = findFastest(redShirtSpeeds,blueShirtSpeeds, True )
# res = findFastest(redShirtSpeeds,blueShirtSpeeds, False )
print("40-res =", res);