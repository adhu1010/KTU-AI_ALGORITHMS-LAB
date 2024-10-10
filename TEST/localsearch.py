import random

def is_valid(assignment, neighbors):
    for region in assignment:
        for neighbor in neighbors[region]:
            if assignment[region] == assignment[neighbor]:
                return False
    return True

def count_conflicts(assignment, neighbors):
    conflicts = 0
    for region in assignment:
        for neighbor in neighbors[region]:
            if assignment[region] == assignment[neighbor]:
                conflicts += 1
    return conflicts

def min_conflicts(map_regions, neighbors, colors, max_steps=1000):
    assignment = {region: random.choice(colors) for region in map_regions}
    for step in range(max_steps):
        if is_valid(assignment, neighbors):
            return assignment

        conflicts = count_conflicts(assignment, neighbors)
        print(f"Step {step}: Current conflicts = {conflicts}")
        print(f"Current assignment: {assignment}")
        
        conflicted_regions = [region for region in map_regions if any(assignment[region] == assignment[neighbor] for neighbor in neighbors[region])]
        region = random.choice(conflicted_regions)
        min_conflict_color = None
        min_conflict_count = float('inf')
        
        for color in colors:
            assignment[region] = color
            conflict_count = sum(1 for neighbor in neighbors[region] if assignment[region] == assignment[neighbor])
            if conflict_count < min_conflict_count:
                min_conflict_count = conflict_count
                min_conflict_color = color
        assignment[region] = min_conflict_color
    return None

def main():
    num_regions = int(input("Enter the number of regions: "))
    map_regions = []
    neighbors = {}
   
    for i in range(num_regions):
        region_name = input(f"Enter the name of region {i + 1}: ")
        map_regions.append(region_name)
        neighbor_names = input(f"Enter the neighbors of {region_name} (comma separated): ").split(",")
        neighbors[region_name] = [name.strip() for name in neighbor_names]
   
    colors = input("Enter the available colors (comma separated): ").split(",")
    colors = [color.strip() for color in colors]
    solution = min_conflicts(map_regions, neighbors, colors)
   
    if solution:
        print("\nSolution Found:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("\nNo valid solution found within the given steps.")

main()

