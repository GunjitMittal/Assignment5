e=10e-6
pr_a=0.3;pr_b=0.4
pr_anb = pr_a*pr_b
pr_aub = pr_a+pr_b-pr_anb
pr_a_b = pr_anb / pr_b
pr_b_a = pr_anb / pr_a
if abs(pr_anb-0.12)<e:
    print("Solution to part (i) verified.\n")
if abs(pr_aub-0.58)<e:
    print("Solution to part (ii) verified.\n")
if abs(pr_a_b-0.3)<e:
    print("Solution to part (iii) verified.\n")
if abs(pr_b_a-0.4)<e:
    print("Solution to part (iv) verified.\n")