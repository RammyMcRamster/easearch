from taipy.gui import Html
from taipy import Gui
from Components.NavBar import NavBar
from Pages.HomePage import HomePage

root = NavBar()
home_page = HomePage()
article_page = "## Article Page"
search_page = "## Search Page"
stack_page = "## Stack Page"


pages = {
    "/": root,
    "home-page": home_page,
    "search-page": search_page,
    "stack-page": stack_page,
    "article-page": article_page,
}


Gui(pages=pages).run()