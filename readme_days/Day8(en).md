## 📘 Day8. Markdown Merge Automation Experiment (2025.11.2)

> “Code weaves records, and records organize me.  
> I automated repetitive tasks and built a tool that captures emotion with a single click.  
> My fingertips now dance with technology.”  
_Creative journey to organize emotions through automation_

This experiment was created in collaboration with Microsoft Copilot, 'Irosi'.  
It documents the automation of `.md` file merging and the expansion into a GUI application with `.exe` packaging.

---

### 🧠 Experiment Navigation

- 📁 [Folder Structure Overview](https://github.com/yoonyoo33/cozi6-lab)  
- 🧾 [Experiment Code: modules](https://github.com/yoonyoo33/cozi6-lab/tree/master/modules)  
- 🖥️ [Terminal Logs: terminal_logs](https://github.com/yoonyoo33/cozi6-lab/tree/master/terminal_logs)  
- 📦 [Execution Results: indicator](https://github.com/yoonyoo33/cozi6-lab/tree/master/indicator)  
- 📄 [Data Files: data](https://github.com/yoonyoo33/cozi6-lab/tree/master/data)

---

### 🧠 Experiment Versions

| Version | Description |
|---------|-------------|
| 🐍 Python CLI Merger | Sorts `.md` files by modified date and merges the top 100 into one file |
| 🖼 GUI + `.exe` Merger | Folder selection → one-click merge! GUI app packaged as `.exe` for distribution |

---

### 🧪 Experiment Structure

- `modules/` : Merge script repository  
- `indicator/` : Merged output archive  
- `terminal_logs/` : Execution logs and debug traces  
- `data/` : Reserved for future emotion tracking automation

---

### 🛠️ Technologies Used

- Python (`os`, `pathlib`, `tkinter`)  
- GUI development with `tkinter`  
- `.exe` packaging via `pyinstaller`  
- File sorting and merge automation  
- Path handling and exception management

---

### 🐯 Merge (GUI, EXE) Code

```python
import time
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

start = time.time()

def merge_md_files():
    folder = filedialog.askdirectory(title="📁 Select folder to merge")
    if not folder:
        return

    md_files = [f for f in Path(folder).glob("*.md") if f.is_file()]
    md_files_sorted = sorted(md_files, key=lambda f: f.stat().st_mtime, reverse=True)

    output_path = os.path.join(folder, "merged_latest_100.md")
    with open(output_path, "w", encoding="utf-8") as outfile:
        for i, file in enumerate(md_files_sorted[:100], 1):
            outfile.write(f"\n\n--- File {i}: {file.name} ---\n\n")
            with open(file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())

    messagebox.showinfo("✅ Done", f"Merged file created:\n{output_path}")

# Create GUI window
root = tk.Tk()
root.title("📄 Markdown Merger")
root.geometry("300x150")

label = tk.Label(root, text="Markdown File Merger", font=("Arial", 14))
label.pack(pady=10)

merge_button = tk.Button(root, text="📁 Select Folder & Merge", command=merge_md_files)
merge_button.pack(pady=20)

root.mainloop()

end = time.time()
print(f"⏱️ Total execution time: {end - start:.2f} seconds")
```

---

### 📚 Learning Summary

| Skill | Outcome |
|-------|---------|
| CLI Automation | Completed `.md` merge script |
| GUI App | Built a user-friendly merge window |
| `.exe` Packaging | Converted Python GUI to distributable `.exe` |
| Debugging | Solved path and encoding issues |
| UX Design | Designed a one-click merge experience |

---
]\
