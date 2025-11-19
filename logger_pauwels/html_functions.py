def get_start():
    """ Give the start of the html file """
    return """
<!DOCTYPE html>

<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Logs Pauwels</title>
<style>
    body {
        font-family: 'Courier New', monospace;
        background-color: #f4f4f4;
        color: #333;
        padding: 20px;
        font-weight: bold;
        font-size: 2vh;
    }

/* Ligne pleine avec texte centré */
.line-header {
    width: 100vw;
    display: flex;
    align-items: center;
    text-align: center;
    font-weight: bold;
    font-size: 1.2em;
    margin: 20px 0;
    color: #0000ff
}
.line-header::before,
.line-header::after {
    content: "";
    flex: 1;
    border-bottom: 2px solid #0000ff;
}
.line-header::before {
    margin-right: 10px;
}
.line-header::after {
    margin-left: 10px;
}

/* Cadre */
.frame-header {
    border: 3px solid #ff0000;
    color: #ff0000;
    padding: 20px;
    text-align: center;
    font-weight: bold;
    font-size: 1.2em;
    margin-bottom: 20px;
    background-color: #fff;
}

/* Logs */
.log-entry {
    background-color: #fff;
    padding: 10px 15px;
    margin-bottom: 5px;
    border-left: 4px solid #000000; /* Couleur par défaut */
    color: #000000;
    white-space: pre-wrap;
}

/* Types de logs */
.log-warning {
    border-left-color: magenta;
    color: magenta;
}
.log-error {
    border-left-color: red;
    color: red;
    font-weight: bold;
}
.log-debug {
    border-left-color: orange;
    color: orange;
}
.log-failed {
    border-left-color: darkred;
    color: darkred;
    font-weight: bold;
}
.log-success {
    border-left-color: green;
    color: green;
    font-weight: bold;
}

/* Progress bar */
.progress-bar {
    margin-top: 20px;
    font-style: italic;
    text-align: center;
}

</style>
</head>
<body>\n"""

def get_end():
    """ End of html file """
    return """</body>
</html>"""

def get_cadre(msg):
    """ Something that looks like a cadre """
    return f"""<div class="frame-header">{msg}</div>\n"""
    
def get_section(msg):
    """ Something that looks like a section """
    return f"""<div class="line-header">{msg}</div>\n"""

def get_log(msg):
    """ Log line for HTML """
    return f"""<div class="log-entry log-entry">{msg}</div>\n"""

def get_debug(msg):
    """ Debug log line for HTML """
    return f"""<div class="log-entry log-debug">{msg}</div>\n"""

def get_warn(msg):
    """ Warning log line for HTML """
    return f"""<div class="log-entry log-warning">{msg}</div>\n"""

def get_error(msg):
    """ Error log line for HTML """
    return f"""<div class="log-entry log-error">{msg}</div>\n"""

def get_failed(msg):
    """ Failed log line for HTML """
    return f"""<div class="log-entry log-failed">{msg}</div>\n"""

def get_succes(msg):
    """ Success log line for HTML """
    return f"""<div class="log-entry log-success">{msg}</div>\n"""