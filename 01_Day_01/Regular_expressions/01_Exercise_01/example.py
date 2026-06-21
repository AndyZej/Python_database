import re


love_matches = re.findall(r"\blove\b", text_to_search, re.IGNORECASE)

sure_percent_matches = re.findall(r"<sure>%", text_to_search)

question_mark_words = re.findall(r"\b\w+\?", text_to_search)

fair_words = re.findall(r"\b\w*fair\w*\b", text_to_search, re.IGNORECASE)