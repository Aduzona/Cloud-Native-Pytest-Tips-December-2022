import wikipedia

def search_wiki(term="Lakers"):
    """ This search is for pages in Wikipedia"""
    return wikipedia.search(term)