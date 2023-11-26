from taipy.gui import Html
from taipy import Gui
from Components.NavBar import NavBar
from Pages.HomePage import HomePage
from Pages.ArticlePage import ArticlePage

root = NavBar()
home_page = HomePage()
article_page = ArticlePage()
search_page = "## Search Page"
stack_page = "## Stack Page"

pages = {
    "/": root,
    "home": home_page,
    "explore": search_page,
    "stacks": stack_page,
    "article-page": article_page,
}