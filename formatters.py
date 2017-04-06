import models
import re

def markdown_remove(s):
    if s:
        s = "".join(s.split("\\r\\n"))
        for index in range(0,len(re.findall(r"[^[]*\[([^]]*)\]", s))):
            s = re.sub(r'\[.*?\]\((.*?)\)', re.findall(r"[^[]*\[([^]]*)\]", s)[0], s, count=1)
    return s

