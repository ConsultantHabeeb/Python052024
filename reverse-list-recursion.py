def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

# Example usage:
lst = [1, 2, 3, 4, 5]
reversed_lst = reverse_list(lst)
print(f"Original list: {lst}")
print(f"Reversed list: {reversed_lst}")




