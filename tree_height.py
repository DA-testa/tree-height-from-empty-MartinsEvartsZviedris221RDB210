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
    
    input_type = input("Ievadiet 'I' ja vēlaties skaitļus ievadīt no tastatūras vai 'F' ja vēlaties no faila ievadīt: ")

    if input_type == "I":
        
        n = int(input("ievadiet 'nodes' daudzumu: "))
        parents = list(map(int, input("ievadiet vērtības atdalot ar atstarpi: ").split()))
       
    elif input_type == "F":
        
        file_name = input("ievadiet faila nosaukumu: ")
        
        if "a" in file_name:
            
            print("faila nosaukums nedr;ikst saturēt burtu 'a'")
            return
        
        try:
            
            with open(f"./test/{file_name}", "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
                
        except Exception as e:
            print(f"Error: {e}")
            return
        
    else:
        print("Error: Invalid input type.")
        return

    print(compute_height(n, parents))


# Increase recursion depth limit and stack size for larger inputs.
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
