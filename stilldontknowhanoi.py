def hanoi(n, source, helper, target):
    '''Does the Hanoi thing. Shows the steps needed to get there.'''
    print("hanoi( ", n, source, helper, target, " called")
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = ([4,3,2,1], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]),source,helper,target)

print(source, helper, target)

# f.y.i: the least readable thing ever:
# i = input()
# j = input()
# string = i[:int(j[0])] + j[2] + i[int(j[0])+1:]
# print(string)
