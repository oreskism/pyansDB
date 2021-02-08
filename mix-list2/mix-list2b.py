#! /usr/bin/env python3
# this is the list we want to agument
proto = ['ssh','http','https']

# this is the list we wnat to augment a bit differently
protoa = ['ssh','http','https']

# print the first list we created
print(proto)

# change our first list
proto.append('dns') # this  will add 'dns' to the end of the line

# perform same change to second list
protoa.append('dns')

# display on the screen of the first list
print(proto)

# display on screen of second list
print(protoa)

# create new list of information
proto2 = [22, 80, 443, 53] # a list of common ports

# list.extend()
proto.extend(proto2)

print("\nThis is what list.extend() did to our list.\nExtend iterated through proto2, and added each element to the end of the list (fancy way to say it combined the lists).")

print (proto) 

# list.append()
protoa.append(proto2)
print("\nThis is what list.append() did to our list.\nAppend opens up a single slot at the end of the list.")
print (protoa) 

print(proto[4])
print(protoa[4][0])

