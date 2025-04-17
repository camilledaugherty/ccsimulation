import sys

#usage: python gen_trace.py rate duration > tracefile.trace

rate = float(sys.argv[1])
duration = int(sys.argv[2])
base = 12
total_lines = duration*1000

if int(rate)>base: #greater than 12
        repeats = int(rate / base)

        for t in range(total_lines):
                for _ in range(repeats):
                        print(t)
else:
        for t in range(0, total_lines, int(base/rate)): #less than 12
                print(t)
