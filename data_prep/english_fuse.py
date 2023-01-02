#!/usr/bin/env python3

a = ["english.dev.conll","english.train.conll","english.test.conll"]
for filename in a:
    depfilename = filename + ".dep"

    with open(filename + ".tab", encoding='utf-8') as f:
        if f is None:
            print('error1')
        srldata = f.read().strip().split("\n")
    with open(depfilename, encoding='utf-8') as f:
        if f is None:
            print('error2')
        depdata = f.read().strip().split("\n")

    outfile = filename + ".fused"

    line_no = 0
    with open(outfile, "w", encoding='utf-8') as fout:
        for l1, l2 in zip(srldata, depdata):
            line_no += 1
            print((len(l1) == 0))
            if (len(l1) == 0) != (len(l2) == 0):
                print(line_no, "err")
            if len(l1) == 0:
                fout.write("\n")
            else:
                s = l1.split("\t")
                t = l2.split("\t")
                fout.write(("\t".join(s[:11] + t[6:8] + s[11:])))
                fout.write("\n")
