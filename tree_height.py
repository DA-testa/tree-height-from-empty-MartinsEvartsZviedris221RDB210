import sys
import threading
import os


def compute_height(num_nodes, parents):
    
    children = {i: [] for i in range(num_nodes)}

    root = None
    for i in range(num_nodes):
        
        parent = parents[i]
        
        if parent == -1:
            root =i
            
        else:
            children[parent].append(i)

    def height(node):
        
        if not children[node]:
            return 1
        
        else:
            return 1 +max(height(child) for child in children[node])

    return height(root)


def main():
    
    input_type = input("Enter 'F' for file, or 'I' for input: ")
    
    if "I" in input_type:
        num_nodes = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent nodes devided by spaces: ").split()))
        
    elif "F" in input_type:
        path = "./test/"
        filename = input("Enter the name of file: ")
        file_path = os.path.join(path, filename)

        if "a" not in filename:
            try:
                with open(file_path) as f:
                    num_nodes = int(f.readline().strip())
                    parents = list(map(int, f.readline().strip().split()))
                    
            except Exception as e:
                print("Error:", str(e))
                return
            
    else:
        print("Invalid input type. Please enter 'I' or 'F'.")
        return

    print(compute_height(num_nodes, parents))
    
sys.setrecursionlimit(107)  # max depth of recursion
threading.stack_size(227)  # new thread will get stack of such size
threading.Thread(target=main).start()
