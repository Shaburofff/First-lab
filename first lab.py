DIGITS = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

def number_to_words(number):
    return ' '.join(DIGITS[digit] for digit in number)

def process_stream(filename):
    with open(filename, 'r') as file:
        data = file.read().split()
    
    count = 0
    min_odd_number = None

    for item in data:
        if item.isdigit() and len(item) == 4 and item.startswith("97") and int(item) % 2 != 0:
            count += 1
            if min_odd_number is None or int(item) < int(min_odd_number):
                min_odd_number = item

    print(f"Количество чисел: {count}")
    if min_odd_number:
        print("Минимальное число прописью:", number_to_words(min_odd_number))

process_stream("1lab.txt")
