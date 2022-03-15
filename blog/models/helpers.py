def custom_shorten(text, max_len):
    shortened_text = text[:max_len]
    if len(shortened_text) < len(text):
        shortened_text = shortened_text[:-5] + '[...]'
    return shortened_text