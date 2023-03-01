for s in range(10):
    for e in range(10):
        for n in range(10):
            for d in range(10):
                for f in range(10):
                    for l in range(10):
                        for r in range(10):
                            for p in range(10):
                                for g in range(10):
                                    first = s*1000+e*100+n*10+d
                                    second = f*1000+l*100+e*10+r
                                    third = p*10000+e*1000+n*100+g*10+e

                                    if first+second == third:
                                        print(f"{s} {e} {n} {d} {f} {l} {r} {p} {g}")
