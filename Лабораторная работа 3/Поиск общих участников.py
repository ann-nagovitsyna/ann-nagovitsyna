def count_letters(text):

    russian_alphabet = [
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
        'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
        'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
        'э', 'ю', 'я'
    ]

    # Инициализируем словарь с нулевыми значениями для каждой буквы
    letter_counts = {letter: 0 for letter in russian_alphabet}

    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                pass
    return letter_counts


def calculate_frequency(letter_counts):

    total_letters = sum(letter_counts.values())
    if total_letters == 0:
        return {letter: 0 for letter in letter_counts}

    letter_frequencies = {}
    for letter, count in letter_counts.items():
        frequency = count / total_letters
        letter_frequencies[letter] = frequency
    return letter_frequencies


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_counts = count_letters(main_str)

# Вычисление частот
letter_frequencies = calculate_frequency(letter_counts)

ordered_letters = [
    'у', 'л', 'к', 'о', 'м', 'р', 'ь', 'я',
    'д', 'б', 'з', 'е', 'ё', 'н', 'ы', 'й',
    'а', 'т', 'ц', 'п', 'и', 'ч', 'ю', 'в',
    'с', 'х', 'г', 'ш', 'ж', 'щ'
]

for letter in ordered_letters:
    frequency = letter_frequencies.get(letter, 0)
    print(f"{letter}: {frequency:.2f}")