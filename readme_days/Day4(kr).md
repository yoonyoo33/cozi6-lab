## 📘 Day4. 새로운 다이어리 기록기 시작 (25.9.22)  
“나는 오늘, 감정을 기록하는 첫 줄을 남겼다.  
코드는 나의 마음을 저장하고, AI는 나의 흐름을 읽는다.”  
_기술로 감정을 정리하려는 창작자의 여정_

이 코드는 Microsoft Copilot '이롯이'와 함께 작성된 것입니다.  
_본 활동은 정현이의 개인 다이어리를 기반으로 하는 기록 자동화 실험이며,  
표시되는 코드는 구조와 흐름을 보여주는 예시로 구성되었습니다._

**🧠 실습 흐름 보기**
- 📂 [실습 코드 보기](https://github.com/yoonyoo33/cozi6-lab/blob/master/modules/250922_journal.py)
- 📄 [결과 파일 보기](https://github.com/yoonyoo33/cozi6-lab/blob/master/indicator/250922_journal.txt)
- 🖥️ [터미널 로그 보기](https://github.com/yoonyoo33/cozi6-lab/blob/master/terminal_logs/250922_terminal_log.md)




---

### 🧠 활동 목표

- 정현이의 감정을 직접 다이어리처럼 입력하고 기록하는 자동화 시스템 구축  
- 날짜, 제목, 내용 구조화하여 `.txt` 파일로 저장  
- VS Code 환경에서 경로 설정, 파일 생성, 실행 흐름 이해  
- OneDrive 경로 문제 해결 및 로컬 폴더 설정  
- 감정 기록을 기반으로 향후 분석 및 시각화 준비

---

### 🛠️ 설치한 라이브러리 및 환경 설정

- Python 3.x (내장 모듈: datetime)
- Visual Studio Code (코드 작성 및 실행)
- Windows PowerShell (터미널 명령어 사용)
- 파일 경로: C:\Users\YOONYOO\Desktop\파이썬꼬꼬마
- OneDrive 경로 이슈 해결: Escritorio → Desktop으로 변경하여 파일 저장 문제 해결

---

### 🐯 감정 기록기 코드 예시

```python
from datetime import datetime

def write_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    title = input("오늘 글 제목을 입력하세요: ")
    content = input("오늘의 글을 적어주세요: ")

    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(f"날짜: {today}\n제목: {title}\n내용: {content}\n")
        f.write("-" * 40 + "\n")

    print("저장 완료! journal.txt 파일에서 확인해보세요. 📖")

write_journal()
```

---

### 🎯 결과 예시

- 실행 시 터미널에서 제목/내용 입력 → journal.txt 파일 자동 생성 및 저장
- 날짜, 제목, 내용이 구분되어 저장되어 데이터 분석 및 시각화에 활용 가능
- 경로 문제(OneDrive/Escritorio) 직접 해결, 파일 저장 위치 명확히 파악
- 저장 완료 메시지로 사용자 경험 개선

---

### 📚 학습 성과 요약

| 주제 | 성과 내용 |
|------|-----------|
| 🧠 경로 설정 실전 | OneDrive 경로 문제 직접 해결, Escritorio → Desktop 전환, 파일 저장 위치 명확히 이해 |
| 🧵텍스트 저장 | 날짜, 제목, 내용 구조화하여 .txt 파일로 자동 저장, append 모드로 여러 기록 누적 |
| 🤖 코드 흐름 이해 |함수 정의, 입력 처리, 파일 쓰기, 출력까지의 전체 흐름 직접 구현 |
| ⚠️ 오류 처리  | IndentationError, NameError 등 직접 경험하고 해결, import 누락 등 실전 디버깅 |
| 📊 출력값 확인 | 저장 메시지 출력 및 파일 생성 여부 즉시 확인, 사용자 경험 개선 |
| 🎨 캐릭터 수집 | “감정을 기록하는 AI 친구” 콘셉트로 코드에 감성 메시지 추가 |
| 🐯 AI와 협력 | Copilot '이롯이'와 함께 실전 개발, 문제 분석 및 해결 과정 체험 |

### 🌱 차후 발전 방향

- 입력값 유효성 검사(빈 값, 특수문자 등) 및 예외 처리 추가
- 기록을 .md, .pdf 등 다양한 포맷으로 저장하는 기능 확장
- 감정 분석, 키워드 추출, 시각화 등 데이터 활용 기능 추가
- GUI(그래픽 인터페이스)로 확장하여 사용성 개선
- 자동 백업, 검색, 날짜별 조회 등 부가기능 개발

---
