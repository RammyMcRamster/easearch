from taipy.gui import Html

def ArticlePage():
    return Html ("""
        <taipy:text>{search_results[0].abstract}</taipy:text>
    """
    )