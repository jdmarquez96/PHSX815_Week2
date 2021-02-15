#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort
#from MySort.py as MySort
sys.path.insert(1, '/home/jdmarquez/Downloads/PHSX815_Week2/python/MySort.py')


# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = True

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open("numbers.txt") as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    #times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

prob = [] 
sns.set_theme()

a = np.quantile(times_avg, 0.1)
b = np.quantile(times_avg, 0.25)
c = np.quantile(times_avg, 0.50)
d = np.quantile(times_avg, 0.75)
e = np.quantile(times_avg, 0.9)


aa = np.quantile(times, 0.1)
bb = np.quantile(times, 0.25)
cc = np.quantile(times, 0.50)
dd = np.quantile(times, 0.75)
ee = np.quantile(times, 0.9)



plt.hist(times,bins = 100, range=[0,4], density=True, color='red', label="100 bins")
plt.xlabel('times')
plt.ylabel('probability')
plt.title('Cookie rate = 1.7')
plt.grid()
plt.axvline(aa,label=".1 quantile")
plt.axvline(bb,label=".25 quantile",color="yellow")
plt.axvline(cc,label=".50 quantile", color="green")
plt.axvline(dd,label=".75 quantile", color="blue")
plt.axvline(ee,label=".9 quantile",color ="purple")
plt.legend()
plt.savefig("times_vs_prob.jpg")
plt.show()

plt.hist(times_avg, density=True, color='green', bins = 50,label="50 bins")
plt.xlabel('times_avg')
plt.ylabel('probability')
plt.title('Cookie rate = 1.7')
plt.grid()
plt.axvline(a,label=".1 quantile")
plt.axvline(b,label=".25 quantile",color="yellow")
plt.axvline(c,label=".50 quantile", color="red")
plt.axvline(d,label=".75 quantile", color="blue")
plt.axvline(e,label=".9 quantile",color ="purple")
plt.legend()
plt.savefig("times_avg_vs_prob.jpg")
plt.show()


