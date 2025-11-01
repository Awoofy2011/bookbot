#python
def sort_char_counts(counts):
    items = []
    for CH, N in counts.items():
        # skip non-letters
        if not CH.isalpha():
            continue
        items.append({"char": CH, "num": N})

    def sort_on(ITEM):
        return ITEM["num"]  #sort by the count

    items.sort(key=sort_on, reverse=True)
    return items

def get_char_counts(text: str):
    counts = {}
    for ch in text:  # iterate each character
        ch = ch.lower()  # unify case
        if ch not in counts:
           counts[ch] = 0
        counts[ch] = counts[ch] + 1
    return counts

def get_book_text(filepath):
    with open(filepath) as f:
         return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)
