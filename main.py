from taipy import Gui
from taipy.gui import navigate
from app import pages
import requests as req

user_input = "Search..."
page_names = [('home', 'Home'), ('explore', 'Explore'), ('stacks', 'MyStacks')]

url = "https://api.crossref.org/works"
search_results = []

def search(state):
    query = state.user_input
    try:
        data = req.get(url + '?query=' + query + "&rows=1000&filter=full-text.type:application/pdf").json()
    except Exception as e:
        print(e)

    results = data["message"]["items"]

    search_results = []
    
    for result in results:
        if (result["reference-count"] >= 10):
            search_results.append(result) 
    
    state.search_results = search_results
    navigate(state, "article-page")
        

Gui(pages=pages).run()