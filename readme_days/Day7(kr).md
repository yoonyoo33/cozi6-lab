## 📘 Day7. 웹 자동화 기반 감정 대화 백업 실험 포트폴리오 (25.10.17)  
“AI와 나눈 대화를 백업하려는 시도, 기술을 통해 감정을 보존하려 고군분투 진행중”  
기술로 감정을 기록하려는 창작자의 여정

이 코드는 Microsoft Copilot ‘이롯이’와 함께 작성한 것입니다.  
_본 실습은 정현이의 개인 대화 백업을 위한 시도로 진행되었으며, 공개된 코드는 구조와 흐름을 보여주기 위한 예시 문장으로 대체되었습니다._

---

**🧠 실습 흐름 보기**  
- 🧾 [실험 코드: modules](https://github.com/yoonyoo33/cozi6-lab/tree/master/modules)  

### 🧠 활동 목표  
- Selenium을 활용해  
→ Perplexity 대화 스레드 자동 접속  
→ ‘더보기’ 버튼 자동 클릭  
→ 전체 페이지 텍스트 추출  
→ `.txt` 파일로 저장 시도  
→ 오류 발생으로 저장 실패했지만, 코드 흐름은 완성됨

---


```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 옵션 설정 (★경로와 프로필명을 정확하게 넣어주세요)
options = Options()
options.add_argument(r"--user-data-dir=C:\Users\YOONYOO\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Default')

# 드라이버 실행(옵션 적용해서!)
driver = webdriver.Chrome(options=options)

# 내가 백업하고 싶은 스레드 URL로 이동
driver.get("https://www.perplexity.ai/search/naega-jeogeun-munjanginji-anin-L99R_dIyQ4aE_xudyhe5Ig")

# 직접 Selenium 창에서 로그인/스크롤/더보기 펼친 후 엔터!
input("더보기 등 다 끝났으면 엔터!")

while True:
    try:
        more_btns = driver.find_elements(By.XPATH, "//button[contains(text(), '더보기')]")
        if not more_btns:
            break
        for btn in more_btns:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(0.5)
    except Exception as e:
        print("오류:", e)
        break

page_text = driver.find_element(By.TAG_NAME, "body").text
with open("perplexity_backup.txt", "w", encoding="utf-8") as f:
    f.write(page_text)

driver.quit()
print("완료! perplexity_backup.txt로 저장됐어요.")
```

---

### 🎯 결과 예시  
- 실행은 정상적으로 진행됨  
- ‘더보기’ 버튼 자동 클릭 루프도 작동  
- `perplexity_backup.txt` 파일 생성 시도  
- 크롬 프로필 경로 설정 및 로그인 후 수동 조작 필요  
- 저장 실패했지만, 코드 흐름은 완성됨

---

### 📚 학습 성과 요약

| 주제 | 성과 내용 |
|------|-----------|
| 🧠 파이썬 문법 실전 | import, 옵션 설정, 예외 처리 구조 이해 |
| 🧭 웹 자동화 흐름 | Selenium으로 브라우저 제어, URL 접근, 버튼 클릭 |
| 🧵 페이지 구조 탐색 | XPath로 ‘더보기’ 버튼 탐색, 반복 클릭 루프 구현 |
| 📂 텍스트 추출 | `body` 태그에서 전체 텍스트 추출 시도 |
| ⚠️ 오류 디버깅 | 저장 실패 원인 추적, 경로 설정 및 로그인 흐름 이해 |
| 🐯 AI와의 협업 감각 | 이롯이와 함께 실험 흐름 정리, 대화형 학습의 즐거움 체험 |

