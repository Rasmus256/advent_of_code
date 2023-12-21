from functools import reduce
times=[49877895]
records = [356137815021882]
print(reduce((lambda x, y: x * y),[sum([(records[j] <= i*(times[j]-i)) for i in range(times[j])]) for j in range(len(times))]))