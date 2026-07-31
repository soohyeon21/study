# 베스트앨범

from collections import defaultdict

def solution(genres, plays):
    ## 장르별 frequency 확인
    gfreq = defaultdict(int)
    for i in range(len(genres)):
        gfreq[genres[i]] += plays[i]
    
    ## 장르별 우선순위 설정
    gorder = {}
    order = 1
    for k, v in sorted(gfreq.items(), key=lambda x:-x[1]):
        gorder[k] = order
        order += 1
    
    ## 노래 정보 정리
    # 장르별로 묶기 # {장르순위: [곡번호, 재생횟수]}
    music_by_genre = {gnum:[] for gnum in range(1, len(gorder)+1)}
    for p in range(len(genres)):
        music_by_genre[gorder[genres[p]]].append((p, plays[p]))
    
    # # (번호, 장르순위<=100, 재생횟수)
    # music = []
    # for k in range(len(genres)):
    #     music.append((k, gorder[genres[k]], plays[k]))
    # music.sort(key=lambda x:(x[1], -x[2], x[0]))
    # print(f"music", music)
    
    ## 장르별 2곡 선정
    album = []
    for gorder_num in range(1, len(gorder)+1):
        music_by_genre[gorder_num].sort(key=lambda x:(-x[1], x[0]))
        top2 = music_by_genre[gorder_num][:2]
        for song in top2:
            album.append(song[0])
    
    return album

pipt1 = ['classic', 'pop', 'classic', 'classic', 'pop']
pipt2 = [500, 600, 150, 800, 2500]
print(solution(pipt1, pipt2))
