# Функція для перевірки, чи є два слова анаграмами
def are_anagrams(word1, word2):
    # Переводимо слова в нижній регістр
    word1 = word1.lower()
    word2 = word2.lower()

    # Перевіряємо, чи мають слова однакову кількість літер
    if len(word1) != len(word2):
        return False

    # Створюємо словник для зберігання кількості кожної літери у першому слові
    letter_count = {}

    # Заповнюємо словник для першого слова
    for letter in word1:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Перевіряємо, чи кожна літера у другому слові зустрічається у такій же кількості
    for letter in word2:
        if letter in letter_count:
            letter_count[letter] -= 1
        else:
            return False

    # Перевіряємо, чи всі значення у словнику рівні нулю
    return all(count == 0 for count in letter_count.values())
while True:

    # Зчитуємо два слова від користувача
    word1 = input("Введіть перше слово: ")
    word2 = input("Введіть друге слово: ")

    # Визначаємо, чи є вони анаграмами
    if are_anagrams(word1, word2):
        print(f"{word1} і {word2} є анаграмами.")
    else:
        print(f"{word1} і {word2} не є анаграмами.")
