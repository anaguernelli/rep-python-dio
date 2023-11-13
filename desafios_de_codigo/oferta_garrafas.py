T = int(input())

for i in range(T):
    N, K = input().split()
    # refrigerantes e garrafas vazias, respectivamente
    N = int(N)  # type: ignore
    K = int(K)  # type: ignore

    total_garrafas = (N / K) + (N % K)  # type: ignore
    print(total_garrafas)
