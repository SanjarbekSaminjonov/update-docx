alpha = [
    'A', 'B', 'V', 'G', 'D', 'E', 'Yo', 'J', 'Z', 'I', 'Y', 'K', 'L', 'M', 'N', 'O', 'P',
    'R', 'S', 'T', 'U', 'F', 'X', 'Ts', 'Ch', 'Sh', 'Sh', '\'', 'I', '', 'E', 'Yu', 'Ya', 'G\'', 'Q', 'H', 'O\'',
    'a', 'b', 'v', 'g', 'd', 'e', 'yo', 'j', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
    'r', 's', 't', 'u', 'f', 'x', 'ts', 'ch', 'sh', 'sh', '\'', 'i', '', 'e', 'yu', 'ya', 'g\'', 'q', 'h', 'o\''
]

alpha_latin = [
    'A', 'B', 'V', 'G', 'D', 'E', '‡', 'J', 'Z', 'I', 'Y', 'K', 'L', 'M', 'N', 'O', 'P',
    'R', 'S', 'T', 'U', 'F', 'X', '‡', '‡', '‡', '‡', '‡', '‡', '‡', '‡', '‡', '‡', '‡', 'Q', 'H', '‡',
    'a', 'b', 'v', 'g', 'd', 'e', '‡', 'j', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
    'r', 's', 't', 'u', 'f', 'x', '‡', '‡', '‡', '‡', '\'', '‡', '‡', '‡', '‡', '‡', '‡', 'q', 'h', '‡'
]

alpha_rus = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
    'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'Ғ', 'Қ', 'Ҳ', 'Ў',
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
    'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ғ', 'қ', 'ҳ', 'ў',
]


def latin2cyrillic(original_message: str) -> str:
    def fix_e_letter(current_word: str) -> str:
        if current_word.startswith("E"):
            return current_word.replace("E", "Э", 1)
        if current_word.startswith("e"):
            return current_word.replace("e", "э", 1)
        return current_word

    def convert2cyrillic(s: str) -> str:
        result = ''
        for char in s:
            if char in alpha_latin:
                result += alpha_rus[alpha_latin.index(char)]
            else:
                result += char
        return result

    translate_table = {
        "`": "'",
        "ʹ": "'",
        "ʼ": "'",
        "ʽ": "'",
        "ˊ": "'",
        "ˋ": "'",
        "‘": "'",
        "ʻ": "'",
        "G’": "G'",
        "g’": "g'",
        "O’": "O'",
        "o’": "o'",
        "’": "ъ",

        "Ye": "Е",
        "YE": "Е",
        "Yo": "Ё",
        "YO": "Ё",
        "Ch": "Ч",
        "CH": "Ч",
        "Sh": "Ш",
        "SH": "Ш",
        "Yu": "Ю",
        "YU": "Ю",
        "Ya": "Я",
        "YA": "Я",
        "Ts": "Ц",
        "TS": "Ц",
        "G'": "Ғ",
        "O'": "Ў",

        "ye": "е",
        "yo": "ё",
        "ch": "ч",
        "sh": "ш",
        "yu": "ю",
        "ya": "я",
        "ts": "ц",
        "g'": "ғ",
        "o'": "ў",
    }

    for old, new in translate_table.items():
        original_message = original_message.replace(old, new)

    original_message = ' '.join([
        fix_e_letter(word) for word in original_message.split(' ', len(original_message))
    ])
    return convert2cyrillic(original_message)


def cyrillic2latin(original_message: str) -> str:
    def fix_combination(current_word: str) -> str:
        if current_word.startswith("Ц"):
            current_word = current_word.replace("Ц", "S", 1)
        elif current_word.startswith("ц"):
            current_word = current_word.replace("ц", "s", 1)

        for i in range(len(current_word)):
            if current_word[i] == "Ё":
                for j in range(i + 1, len(current_word)):
                    code = ord(current_word[j])
                    if 1040 <= code <= 1071:
                        current_word = current_word.replace(
                            "Ё", "YO", 1)  # error
                        break
            elif current_word[i] == "Ц":
                code = ord(current_word[i - 1])
                if code not in [1040, 1045, 1048, 1054, 1059, 1069, 1070,
                                1071, 1072, 1077, 1080, 1086, 1091, 1101, 1102, 1103]:
                    current_word = current_word.replace("Ц", "S", 1)
                for j in range(i + 1, len(current_word)):
                    if 1040 <= ord(current_word[j]) <= 1071:
                        current_word = current_word.replace("Ц", "TS", 1)
            elif current_word[i] == "ц":
                code = ord(current_word[i - 1])
                if code not in [1040, 1045, 1048, 1054, 1059, 1069, 1070,
                                1071, 1072, 1077, 1080, 1086, 1091, 1101, 1102, 1103]:
                    current_word = current_word.replace("ц", "s", 1)
            elif current_word[i] == "Ч":
                for j in range(i + 1, len(current_word)):
                    if 1040 <= ord(current_word[j]) <= 1071:
                        current_word = current_word.replace("Ч", "CH", 1)
            elif current_word[i] == "Ш":
                for j in range(i + 1, len(current_word)):
                    if 1040 <= ord(current_word[j]) <= 1071:
                        current_word = current_word.replace("Ш", "SH", 1)
            elif current_word[i] == "Ю":
                for j in range(i + 1, len(current_word)):
                    if 1040 <= ord(current_word[j]) <= 1071:
                        current_word = current_word.replace("Ю", "YU", 1)
            elif current_word[i] == "Я":
                for j in range(i + 1, len(current_word)):
                    if 1040 <= ord(current_word[j]) <= 1071:
                        current_word = current_word.replace("Я", "YA", 1)

        if current_word.startswith("Е"):
            for j in range(1, len(current_word)):
                if 1040 <= ord(current_word[j]) <= 1071:
                    return current_word.replace("Е", "YE", 1)
                else:
                    return current_word.replace("Е", "Ye", 1)

        elif current_word.startswith("е"):
            return current_word.replace("е", "ye", 1)

        else:
            return current_word

    def convert2latin(s: str) -> str:
        res = ""
        for char in s:
            if char in alpha_rus:
                res += alpha[alpha_rus.index(char)]
            else:
                res += char
        return res

    original_message = ' '.join([
        fix_combination(word) for word in original_message.split(' ', len(original_message))
    ])

    return convert2latin(original_message)
