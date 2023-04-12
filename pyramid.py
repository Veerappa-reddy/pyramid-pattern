#python

N = int(input())

for i in range(1,N+1):
    pattern_line = (chr(96+i)+str(i))*i
    pattern_line_half_len = int(len(pattern_line)/2)
    print(pattern_line[pattern_line_half_len:])


# input:
# 6

# output:
# 1
# b2
# 3c3
# d4d4
# 5e5e5
# f6f6f6



