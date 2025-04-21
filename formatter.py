import re

def re_formatter(text):
    items = [x.strip() for x in text.split(",")]

    final = []
    for i in items:
        quantity_match = re.search(r"\d+\s?(kg|g|gm|ml|packets|pcs)?", i)
        if quantity_match:
            quantity = quantity_match.group()
            item = i.replace(quantity, "").strip()
        else:
            quantity = None
            item = i
        final.append({"item": item, "quantity": quantity})

    print(final)
    return final