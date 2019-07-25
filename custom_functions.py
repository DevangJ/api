html_escape_table = {
    "&": "&amp;",
    ">": "&gt;",
    "<": "&lt;",
    '"': "&quot;",
    "'": "&#x27;",
    "/": "&#x2F;"
}

url_escape_table = {
	"!"	:	"%21",
	"#"	:	"%23",
	"$"	:	"%24",
	"%"	:	"%25",
	"&"	:	"%26",
	"'"	:	"%27",
	"("	:	"%28",
	")"	:	"%29",
	"*"	:	"%2A",
	"+"	:	"%2B",
	","	:	"%2C",
	"/"	:	"%2F",
	":"	:	"%3A",
	";"	:	"%3B",
	"="	:	"%3D",
	"?"	:	"%3F",
	"@"	:	"%40",
	"["	:	"%5B",
	"]"	:	"%5D"
}


def url_escape(char):
    if url_escape_table[char]:
        return url_escape_table[char]
    else:
        return char


def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)