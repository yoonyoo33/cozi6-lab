## 📘 Day5. 감정 기록의 시각화와 자동화 (25.9.23)

> “기록은 나를 정리하고, 기술은 책으로 엮는다.  
먹 번짐처럼 퍼지는 감정의 여운을, PDF와 이미지로 남긴 하루.  
그리고 그 책이 태어나는 과정을 조용히 기다리는 밤.”
_기술로 감정을 정리하려는 창작자의 여정_

이 코드는 Microsoft Copilot '이롯이'와 함께 작성된 것입니다.  
_본 활동은 정현이의 개인 다이어리를 기반으로 하는 기록 자동화 실험이며,  
표시되는 코드는 구조와 흐름을 보여주는 예시로 구성되었습니다._

**🧠 실습 흐름 보기**
- 📂 [실습코드:PDF 변환](https://github.com/yoonyoo33/cozi6-lab/blob/master/modules/250923_upgradejournal.py)
- 🎨 [실습코드:먹 번짐 이미지](https://github.com/yoonyoo33/cozi6-lab/blob/master/images/250923_sumi_dot.py)
- 📄 [결과 파일 보기](https://github.com/yoonyoo33/cozi6-lab/blob/master/images/250923_MyDiary.pdf)
- 🖥️ [터미널 로그 보기](https://github.com/yoonyoo33/cozi6-lab/blob/master/terminal_logs/250923_terminal_log.txt)

---

### 🧠 활동 목표

- `.md` 형식으로 저장된 감정 일기를 PDF로 자동 변환  
- 표지 생성, 본문 병합, 목차 포함  
- `tqdm`으로 병합 진행률 시각화  
- `print()` 로그로 단계별 흐름 안내  
- `time.time()`으로 실행 시간 측정  
- PIL을 활용한 먹 번짐 이미지 생성  
- MiKTeX 설치로 PDF 렌더링 환경 구축  
- 시스템 성능 분석 및 디버깅 루틴 수립
- 한글 폰트 깨짐 문제 해결 및 폰트 매핑 전략 수립


---

### 🛠️ 설치한 라이브러리

```bash
pip install pypandoc tqdm pillow
```

- `pypandoc`: Markdown → PDF 변환용  
- `tqdm`: 병합 진행률 시각화  
- `Pillow`: 이미지 생성 및 필터 적용  
- MiKTeX: Pandoc의 PDF 렌더링을 위한 LaTeX 환경

---

### 🐯 PDF 변환 자동화 코드

```python
import os, time, pypandoc
from tqdm import tqdm

def make_pdf_book():
    start = time.time()
    print("🚀 PDF 변환 시작!")

    folder = "journals"
    output = "MyDiary.pdf"
    os.makedirs(folder, exist_ok=True)

    print("📄 .md 파일 불러오는 중...")
    files = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".md")])
    if not files:
        print("⚠️ 변환할 일기 파일이 없습니다.")
        return

    print("🧾 표지 생성 중...")
    cover_text = """\
# 살랑, 살랑

![](sumi_dot.jpg)

by Jasmine  
(초롱이와 함께한 순간들)

---
"""
    cover_file = os.path.join(folder, "0000-cover.md")
    with open(cover_file, "w", encoding="utf-8") as f:
        f.write(cover_text)
    print("✅ 표지 생성 완료!")

    print("📦 파일 병합 중...")
    all_files = [cover_file] + files
    merged_content = ""
    for f in tqdm(all_files, desc="📄 병합 진행"):
        with open(f, encoding="utf-8") as file:
            merged_content += file.read() + "\n\n"
    print("✅ 파일 병합 완료!")

    print("🖨️ PDF 변환 중 (잠시 기다려주세요)...")
    pypandoc.convert_text(
        merged_content,
        "pdf",
        format="md",
        outputfile=output,
        extra_args=[
            "--pdf-engine=xelatex",
            "--variable=mainfont=NanumGothic Light",
            "--standalone",
            "--toc",
            "--toc-depth=2"
        ]
    )

    print(f"✅ PDF 변환 완료! '{output}' 파일을 확인하세요.")
    end = time.time()
    print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")

make_pdf_book()

---

### 🎨 먹 번짐 이미지 생성 코드

```python
from PIL import Image, ImageDraw, ImageFilter

img = Image.new("RGB", (500, 500), "white")
draw = ImageDraw.Draw(img)

draw.ellipse((230, 230, 270, 270), fill=(10, 10, 10))
draw.ellipse((215, 215, 285, 285), fill=(90, 80, 80))
blurred = img.filter(ImageFilter.GaussianBlur(3))
draw.ellipse((190, 190, 310, 310), fill=(200, 200, 200))

blurred.save("sumi_dot_soft.jpg")
print("sumi_dot_soft.jpg 저장 완료!")
```

---

### 🧪 디버깅 루틴

```text
1단계: "# 테스트" 내용으로 PDF 변환만 실행 → Pandoc 정상 여부 확인  
2단계: 이미지 삽입 제거 후 원래 코드 실행 → 이미지 렌더링 문제 확인  
3단계: 컴퓨터 재부팅 → 메모리 초기화 및 프로세스 리셋
```

### 🧠 문제 해결 흐름 요약

| 문제 | 해결 방법 |
|------|-----------|
| PDF에 한글 깨짐 | `mainfont=NanumGothic Light`로 정확한 폰트 지정 |
| 이미지에 Figure 캡션 자동 생성 | `![](sumi_dot.jpg)`로 설명 제거 |
| `.md` 파일 누락 | 확장자 확인 및 `.txt` → `.md`로 변경 |
| VS Code 중단점 오류 | 디버깅 세션 재시작으로 해결 |

---

### 📚 학습 성과 요약

| 주제 | 성과 내용 |
|------|-----------|
| 📁 파일 자동화 | `os.makedirs()`로 폴더 생성, `.md` 병합 |
| 🖨️ PDF 변환 | `pypandoc.convert_text()`로 PDF 생성 |
| 📊 진행률 시각화 | `tqdm`으로 병합 흐름 표시 |
| 🧾 로그 설계 | `print()`로 단계별 안내 메시지 구성 |
| ⏱️ 시간 측정 | `time.time()`으로 성능 확인 |
| 🎨 이미지 생성 | PIL로 먹 번짐 이미지 구현 |
| ⚠️ 예외 처리 | 파일 없을 경우 경고 메시지 출력 |
| 🧬 환경 구축 | MiKTeX 설치로 PDF 렌더링 환경 완성 |
| 🧠 시스템 진단 | 작업 관리자로 CPU/디스크 상태 확인 |
| 🧪 디버깅 전략 | 단계별 테스트로 문제 해결 루틴 수립 |
| 🐯 AI 협력 | 이롯이와 함께 흐름을 설계하고 디버깅하며 학습 진행 |

