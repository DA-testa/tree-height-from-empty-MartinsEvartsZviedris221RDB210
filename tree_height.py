import sys
import threading


def compute_height(n, parents):

    koks = [[] for _ in range(n)]
    root_node = None

    for child_node, parent_node in enumerate(parents):
        
        if parent_node == -1:
            root_node = child_node
            
        else:
            koks[parent_node].append(child_node)

    def garums(node):
        
        height = 1
        
        if not koks[node]:
            
            return height
        
        else:
            for child in koks[node]:
                
                height = max(height, garums(child))

            return height + 1
        
    return garums(root_node)


def main():
    
    
        
        n = int(input("ievadiet 'nodes' daudzumu: "))
        parents = list(map(int, input("ievadiet vērtības atdalot ar atstarpi: ").split()))
       
   

        print(compute_height(n, parents))


# Increase recursion depth limit and stack size for larger inputs.
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
