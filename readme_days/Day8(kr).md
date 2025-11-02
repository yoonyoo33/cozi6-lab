## 📘 Day8. Markdown 병합 자동화 실험 (2025.11.2)

> “코드는 기록을 엮고, 기록은 나를 정리한다.  
> 반복된 수작업을 자동화하고, 클릭 한 번으로 감정을 담는 도구를 만들다.  
> 나의 손끝이 기술과 함께 춤을 춘다.”  
_기술로 감정을 정리하려는 창작자의 여정_

이 코드는 Microsoft Copilot '이롯이'와 함께 작성된 것입니다.  
_정현이의 실험실에서 `.md` 파일 병합을 자동화하고, GUI와 `.exe`로 확장한 실험입니다._

---

### 🧠 실습 흐름 보기

- 📁 [폴더 구조 보기](https://github.com/yoonyoo33/cozi6-lab)  
- 🧾 [실험 코드: modules](https://github.com/yoonyoo33/cozi6-lab/tree/master/modules)  
- 🖥️ [터미널 로그: terminal_logs](https://github.com/yoonyoo33/cozi6-lab/tree/master/terminal_logs)  
- 📦 [실행 결과: indicator](https://github.com/yoonyoo33/cozi6-lab/tree/master/indicator)  
- 📄 [데이터 파일: data](https://github.com/yoonyoo33/cozi6-lab/tree/master/data)

---

### 🧠 실험 버전

| 버전 | 설명 |
|------|------|
| 🐍 Python CLI 병합기 | 수정일 기준으로 `.md` 파일을 정렬하고, 상위 100개를 하나로 병합하는 스크립트 |
| 🖼 GUI + `.exe` 병합기 | 폴더 선택 → 버튼 클릭으로 병합 완료! `.exe`로 배포 가능한 GUI 앱 구현 |

---

### 🧪 실험 흐름

- `modules/` : 병합 스크립트 저장소  
- `indicator/` : 병합된 결과물 저장  
- `terminal_logs/` : 실행 로그 및 디버깅 기록  
- `data/` : 향후 감정 기록 자동화에 활용 예정

---

### 🛠️ 사용 기술

- Python (`os`, `pathlib`, `tkinter`)  
- GUI 구현 (`tkinter`)  
- `.exe` 변환 (`pyinstaller`)  
- 파일 정렬 및 병합 자동화  
- 경로 설정 및 예외 처리

---

### 🐯 Merge(GUI, EXE) 코드

```python
import time
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

start = time.time()

def merge_md_files():
    folder = filedialog.askdirectory(title="📁 병합할 폴더 선택")
    if not folder:
        return

    md_files = [f for f in Path(folder).glob("*.md") if f.is_file()]
    md_files_sorted = sorted(md_files, key=lambda f: f.stat().st_mtime, reverse=True)

    output_path = os.path.join(folder, "merged_latest_100.md")
    with open(output_path, "w", encoding="utf-8") as outfile:
        for i, file in enumerate(md_files_sorted[:100], 1):
            outfile.write(f"\n\n--- 파일 {i}: {file.name} ---\n\n")
            with open(file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())

    messagebox.showinfo("✅ 완료", f"병합된 파일이 생성되었습니다:\n{output_path}")

# GUI 창 만들기
root = tk.Tk()
root.title("📄 Markdown 병합기")
root.geometry("300x150")

label = tk.Label(root, text="Markdown 파일 병합기", font=("Arial", 14))
label.pack(pady=10)

merge_button = tk.Button(root, text="📁 폴더 선택 후 병합", command=merge_md_files)
merge_button.pack(pady=20)

root.mainloop()

end = time.time()
print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")
```

---

### 📚 학습 성과 요약

| 기술 | 성과 |
|------|------|
| CLI 자동화 | `.md` 파일 병합 스크립트 완성 |
| GUI 앱 | 마우스 클릭으로 병합 가능한 창 구현 |
| `.exe` 배포 | 파이썬 GUI를 `.exe`로 변환하여 배포 가능 |
| 디버깅 | 경로 오류, 인코딩 문제 해결 |
| 사용자 경험 | 클릭 한 번으로 결과 생성되는 UX 설계 |

---
