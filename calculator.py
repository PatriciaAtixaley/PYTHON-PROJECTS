import math

def insert_series():
    series = []
    n = int(input("Enter the number of elements in the series: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        series.append(element)
    return series

def minimum(series):
    return min(series)

def maximum(series):
    return max(series)

def series_sum(series):
    return sum(series)

def arithmetic_mean(series):
    return sum(series) / len(series)

def product(series):
    result = 1
    for num in series:
        result *= num
    return result

def geometric_mean(series):
    result = 1
    for num in series:
        result *= num
    return result ** (1 / len(series))

def standard_deviation(series):
    mean = arithmetic_mean(series)
    variance = sum((x - mean) ** 2 for x in series) / len(series)
    return math.sqrt(variance)

def full_report(series):
    print("Minimum:", minimum(series))
    print("Maximum:", maximum(series))
    print("Sum:", series_sum(series))
    print("Arithmetic Mean:", arithmetic_mean(series))
    print("Product:", product(series))
    print("Geometric Mean:", geometric_mean(series))
    print("Standard Deviation:", standard_deviation(series))

def show_series(series):
    print("Series:", series)

def main():
    series = []
    while True:
        print("\nBASIC STATISTICS CALCULATOR:")
        print("1.- Insert Series")
        print("2.- Minimum")
        print("3.- Maximum")
        print("4.- Sum")
        print("5.- Arithmetic Mean")
        print("6.- Product")
        print("7.- Geometric Mean")
        print("8.- Standard Deviation")
        print("9.- Full Report")
        print("10.- Show Series")
        print("0.- Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            series = insert_series()
        elif choice == 2:
            print("Minimum:", minimum(series))
        elif choice == 3:
            print("Maximum:", maximum(series))
        elif choice == 4:
            print("Sum:", series_sum(series))
        elif choice == 5:
            print("Arithmetic Mean:", arithmetic_mean(series))
        elif choice == 6:
            print("Product:", product(series))
        elif choice == 7:
            print("Geometric Mean:", geometric_mean(series))
        elif choice == 8:
            print("Standard Deviation:", standard_deviation(series))
        elif choice == 9:
            full_report(series)
        elif choice == 10:
            show_series(series)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
