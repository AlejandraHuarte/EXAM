def is_valid_url(url):
    """
    Function to check if a string is a valid URL based on basic conditions
    :param url: The string to check
    :return: True if the string follows a basic URL structure, otherwise False
    """
    if url.startswith("http://") or url.startswith("https://"):
        if "." in url and " " not in url:  # Ensuring there is a domain and no spaces
            return True
    return False

# Example usage
print(is_valid_url("https://www.example.com"))
print(is_valid_url("http://example.org"))
print(is_valid_url("www.example.com"))
print(is_valid_url("htp://example.com"))
print(is_valid_url("https://example com"))