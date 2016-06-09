data_store = {
    'italy': ['spaghetti', 'pasta', 'fashion'],
    'fashion': ['paris', 'anything'],
    'paris': ['terrorism', 'bomb', 'cheese', 'france'],
    'cheese': ['holland', 'milk', 'wine'],
    'pasta': ['egg', 'meatball', 'cheese'],
    'egg': ['easter', 'hen', 'jesus'],
    'wine': ['miracle'],
    'miracle': ['jesus', 'bible']
}

def get_links(title):
    try:
        return data_store[title]
    except KeyError:
        return []
