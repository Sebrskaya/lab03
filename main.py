def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    try:
        n = int(input("Введите количество чисел: "))
        if n <= 0:
            print("Введите положительное число.")
            return

        numbers = []
        for i in range(n):
            num = float(input(f"Введите число {i + 1}: "))
            numbers.append(num)

        bubble_sort(numbers)

        print("Отсортированный список по возрастанию:")
        for num in numbers:
            print(num)

    except ValueError:
        print("Ошибка: Введите корректные числа.")

if __name__ == "__main__":
    main()