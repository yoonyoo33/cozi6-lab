import time
start = time.time()

import json # JSON 파일을 불러오기 위해 필요해요!
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams # 폰트 설정을 위해 불러와요!
matplotlib.use('TkAgg') # 그래프 창을 띄우는 설정 (이전과 동일)

# 👇️ 한글 폰트 설정 추가
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False


# --- 1. emotion_keywords.json 파일에서 단어 불러오기 ---
try:
    with open('emotion_keywords.json', 'r', encoding='utf-8') as f:
        emotion_data = json.load(f)
    
    # JSON에서 긍정/부정 단어 리스트를 가져옵니다.
    positive_words = emotion_data['positive_words']
    negative_words = emotion_data['negative_words']
    
    print("✅ 감정 키워드 데이터 불러오기 성공!")

except FileNotFoundError:
    print("❌ 에러: emotion_keywords.json 파일이 없습니다!")
    print("먼저 emotiontraining_250926.py 파일을 실행해서 키워드를 생성해주세요.")
    positive_words = []
    negative_words = []
except Exception as e:
    print(f"❌ 데이터 로드 중 에러 발생: {e}")
    positive_words = []
    negative_words = []


#파일 존재 여부 확인 (기존 코드와 동일)
import os
# output.txt가 존재하지 않는다는 False 메시지가 나오는 것은 이 파일이 없다는 뜻이에요.
print("output.txt 존재 여부:", os.path.exists("output.txt")) 

#데이터 변수 출력해보기
print("긍정 단어 예시:", positive_words[:10])
print("부정 단어 예시:", negative_words[:10])

#데이터 길이 확인
print("긍정 단어 수:", len(positive_words))
print("부정 단어 수:", len(negative_words))

# --- 2. 시각화 (한글 폰트 적용됨) ---
labels = ['긍정', '부정']
counts = [len(positive_words), len(negative_words)]

plt.bar(labels, counts, color=['skyblue', 'salmon'])
plt.title("감정 단어 분포 (상위 100개)")
plt.ylabel("단어 수")
plt.show()

end = time.time()
print(f"실행 시간: {end - start:.2f}초")