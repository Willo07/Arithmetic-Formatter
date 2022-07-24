def right_align(number_available_characters: int, characters_to_show: str, displacement: int = 0):
    number_blank_spaces = number_available_characters - (len(characters_to_show) + displacement)
    right_aligned_text = (" " * number_blank_spaces) + characters_to_show
    return right_aligned_text



