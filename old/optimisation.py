from timeit import default_timer as timer


my_list = (range(1000000))


def bad_function():
    result = ""
    for item in my_list:
        result += str(item)
    return result

def better_function():
    result_parts = []
    for item in my_list:
        result_parts.append(str(item))
    return "".join(result_parts)

def best_function():
    return "".join(map(str, my_list))


def main():
    start = timer()
    bad_function()
    end = timer()
    print(f'Time of bad function: {end - start:.3f} seconds')

    start = timer()
    better_function()
    end = timer()
    print(f'Time of better function: {end - start:.3f} seconds')

    start = timer()
    best_function()
    end = timer()
    print(f'Time of best function: {end - start:.3f} seconds')


if __name__ == "__main__":
    main()
