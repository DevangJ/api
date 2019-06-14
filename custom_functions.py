html_escape_table = {
    "&": "&amp;",
    ">": "&gt;",
    "<": "&lt;",
    '"': "&quot;",
    "'": "&#x27;",
    "/": "&#x2F"
    }

def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)