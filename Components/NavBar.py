from taipy.gui import Html
from taipy import Gui

def NavBar():
    return Html("""
        <taipy:layout columns="1 1 3">
            <taipy:image content="../easesearchlogo.png"></taipy:image>
            <taipy:navbar></taipy:navbar>
        </taipy:layout>
    """
    )