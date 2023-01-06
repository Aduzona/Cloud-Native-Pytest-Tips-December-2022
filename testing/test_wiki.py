from mylib.wiki import search_wiki

def test_search_wiki():
    assert "Celtics–Lakers rivalry" in search_wiki()