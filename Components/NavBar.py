from taipy.gui import Html

def NavBar():
    return Html("""
        <taipy:layout columns="1 1 3">
            <taipy:image content="easesearchlogo.png"></taipy:image>
            <taipy:navbar lov={page_names}></taipy:navbar>
        </taipy:layout>
    """
    )