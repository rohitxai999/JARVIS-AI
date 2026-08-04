SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi"
}


def get_language(code):
    return SUPPORTED_LANGUAGES.get(code, "Unknown")