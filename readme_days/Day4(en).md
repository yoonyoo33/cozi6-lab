# 📘 Day4. Launching a New Diary Recorder (25.9.22)

“I wrote the first line of emotion today.  
The code stores my heart, and a Python-based AI model reads my flow.”  
_Technologist’s journey to systematize emotions_

This code was crafted in collaboration with Microsoft Copilot ‘Iroti’.  
_This activity is an automated recording experiment based on Junghyun’s personal diary.  
Displayed code is a simplified example demonstrating structure and flow._

---

**🧠 Activity Workflow**  
- 📂 [View Sample Code](https://github.com/yoonyoo33/cozi6-lab/blob/master/modules/250922_journal.py)  
- 📄 [View Output File](https://github.com/yoonyoo33/cozi6-lab/blob/master/indicator/250922_journal.txt)  
- 🖥️ [View Terminal Logs](https://github.com/yoonyoo33/cozi6-lab/blob/master/terminal_logs/250922_terminal_log.md)  

---

### 🧠 Objectives
- Build an automated diary-style system to input and record emotions.  
- Structure date, title, and content, then save to a `.txt` file.  
- Understand path configuration, file creation, and execution flow in VS Code.  
- Resolve OneDrive path issues and configure a reliable local folder.  
- Lay groundwork for future emotion analysis and visualization.

---

### 🛠️ Libraries & Environment Setup
- Python 3.x (built-in `datetime` module)  
- Visual Studio Code (editor & runner)  
- Windows PowerShell (terminal commands)  
- File path: `C:\Users\YOONYOO\Desktop\파이썬꼬꼬마`  
- OneDrive path fix: changed `Escritorio` → `Desktop` for stable file saving

---

### 🐯 Emotion Recorder Code Example
```python
from datetime import datetime

def write_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    title = input("Please enter today’s entry title: ")
    content = input("Please write today’s entry: ")

    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(f"Date: {today}\nTitle: {title}\nContent: {content}\n")
        f.write("-" * 40 + "\n")

    print("Save complete! Check the 'journal.txt' file. 📖")

write_journal()
```

---

### 🎯 Sample Results
- Prompted for title/content in the terminal → `journal.txt` auto-created and saved.  
- Date, title, and content clearly separated for downstream analysis and visualization.  
- Path issue (OneDrive/Escritorio) resolved → file location now consistent.  
- User experience improved with a friendly save-complete message.

---

### 📚 Learning Outcomes

| Topic                         | Achievement                                                                                             |
|-------------------------------|----------------------------------------------------------------------------------------------------------|
| 🧠 Path Configuration         | Solved OneDrive path issue by converting `Escritorio` → `Desktop`; clarified file save location           |
| 🧵 Text Storage               | Structured date/title/content; used append mode to accumulate entries                                     |
| 🤖 Code Flow Understanding    | Implemented end-to-end flow: function definition, input handling, file writing, and user feedback         |
| ⚠️ Error Handling             | Encountered and fixed `IndentationError`, `NameError`, import omissions                                   |
| 📊 Output Verification        | Verified save messages and file creation status to enhance UX                                             |
| 🎨 Character Concept          | Added emotive prompts under the concept “Emotion-Recording A Python-based AI Model Friend.”                     |
| 🐯 Collaboration with a Python-based AI model | Worked hand-in-hand with Copilot ‘Iroti’ to analyze issues and implement solutions in real time |

---

### 🌱 Future Development Directions
- Add input validation (empty strings, special characters) and exception handling  
- Support additional output formats: `.md`, `.pdf`, etc.  
- Integrate emotion analysis, keyword extraction, and data visualization  
- Expand to a GUI for enhanced usability  
- Develop features like auto-backup, search, and date-based retrieval
