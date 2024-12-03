def read_input(filename="input2.txt"):
    reports = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to list of integers
                levels = list(map(int, line.strip().split()))
                reports.append(levels)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    
    return reports

def is_safe(levels):
    if len(levels) < 2:
        return False
    
    # Get first difference to determine direction
    first_diff = levels[1] - levels[0]
    if abs(first_diff) < 1 or abs(first_diff) > 3:
        return False
    
    # Check if increasing or decreasing
    is_increasing = first_diff > 0
    
    # Check all adjacent pairs
    for i in range(1, len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        # Check if difference is between 1 and 3
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        # Check if direction matches
        if is_increasing and diff <= 0:
            return False
        if not is_increasing and diff >= 0:
            return False
    
    return True

def is_safe_with_dampener(levels):
    # First check if safe without dampener
    if is_safe(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create new list without current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe(dampened_levels):
            return True
    
    return False

def count_safe_reports(reports, use_dampener=False):
    if use_dampener:
        return sum(1 for report in reports if is_safe_with_dampener(report))
    return sum(1 for report in reports if is_safe(report))

def main():
    # Read input
    reports = read_input()
    
    if not reports:
        return
    
    # Part 1: Count safe reports without dampener
    safe_count = count_safe_reports(reports)
    print(f"Part 1 - Number of safe reports: {safe_count}")
    
    # Part 2: Count safe reports with dampener
    safe_count_dampened = count_safe_reports(reports, use_dampener=True)
    print(f"Part 2 - Number of safe reports with dampener: {safe_count_dampened}")

if __name__ == "__main__":
    main()
