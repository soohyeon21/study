# 86491
# 최소직사각형

# (w, h)가 항상 w>h가 되도록 설정.

def solution(sizes):
    resize = [(max(card), min(card)) for card in sizes]
    max_w = max(w for w, h in resize)
    max_h = max(h for w, h in resize)
    
    return max_w * max_h
