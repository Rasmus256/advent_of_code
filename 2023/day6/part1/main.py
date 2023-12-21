from functools import reduce
times=[49,87,78,95]
records = [356,1378,1502,1882]
print(reduce((lambda x, y: x * y),[sum([(records[j] <= i*(times[j]-i)) for i in range(times[j])]) for j in range(len(times))]))