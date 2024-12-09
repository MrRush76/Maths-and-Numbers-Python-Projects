import random

games = ['Ghost Recon Wildlands', 'Snow Runner', 'Little Big Planet 3', 'Borderlands 3', 'Prey', 'Red Dead Redemption 2', 'Wolfenstein 2', 'Dishonored 2', 'Dirt 5', 'Watch Dogs 2', 'Sniper Ghost Warrior Contracts 2', 'Assassins Creed Black Flag', 'Mafia 3', 'Horizon Forbidden West', 'Far Cry 5', 'Cyberpunk 2077', 'Minecraft', 'Metal Gear Solid V']

def bubble_sort(games):
    for i in range(len(games)):
        list_srt = False
        while list_srt == False:
            for j in range(len(games)-1):
                no_sorts = 0
                if games[j] > games[j+1]:
                    games[j], games[j+1] = games[j+1], games[j]
                    no_sorts += 1
            if no_sorts == 0:
                list_srt = True
    return games

def insertion_backwards(list):
    for i in range(len(list) -1, 0, -1):
        if list[i] < list[i-1]:
            list[i], list[i-1] = list[i-1], list[i]
        else:
            break
    return list

def insertion_forwards(list):
    for i in range(len(list) -1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
        else:
            list[:i] = insertion_backwards(list[:i])
    return list

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def get_user_list():
    user_list = input("Enter a list of items separated by commas: ").split(',')
    return [item.strip() for item in user_list]

def get_random_list():
    return [random.randint(1, 100) for _ in range(20)]

def main():
    print("Choose an option:")
    print("1. Use predefined list of games")
    print("2. Enter your own list")
    print("3. Use a list of random numbers")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        list_to_sort = games
    elif choice == '2':
        list_to_sort = get_user_list()
    elif choice == '3':
        list_to_sort = get_random_list()
    else:
        print("Invalid choice")
        return

    print("Choose a sorting method:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    sort_choice = input("Enter your choice (1/2/3): ")

    if sort_choice == '1':
        sorted_list = bubble_sort(list_to_sort)
    elif sort_choice == '2':
        sorted_list = insertion_forwards(list_to_sort)
    elif sort_choice == '3':
        sorted_list = merge_sort(list_to_sort)
    else:
        print("Invalid choice")
        return

    print(f"Sorted List: {sorted_list}")

main()