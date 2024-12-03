def read_input(filename="input.txt"):
    left_list = []
    right_list = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split line and convert to integers
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return [], []
    
    return left_list, right_list

def calculate_distance(left_list, right_list):
    if len(left_list) != len(right_list):
        raise ValueError("Lists must be of equal length")
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

def calculate_similarity(left_list, right_list):
    # Create frequency map for right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity score
    total = 0
    for num in left_list:
        count = right_counts.get(num, 0)
        total += num * count
    
    return total

def main():
    # Read input
    left_list, right_list = read_input()
    
    if not left_list or not right_list:
        return
        
    # Part 1
    distance = calculate_distance(left_list, right_list)
    print(f"Part 1 - Total distance between lists: {distance}")
    
    # Part 2
    similarity = calculate_similarity(left_list, right_list)
    print(f"Part 2 - Similarity score: {similarity}")

if __name__ == "__main__":
    main()
