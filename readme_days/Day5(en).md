## 📘 Day5. Visualization and Automation of Emotion Records (25.9.23)

> “Recording helps me organize myself, and technology binds it into a book.  
A day where the lingering emotions, like ink spreading on paper, were captured in PDF and image.  
And a quiet night, waiting for that book to be born.”  
_A creator’s journey to organize emotions through technology_

This code was crafted in collaboration with Microsoft Copilot ‘Iroti’.  
_This activity is part of Junghyun’s personal diary automation experiment.  
The code shown is a simplified example to illustrate structure and flow._

---

**🧠 Workflow Overview**  
- 📂 [Code: PDF Conversion](https://github.com/yoonyoo33/cozi6-lab/blob/master/modules/250923_upgradejournal.py)  
- 🎨 [Code: Ink Spread Image](https://github.com/yoonyoo33/cozi6-lab/blob/master/images/250923_sumi_dot.py)  
- 📄 [Output File](https://github.com/yoonyoo33/cozi6-lab/blob/master/images/250923_MyDiary.pdf)  
- 🖥️ [Terminal Log](https://github.com/yoonyoo33/cozi6-lab/blob/master/terminal_logs/250923_terminal_log.txt)

---

### 🧠 Objectives

- Automatically convert emotion diary entries saved in `.md` format into a PDF  
- Generate a cover page, merge content, and include a table of contents  
- Visualize merge progress using `tqdm`  
- Guide each step with `print()` logs  
- Measure execution time using `time.time()`  
- Create ink spread-style images using PIL  
- Set up MiKTeX for PDF rendering via Pandoc  
- Analyze system performance and establish debugging routines  
- Resolve Korean font rendering issues and define font mapping strategy

---

### 🛠️ Installed Libraries

```bash
pip install pypandoc tqdm pillow
```

- `pypandoc`: Converts Markdown to PDF  
- `tqdm`: Visualizes merge progress  
- `Pillow`: Generates and filters images  
- MiKTeX: LaTeX environment required for Pandoc’s PDF rendering

---

### 🐯 PDF Automation Code Example

```python
import os, time, pypandoc
from tqdm import tqdm

def make_pdf_book():
    start = time.time()
    print("🚀 Starting PDF conversion!")

    folder = "journals"
    output = "MyDiary.pdf"
    os.makedirs(folder, exist_ok=True)

    print("📄 Loading .md files...")
    files = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".md")])
    if not files:
        print("⚠️ No diary files found for conversion.")
        return

    print("🧾 Creating cover page...")
    cover_text = """\
# Sway, Sway

![](sumi_dot.jpg)

by Jasmine  
(Moments shared with Chorong)

---
"""
    cover_file = os.path.join(folder, "0000-cover.md")
    with open(cover_file, "w", encoding="utf-8") as f:
        f.write(cover_text)
    print("✅ Cover page created!")

    print("📦 Merging files...")
    all_files = [cover_file] + files
    merged_content = ""
    for f in tqdm(all_files, desc="📄 Merging Progress"):
        with open(f, encoding="utf-8") as file:
            merged_content += file.read() + "\n\n"
    print("✅ Merge complete!")

    print("🖨️ Converting to PDF (please wait)...")
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

    print(f"✅ PDF conversion complete! Check the '{output}' file.")
    end = time.time()
    print(f"⏱️ Total execution time: {end - start:.2f} seconds")

make_pdf_book()
```

---

### 🎨 Ink Spread Image Code

```python
from PIL import Image, ImageDraw, ImageFilter

img = Image.new("RGB", (500, 500), "white")
draw = ImageDraw.Draw(img)

draw.ellipse((230, 230, 270, 270), fill=(10, 10, 10))
draw.ellipse((215, 215, 285, 285), fill=(90, 80, 80))
blurred = img.filter(ImageFilter.GaussianBlur(3))
draw.ellipse((190, 190, 310, 310), fill=(200, 200, 200))

blurred.save("sumi_dot_soft.jpg")
print("sumi_dot_soft.jpg saved successfully!")
```

---

### 🧪 Debugging Routine

```text
Step 1: Run PDF conversion with "# Test" content only → Check Pandoc functionality  
Step 2: Remove image insertion → Identify image rendering issues  
Step 3: Reboot computer → Reset memory and processes
```

---

### 🧠 Problem-Solving Summary

| Issue | Solution |
|-------|----------|
| Korean text broken in PDF | Specified font with `mainfont=NanumGothic Light` |
| Auto-generated figure captions | Removed by using `![](sumi_dot.jpg)` |
| Missing `.md` files | Verified extensions and renamed `.txt` to `.md` |
| VS Code breakpoint errors | Restarted debugging session to resolve |

---

### 📚 Learning Outcomes

| Topic | Achievement |
|-------|-------------|
| 📁 File Automation | Created folders with `os.makedirs()`, merged `.md` files |
| 🖨️ PDF Conversion | Used `pypandoc.convert_text()` to generate PDF |
| 📊 Progress Visualization | Displayed merge flow with `tqdm` |
| 🧾 Log Design | Structured step-by-step messages with `print()` |
| ⏱️ Time Measurement | Measured performance using `time.time()` |
| 🎨 Image Creation | Designed ink spread visuals using PIL |
| ⚠️ Exception Handling | Displayed warnings when files were missing |
| 🧬 Environment Setup | Installed MiKTeX for PDF rendering |
| 🧠 System Diagnostics | Checked CPU/disk status via Task Manager |
| 🧪 Debugging Strategy | Solved issues through step-by-step testing |
| 🐯 Collaboration with a Python-based AI model | Designed flow and debugged in tandem with Copilot ‘Iroti’ |
