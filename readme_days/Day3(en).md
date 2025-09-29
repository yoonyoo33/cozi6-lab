## 📘 Day3. A Git Collision and the Code Recovery Saga (25.9.17)

> “A Python-based AI model tried to organize me,  
but I got swept up in its storm.  
The moment GitHub collided with my local files,  
Copilot chat logs disappeared, and my code scattered like confetti.  
That night, I gathered the fragments and wrote a memo to remember.”  
_A creator’s journey to organize emotions through technology_

This code was originally crafted with Microsoft Copilot ‘Iroti’,  
_but all activities below are based on Junghyun’s manual recovery after the Copilot session was lost._

---

### 🧠 Workflow Overview

- GitHub sync triggered a merge conflict
- `readme.md` file contents got scrambled, commit history tangled
- Copilot chat history disappeared, code recovery impossible
- Junghyun manually recovered code fragments from memory and Git logs  
- Final notes were preserved in a memo file, now archived as a relic of survival
  
**💡 Key takeaway:** Reconstructed workflow from fragmented code and commit history, enhancing problem-solving skills

---

### 📄 Summary of Recovered Notes

- `git init` → Initialized local repo  
- `git remote add origin` → Connected to GitHub  
- `git pull origin main` → Collision occurred  
- `readme.md` auto-merged with conflicting content  
- Used `git status`, `git log` to trace changes  
- Attempted recovery via `git reset --hard` and `git restore`  
- Rebuilt folder structure in `cozi6-lab` manually

**💡 Key takeaway:** Practiced Git commands and learned systematic code recovery methods

---

### 🧪 Debugging Routine

1. Checked GitHub commit history → Traced when chat logs disappeared
2. Compared files in `readme_days` → Identified corrupted entries
3. Reconstructed workflow using memo notes and Git commands
4. Rewrote code manually without Copilot

**💡 Key takeaway:** Independently analyzed problems and reconstructed code flow without AI assistance


---

### 🧠 Git Structure Understanding

Through this experience, Junghyun developed a clear understanding of Git:

* **git (local computer) ↔ GitHub (remote)**
  → Files are exchanged back and forth
* **init**: Initialize repository  (Ready, set, go!)  
* **add**: Stage changes for commit (I’m adding this!)
* **commit**: Save changes locally
* **push**: Send changes to remote repository (Send it to GitHub!) 
* **pull**: Fetch changes from remote repository (Bring it from GitHub!)  
* **gitkeep**: Maintain empty folders in repo
* **rebase**: Reorganize and selectively apply changes (So… what do you want to save?)

**💡 Key takeaway:** Gained practical comprehension of Git workflows beyond memorizing commands, able to resolve conflicts independently



### 📚 Learning Outcomes

| Topic | Achievement |
|-------|-------------|
| ⚠️ Git Conflict Experience | First-hand experience with `git pull` merge conflicts |
| 🧾 Commit Message Clues | Used GitHub commit history to rebuild lost logic |
| 📁 Folder Structure Recovery | Reorganized `cozi6-lab` and restored `readme_days` |
| 🧠 Memory-Based Coding | Rewrote code from scratch using memo notes |
| 🐯 Solo Recovery Without AI | Reconstructed flow without Copilot for the first time |

---

### 🌱 Future Directions

* Learn `git pull --rebase` to prevent conflicts
* Establish commit message conventions and automate log extraction
* Explore Copilot chat backup strategies
* Automate portfolio scripts to reduce recovery time
* Use GitHub Actions to automatically log commits

---
