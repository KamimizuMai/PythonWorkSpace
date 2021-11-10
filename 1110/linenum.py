import os
file_name = "1110/word.txt"
with open(file_name) as f:
    gyou = 1
    for i in f:
        # print("{:0>4}:{}".format(gyou,i))
        print("{0:04d}:{1}".format(gyou,i.strip()))

        gyou += 1