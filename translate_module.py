

def translate_mes(mes):
    global src_gl
    global dest_gl
    if dest_gl == 'en':
        lang_mes = mes
    else:
        lang_mes = translator.translate(mes, src = src_gl, dest = dest_gl).text
    return lang_mes

def translate_mes_API(mes):
    '''TODO understand how to get API key and which instrument better use, add more languages'''
    pass 