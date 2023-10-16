def count_apples(days: int, apples_in_backet: int) -> int:
    if days == 0:
        return apples_in_backet
    return count_apples(days -1, apples_in_backet + 1)

if __name__ == "__main__":
    print(count_apples(5,0))