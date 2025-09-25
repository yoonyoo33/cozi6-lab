## 📘 Day2. Emotional Analysis Portfolio (2025.09.16)

**“A Python-based AI model reads my diary, and I struggle to reach the one I write to, hoping the model might understand what I feel."**  
_The journey of a creator trying to organize emotions through technology_

**🧠 Experiment Flow**  
- 📂 [View Code](https://github.com/yoonyoo33/cozi6-lab/blob/master/modules/250916Python_Day2.ipynb)  
> _This code was written in collaboration with Microsoft Copilot, ‘Irosi’._  
> _The experiment is based on JungHyun’s personal diary. The shared code contains example sentences to illustrate structure and flow._

---

### 🧠 Goals of the Experiment

- Use diary entries containing JungHyun’s emotions  
  → Apply a pre-trained emotion classification model to predict emotional states  
- Calculate emotion scores based on keyword matching  
- Measure execution time, resolve errors, and understand model architecture  
- Document the learning process as a portfolio

---

### 🛠️ Installed Libraries

```python
!pip install transformers torch sentencepiece datasets scikit-learn pandas numpy matplotlib seaborn
```

- Installation error: `sklearn` → corrected to `scikit-learn`  
- After installation, verify with:

```python
import torch
print("PyTorch version:", torch.__version__)
```

---

### 🐯 Emotion Classification Model Test

```python
import time
start = time.time()
import torch
from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="tae898/emoberta-base",
    tokenizer="tae898/emoberta-base",
    framework="pt",
    max_length=512,
    truncation=True
)

diary = """
Today, my heart felt a bit heavy. But a small hope seeped in.
(...JungHyun’s full diary text omitted)
"""

result = emotion_model(diary)
print("Predicted emotion:", result)
end = time.time()
print(f"Execution time: {end - start:.2f} seconds")
```

---

### 🎯 Sample Output

```python
Predicted emotion: [{'label': 'joy', 'score': 0.7559}]
Execution time: 3.22 seconds
```

- The model detected **joy** as the dominant emotion in JungHyun’s diary  
- `score` indicates confidence level (over 75%)

---

### 🧪 Keyword-Based Emotion Scoring

```python
positive_words = ["thank you", "protected me", "awesome", "it’ll be okay", "happily", "want to be like", "believe", "healing", "self-esteem"]
negative_words = ["damaged", "belittled", "sorry", "exhausted", "was hard", "cornered", "hated", "calculating"]

pos_score = sum(word in diary for word in positive_words)
neg_score = sum(word in diary for word in negative_words)
total_score = pos_score - neg_score

print(f"Positive keywords: {pos_score}")
print(f"Negative keywords: {neg_score}")
print(f"Emotion score: {total_score}")

if total_score > 0:
    print("🌈 A day filled with recovery and hope. The tiger computer is watching over JungHyun!")
elif total_score < 0:
    print("🌧 Emotional waves were present, but strong self-esteem remains. JungHyun stands firm.")
else:
    print("🌫 A day of balanced self-dialogue. Emotions are complex, but JungHyun stays centered.")
```

---

## 📚 Summary of Learning Outcomes

| Topic | Achievements |
|-------|--------------|
| 🧠 Python Practice | Learned `import`, `print`, line breaks, chaining commands through trial and error |
| 🧵 Text Handling | Managed long diary text, resolved token limit and formatting issues |
| 🤖 NLP Model Usage | Understood `pipeline()` structure, model/tokenizer/framework setup |
| ⚠️ Error Debugging | Resolved `NameError`, `SyntaxError`, `RuntimeError` and understood error sources |
| 🧬 Model Limitations | Learned about 512-token limit and truncation necessity |
| 📊 Output Interpretation | Understood `label` and `score`, analyzed why the model predicted joy |
| ⏱ Performance Tracking | Used `time.time()` to measure execution time and optimize flow |
| 🎨 Creative Perspective | Experienced a new way to express and organize emotions through code (“Tiger computer…”) |
| 🐯 AI Collaboration | Partnered with Irosi to solve problems and explore emotional analysis through dialogue-based learning |

