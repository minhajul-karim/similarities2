import nltk
# nltk.download('punkt')


def lines(a, b):
    """Return lines in both a and b"""
    # Split strings into lists
    list1 = a.split('\n')
    list2 = b.split('\n')

    # Remove duplicates from both lists and find the common elements
    list_of_common_lines = list(set(list1) & set(list2))
    return list_of_common_lines


def sentences(a, b):
    """Return sentences in both a and b"""
    # Split strings into sentences
    list1 = nltk.sent_tokenize(a)
    list2 = nltk.sent_tokenize(b)

    # Remove duplicates from both lists and find the common elements
    list_of_common_sentences = list(set(list1) & set(list2))
    return list_of_common_sentences


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    # Length of string a & b
    length1 = len(a)
    length2 = len(b)
    
    # Create 2 lists to contain substrings
    list1 = []
    list2 = []
    
    # Append substrings of a in list1
    i = 0
    while (i+n <= length1):
        list1.append(a[i:(i+n)])
        i = i + 1

    # Append substrings of a in list2
    i = 0
    while (i+n <= length2):
        list2.append(b[i:(i+n)])
        i = i + 1
    
    # Remove duplicates from both lists and find the common elements
    list_of_common_substrings = list(set(list1) & set(list2))
    return list_of_common_substrings
