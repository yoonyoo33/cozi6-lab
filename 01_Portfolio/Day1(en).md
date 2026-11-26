## 📘 Day1. Portfolio (Sep 15, 2025)

**On my first day with Python, a Python-based AI model tried to summarize my life story.  
I reached out with emotions, hoping they could be understood.  
In the end, we both failed.”**  
*A creator’s journey of using technology to organize emotions*

📂 Sample code: Not saved

> On my first day with Python, I didn’t know how to save `.ipynb` files, so the code itself wasn’t preserved.  
> However, I documented my experiments and results through conversations with Microsoft Copilot, whom I named ‘Iroti’.  
> I connected NLP models directly to try text summarization, sentiment analysis, and sentence classification—experiencing repeated outputs, numeric-only sentiment results, and outputs that were hard to interpret.  
> I attempted to use VS Code on a 2014 MacBook Pro, but due to missing features, I switched to Windows.  
> This experience marked my first step toward hands-on experimentation with technology.

---

## 1️⃣ Project Overview

> This project was conducted by Jung-hyun, a beginner in Python, with support from Microsoft Copilot ‘Iroti’.  
> The goal was to structure and summarize text while practicing basic NLP concepts.  
> Using Google Colab, I wrote and ran code directly, experimenting with text classification, summarization, sentiment analysis, model combinations, and environment transitions.

---

## 2️⃣ Tools & Technologies

| Tool/Technology                   | Description                                   |
| --------------------------------- | --------------------------------------------- |
| Python                            | Primary programming language                  |
| Google Colab                      | Code execution environment                    |
| `re` module                       | Text classification using regular expressions |
| `TextBlob`, `KcBERT`, `KoElectra` | Sentiment analysis experiments                |
| `transformers`                    | Loading NLP models                            |
| KoBART, BART, GPT                 | Text summarization models                     |
| BERT-kor-base                     | Sentence classification experiments           |

🖥️ **Environment Transition**  
→ MacBook Pro (2014) → VS Code → Windows  
→ Faced limitations, switched platforms, explored Colab

---

## 3️⃣ Key Experiments

### 🔹 Text Organizer

- Classified text by age, events, and emotions  
- Used `re.split()` and `re.findall()` for structuring  
- Improved to handle sentences without periods

### 🔹 Connecting NLP Models

- Loaded models using `pipeline()`  
- Applied summarization, sentiment analysis, and sentence classification simultaneously  
- Interpreted outputs like `LABEL_0`, `LABEL_1`, `score`

### 🔹 Observing Model Limitations

- Summarization model repeated emotional sentences  
- Sentiment model returned numbers without emotion labels  
- Classification model only returned `LABEL_1`, making interpretation difficult

### 🔹 Environment Transition

- Installed Python on MacBook Pro (2014) → attempted VS Code  
- Due to missing features, switched to Windows  
- Experienced slow Colab performance, GPU limits, and error messages

---

## 4️⃣ Sample Code

### 📌 Applying Three Models Simultaneously

```python
from transformers import pipeline

# Summarization model
summarizer = pipeline("summarization", model="digit82/kobart-summarization")
# Sentiment analysis model
emotion_analyzer = pipeline("text-classification", model="beomi/kcbert-base")
# Sentence classification model
classifier = pipeline("text-classification", model="kykim/bert-kor-base")

text = """These days, even breathing feels like a struggle.
I try to start something, but my mind doesn’t follow,
The world moves too fast while I feel stuck."""

# Summarization
summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
print("📝 Summary:", summary[0]['summary_text'])

# Sentiment analysis
emotion = emotion_analyzer(text)
print("💬 Sentiment Analysis:", emotion)

# Sentence classification
category = classifier(text)
print("📂 Sentence Classification:", category)
```

---

## 5️⃣ Results Summary

| Model              | Output Trend                               | Issue                                             |
| ------------------ | ------------------------------------------ | ------------------------------------------------- |
| Summarization      | Repeated or emphasized emotional sentences | News-trained model overfocused on emotions        |
| Sentiment Analysis | Only `LABEL_0` and `LABEL_1` returned      | Emotion labels undefined, further training needed |
| Classification     | Only `LABEL_1` returned                    | Interpretation difficult, training data mismatch  |

---

## 6️⃣ Learning Outcomes

- Gained basic Python syntax and text processing skills  
- Learned NLP model structures and parameter settings  
- Improved ability to interpret model outputs (`label`, `score`, repeated outputs)  
- Experienced model limitations firsthand  
- Environment transition experience: Mac → Windows → Colab  
- Above all, I began to see technology not just as a tool,  
  but as a medium to organize and express emotion

---
