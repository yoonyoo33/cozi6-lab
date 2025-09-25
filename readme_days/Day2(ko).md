## 📘 Day2. 감성 분석 포트폴리오 (25.9.16)
**“AI는 내 다이어리를 통해 나를 예측하고, 나는 오늘도 감정을 가르치려 고군분투 진행중”**  
_기술로 감정을 정리하려는 창작자의 여정_

**🧠 실습 흐름 보기**
- 📂 [실습 코드 보기](https://github.com/yoonyoo33/cozi6-lab/blob/master/modules/250916Python_Day2.ipynb)
> _이 코드는 Microsoft Copilot ‘이롯이’와 함께 작성한 것입니다._
> _본 실습은 정현이의 개인 다이어리를 기반으로 진행되었으며, 공개된 코드는 구조와 흐름을 보여주기 위한 예시 문장으로 대체되었습니다.
---
### 🧠 실습 목표
- 정현이의 감정이 담긴 다이어리 문장을 기반으로  
  → 사전 학습된 감정 분석 모델을 활용해 감정 예측 실험  
- 키워드 기반 감정 점수 계산  
- 실행 시간 측정, 오류 해결, 모델 구조 이해  
- 포트폴리오로 정리하여 학습 흐름 기록
---
### 🛠️ 설치한 라이브러리
```python
!pip install transformers torch sentencepiece datasets scikit-learn pandas numpy matplotlib seaborn
```
- 설치 중 오류 발생: `sklearn` → `scikit-learn`으로 수정
- 설치 완료 후 `import torch`로 버전 확인
```python
import torch
print("PyTorch 버전:", torch.__version__)
```
---
### 🐯 감정 분석 모델 실험
```python
import time
start = time.time()
import torch
from transformers import pipeline
emotion_model = pipeline(
    "text-classification",
    model="tae898/emoberta-base",
    tokenizer="tae898/emoberta-base",
    framework="pt",
    max_length=512,
    truncation=True
)
diary = """ 
오늘은 마음이 조금 무거웠다. 하지만 작은 희망이 스며들었다.
(중략: 정현이의 긴 다이어리 텍스트)
"""
result = emotion_model(diary)
print("예측된 감정:", result)
end = time.time()
print(f"실행 시간: {end - start:.2f}초")
```
---
### 🎯 결과 예시
```python
예측된 감정: [{'label': 'joy', 'score': 0.7559}]
실행 시간: 3.22초
```
- 모델은 정현이의 다이어리에서 **기쁨(joy)** 감정을 가장 강하게 감지
- `score`는 모델의 확신도 (75% 이상 확신)
---
### 🧪 키워드 기반 감정 점수 분석
```python
positive_words = ["고마워", "지켜줘서", "멋있어", "잘될거니까", "행복하게", "닮고 싶어", "믿어", "회복", "자존감"]
negative_words = ["훼손", "낮춰", "미안해", "지치고", "힘들었던", "몰아가지", "프레임화", "계산적이다"]
pos_score = sum(word in diary for word in positive_words)
neg_score = sum(word in diary for word in negative_words)
total_score = pos_score - neg_score
print(f"긍정 키워드 수: {pos_score}")
print(f"부정 키워드 수: {neg_score}")
print(f"감정 점수: {total_score}")
if total_score > 0:
    print("🌈 오늘은 자기 회복과 희망이 가득한 날이야. 호랑이 컴퓨터가 정현이를 지켜보고 있어!")
elif total_score < 0:
    print("🌧 감정의 파도가 있었지만, 그 안에 단단한 자존감이 살아있어. 정현이는 흔들리지 않아.")
else:
    print("🌫 균형 속에서 자기 대화를 이어가는 날. 감정은 복합적이지만, 정현이는 중심을 잡고 있어.")
```
---
## 📚 학습 성과 요약
| 주제 | 성과 내용 |
|------|-----------|
| 🧠 파이썬 문법 실전 | `import`, `print`, 줄바꿈 오류, 한 줄에 여러 명령어 쓰기 등 직접 부딪히며 문법 감각 체득 |
| 🧵 텍스트 처리 | 긴 다이어리 텍스트를 변수에 담고, 줄바꿈/토큰 제한 문제 해결 |
| 🤖 NLP 모델 사용법 | `pipeline()` 함수 구조 이해, `model`, `tokenizer`, `framework` 설정 방식 학습 |
| ⚠️ 오류 디버깅 | `NameError`, `SyntaxError`, `RuntimeError` 등 다양한 에러를 직접 해결하며 구조 파악 |
| 🧬 모델 한계 이해 | 512 토큰 제한, truncation 옵션의 필요성, 모델이 감정 예측하는 방식 체득 |
| 📊 출력값 해석 | `label`, `score`의 의미 파악, 모델이 왜 joy라고 판단했는지 감정 흐름 분석 |
| ⏱ 실행 시간 측정 | `time.time()`으로 코드 성능 확인, 실전 개발 흐름 경험 |
| 🎨 창작자의 시선 획득 | 기술을 통해 자기 감정을 정리하고 표현하는 새로운 방식 체험 (“호랑이 컴퓨터야…”)
| 🐯 AI와의 협업 감각 | 이롯이와 함께 문제 해결하며 감정 분석 여정 동행, 대화형 학습의 즐거움 체험
