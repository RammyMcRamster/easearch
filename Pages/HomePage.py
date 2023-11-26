from taipy.gui import Html

def HomePage():
    return Html("""
        <taipy:layout columns="1 2 1">
            <taipy:part></taipy:part>
            <taipy:layout columns="1" class_name="card">
                <taipy:text class_name="h1">Find research with ease.</taipy:text>
                <taipy:input on_action=search class_name="fullwidth">{user_input}</taipy:input>
            </taipy:layout>
        </taipy:layout>
    """)