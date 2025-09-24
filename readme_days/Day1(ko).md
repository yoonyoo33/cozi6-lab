## 📘 Day1. 포트폴리오 (25.9.15)
**“파이썬 첫날: AI는 내 연대기를 요약하려 하고, 나는 AI에게 감정을 가르치려 하고, 결국 둘 다 실패한다.”** 
_기술로 감정을 정리하려는 창작자의 여정_

📂 실습 코드 보기: 날려서 없음.
> _“파이썬을 처음 접한 날, .ipynb 파일을 저장하는 방법을 몰라 실습 코드는 남기지 못했지만, Microsoft Copilot ‘이롯이’와의 대화를 통해 실험 과정과 결과를 기록했습니다.
NLP 모델을 직접 연결해 텍스트 요약, 감정 분석, 문장 분류를 시도했으며, 반복된 문장 출력, 숫자만 나오는 감정 분석, 해석이 어려운 분류 결과 등을 경험했습니다.
Mac 환경에서 VS Code를 사용하려 했으나 기능 미지원(2014년형 MacBook Pro)으로 Windows 환경으로 전환한 과정 역시 기술을 직접 다루고자 한 창작자의 첫 걸음이었습니다.”_

---
## 1️⃣ 프로젝트 개요
> 파이썬을 처음 접한 정현이가 Microsoft Copilot ‘이롯이’와 함께 진행한 프로젝트입니다.
텍스트 구조화와 요약 과정을 통해 NLP의 기본 개념을 실습하고, Google Colab에서 직접 코드 작성과 실행을 경험했습니다.
텍스트 분류, 요약, 감정 분석, 모델 조합, 환경 전환 등을 체험하며 감각을 익혔습니다.
 
---
## 2️⃣ 사용 기술 및 도구
| 기술/도구 | 설명 |
|-----------|------|
| Python | 기본 프로그래밍 언어 |
| Google Colab | 코드 실행 환경 |
| `re` 모듈 | 정규표현식을 활용한 텍스트 분류 |
| `TextBlob`, `KcBERT`, `KoElectra` | 감정 분석 실험 |
| `transformers` | NLP 모델 불러오기 |
| KoBART, BART, GPT | 텍스트 요약 모델 실험 |
| BERT-kor-base | 문장 분류 모델 실험 |
| MacBook → Windows | 환경 전환 실험 |
---
## 3️⃣ 주요 실습 내용
### 🔹 텍스트 정리기 만들기
- 나이 기준, 사건 기준, 감정 기준으로 텍스트 분류
- `re.split()`과 `re.findall()`을 활용해 구조화
- 마침표 없는 문장도 정리 가능하도록 개선
### 🔹 NLP 모델 연결 실험
- `pipeline()`으로 모델 불러오기
- 요약, 감정 분석, 문장 분류 모델을 동시에 적용
- 결과값 해석: `LABEL_0`, `LABEL_1`, `score` 등
### 🔹 반복 출력 및 모델 한계 체험
- 감정 중심 문장에 대해 요약 모델이 반복 출력
- 감정 분석 모델이 감정 이름 없이 숫자만 반환
- 분류 모델이 `LABEL_1`만 출력하고 해석 어려움
### 🔹 환경 전환 실험
- MacBook Pro(2014)에 파이썬 설치 → VS Code 실행 시도
- 기능 미지원으로 인해 Windows 환경으로 전환
- Colab에서의 느린 속도, GPU 제한, 오류 메시지 경험
---
## 4️⃣ 코드 예시
### 📌 세 가지 모델을 동시에 적용한 코드
```python
from transformers import pipeline
# 요약 모델
summarizer = pipeline("summarization", model="digit82/kobart-summarization")
# 감정 분석 모델
emotion_analyzer = pipeline("text-classification", model="beomi/kcbert-base")
# 문장 분류 모델
classifier = pipeline("text-classification", model="kykim/bert-kor-base")
text = """요즘은 숨 쉬는 것도 버거울 때가 있어요.
무언가를 시작하려 해도 마음이 따라주지 않고,
세상은 너무 빠르게 돌아가는데 나는 멈춰 있는 것 같아요."""
# 요약
summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
print("📝 요약:", summary[0]['summary_text'])
# 감정 분석
emotion = emotion_analyzer(text)
print("💬 감정 분석:", emotion)
# 문장 분류
category = classifier(text)
print("📂 문장 분류:", category)
```
---
## 5️⃣ 결과 분석 요약
| 모델 | 결과 경향 | 문제점 |
|------|-----------|--------|
| 요약 | 감정 문장을 반복하거나 강조 | 뉴스 기반 모델이 감정 중심 문장에 과몰입 |
| 감정 분석 | `LABEL_0`, `LABEL_1`만 출력됨 | 감정 이름 미정의, 추가 학습 필요 |
| 분류 | `LABEL_1`만 출력됨 | 의미 해석 어려움, 훈련 데이터 불일치 |
---
## 6️⃣ 학습 성과
- 파이썬 문법과 텍스트 처리 기초 이해  
- NLP 모델 구조와 파라미터 설정 방식 체득  
- 모델 출력값 해석 능력 향상 (`label`, `score`, 반복 현상 등)  
- 실전으로 부딪히며 모델의 한계와 구조를 이해함  
- 환경 전환 경험: Mac → Windows → Colab  
- 기술을 통해 감정을 정리하려는 창작자의 시선 획득

