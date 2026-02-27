vowels = ('aeiou')

def _search_for_first_vowel(text):
    i = 0
    while i < len(text) and text[i] not in vowels:
        i += 1
    return i

def _search_for_qu(text: str) -> int:
    return text.find("qu")

def _search_for_y(text: str) -> int:
    return text.find("y")

def _pig_latin(text: str) -> str:
    
    t = text

    # Rule 1
    if t.startswith(("xr", "yt")) or t[0] in vowels:
        return t + "ay"

    # Rule 3: 
    qu_pos = _search_for_qu(text)
    if qu_pos != -1 and not any(ch in vowels for ch in t[:qu_pos]):
        split = qu_pos + 2 
        return text[split:] + text[:split] + "ay"

    # Rule 4:
    y_pos = _search_for_y(text)
    if y_pos > 0 and not any(ch in vowels for ch in t[:y_pos]):
        return text[y_pos:] + text[:y_pos] + "ay"

    # Rule 2: 
    i = _search_for_first_vowel(text)
    return text[i:] + text[:i] + "ay"


def translate(text: str) -> str:
    return " ".join(_pig_latin(word) for word in text.split())
