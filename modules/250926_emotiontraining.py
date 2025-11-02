import time
start = time.time()

import json  # JSON 파일을 다루는 도구를 불러와요!
from collections import Counter
from konlpy.tag import Okt

try:
    print("파일 열기 시도 중!")

    # 파일 열기
    with open('training.json', 'r', encoding='utf-8') as f:
        data = json.load(f)  # JSON 파일을 파이썬에서 읽어서 'data'에 저장해요!

    print("파일 불러오기 성공!")
    print(data[0])  # 첫 번째 데이터 확인해보기

except Exception as e:
    print("에러 발생:", e)

print("전체 항목 수:", len(data))

for i in range(3):  # 앞에서 3개만 보기
    print(f"\n--- 항목 {i+1} ---")
    print(data[i])

# 긍정/부정 감정 코드 정의
positive_codes = {'E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10'}
negative_codes = {'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27'}

# 문장 담을 리스트
positive_texts = []
negative_texts = []

# 전체 항목 반복하면서 분류하기
for item in data:
    emotion_type = item['profile']['emotion']['type']
    content = item['talk']['content'].values()  # 문장들만 꺼내기

    if emotion_type in positive_codes:
        positive_texts.extend(content)
    elif emotion_type in negative_codes:
        negative_texts.extend(content)

# 결과 확인
print("긍정 문장 수:", len(positive_texts))
print("부정 문장 수:", len(negative_texts))

# 형태소 분석
okt = Okt()

def extract_keywords(texts):
    words = []
    for sentence in texts:
        tokens = okt.nouns(sentence)  # 명사만 추출
        words.extend(tokens)
    return Counter(words)

# 키워드 추출
positive_keywords = extract_keywords(positive_texts).most_common(100)
negative_keywords = extract_keywords(negative_texts).most_common(100)

# 리스트 저장
positive_words = [word for word, _ in positive_keywords]
negative_words = [word for word, _ in negative_keywords]


end = time.time()
print(f"실행 시간: {end - start:.2f}초")