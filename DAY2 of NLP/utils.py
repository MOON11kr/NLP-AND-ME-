# utils.py

def read_uploaded_file(file):
    """
    Reads uploaded text file and decodes it to UTF-8 string.
    Returns empty string on failure.
    """
    try:
        return file.read().decode("utf-8")
    except Exception:
        return ""


def clean_multiline_input(text):
    """
    Cleans multiline keyword input into a list of stripped lines.
    """
    return [line.strip() for line in text.splitlines() if line.strip()]
