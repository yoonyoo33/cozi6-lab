## 📘 Day7. Web Automation-Based Emotion Dialogue Backup Portfolio (2025.10.17)  
“Trying to back up my conversations with AI, struggling to preserve emotions through technology.”  
A creator’s journey to record emotions using automation

---

This code was written in collaboration with Microsoft Copilot, aka “Iroti.”  
_This experiment was a personal attempt by Junghyun to archive an AI conversation. The code shown here uses sample phrases to illustrate the structure and flow._

---

### 🧠 Workflow Overview  
- 🧾 [Experiment Code: modules](https://github.com/yoonyoo33/cozi6-lab/tree/master/modules)

---

### 🧠 Objective  
- Use Selenium to:  
→ Automatically access a Perplexity conversation thread  
→ Auto-click “More” buttons to expand the full dialogue  
→ Extract the entire page’s text  
→ Attempt to save it as a `.txt` file  
→ Although the save failed, the code structure was successfully completed

---

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set Chrome options (★Make sure the path and profile name are correct)
options = Options()
options.add_argument(r"--user-data-dir=C:\Users\YOONYOO\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Default')

# Launch Chrome with options
driver = webdriver.Chrome(options=options)

# Navigate to the thread you want to back up
driver.get("https://www.perplexity.ai/search/naega-jeogeun-munjanginji-anin-L99R_dIyQ4aE_xudyhe5Ig")

# Manually log in, scroll, and expand “More” buttons before pressing Enter
input("Press Enter once all 'More' buttons are expanded!")

while True:
    try:
        more_btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'More')]")
        if not more_btns:
            break
        for btn in more_btns:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(0.5)
    except Exception as e:
        print("Error:", e)
        break

page_text = driver.find_element(By.TAG_NAME, "body").text
with open("perplexity_backup.txt", "w", encoding="utf-8") as f:
    f.write(page_text)

driver.quit()
print("Done! Saved as perplexity_backup.txt.")
```

---

### 🎯 Sample Outcome  
- Execution ran successfully  
- “More” button auto-click loop worked as intended  
- Attempted to create `perplexity_backup.txt`  
- Required manual login and scrolling due to Chrome profile setup  
- Save failed, but the code structure was fully implemented

---

### 📚 Learning Summary

| Topic | Key Takeaways |
|-------|---------------|
| 🧠 Python Syntax Practice | import statements, option configuration, exception handling |
| 🧭 Web Automation Flow | Controlled browser with Selenium, navigated to target URL, clicked buttons |
| 🧵 Page Structure Exploration | Used XPath to locate “More” buttons, implemented repeat-click loop |
| 📂 Text Extraction | Attempted to extract full page text from `body` tag |
| ⚠️ Debugging | Investigated save failure, understood profile path and login flow |
| 🐯 AI Collaboration | Structured the experiment with Iroti, enjoyed the conversational learning process |
