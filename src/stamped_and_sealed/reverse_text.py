def reverse_text(text: str, ignore_spaces: bool = False, ignore_punctuation: bool = False) -> str:
    """
    Reverses the given text.

    :param text: The input string to reverse.
    :param ignore_spaces: If True, spaces are removed before reversing.
    :param ignore_punctuation: If True, punctuation is removed before reversing.
    :return: The reversed string.
    """
    if ignore_spaces:
        text = text.replace(" ", "")
    if ignore_punctuation:
        text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text[::-1]
