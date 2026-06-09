def text_stats_tool(text:str):
    words = len(text.split())
    characters = len(text)
    return {'words':words,
            'characters':characters}