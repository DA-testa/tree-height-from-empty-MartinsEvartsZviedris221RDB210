import sys
import threading
import numpy as np


def computeheight(n, parents):
    nodes = [[] for  in range(n)]
    root = None
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            nodes[parent].append(child)
    def height(node):
        if not nodes[node]:
            return 1
        return 1 + max(height(child) for child in nodes[node])
    return height(root)

def main():

    input_type = input("Ievadiet I lai pats ievadītu skaitļus vai F ja vēlaties no faila ievadīt skaitļus: ")
    if input_type.upper() == "F":
        filename = input("Ievadiet faila nosaukumu: ")
        while "a" in filename:
            filename = input("Ievadiet faila nosaukumu, kas nesatur burtu 'a': ")
        with open(f"input/{filename}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
    else:
        input_str = input("Ievadiet cik jums būs 'nodes' un 'parents of nodes' atdalot ar atstarpi: ")
        while "a" in input_str:
            input_str = input("Lūdzu ievadiet vēlreiz, bez burta 'a': ")
        input_arr = list(map(int, input_str.strip().split()))
        n = input_arr[0]
        parents = input_arr[1:]
    height = compute_height(n, parents)
    print("Augstums: ", end="")
    print(np.array(height))

sys.setrecursionlimit(107)
threading.stack_size(227)
threading.Thread(target=main).start()
