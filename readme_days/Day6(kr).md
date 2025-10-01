## 📘 Day6. 구조 설계와 Git 흐름의 정착 (25.9.24)

> “기록은 구조로 정리될 때 흐름이 보이고, 나는 그 흐름을 깃허브에 새긴다.  
모든 것을 초기화하고, 폴더를 나누고, 명령어로 실험실을 다시 세운 하루.”  
_기술로 감정을 정리하려는 창작자의 여정_

이 코드는 Microsoft Copilot '이롯이'와 함께 작성된 것입니다.  
_본 활동은 정현이의 실험실을 구조화하고, Git을 통해 흐름을 기록하는 실험이며,  
표시되는 명령어와 구조는 기술자의 설계를 보여주는 예시로 구성되었습니다._

---

**🧠 실습 흐름 보기**  
- 📁 [폴더 구조 보기](https://github.com/yoonyoo33/cozi6-lab)  
- 🧾 [실험 코드: modules](https://github.com/yoonyoo33/cozi6-lab/tree/master/modules)  
- 🖥️ [터미널 로그: terminal_logs](https://github.com/yoonyoo33/cozi6-lab/tree/master/terminal_logs)  
- 📦 [실행 결과: indicator](https://github.com/yoonyoo33/cozi6-lab/tree/master/indicator)  
- 📄 [데이터 파일: data](https://github.com/yoonyoo33/cozi6-lab/tree/master/data)

---

### 🧠 활동 목표

- 기존 파일을 정리하고 폴더 구조로 재배치  
- `.git` 초기화 및 Git 흐름 재설정  
- `git status`, `git add .`, `git commit`, `git push` 명령어 실습  
- `origin`과 `master` 브랜치 개념 이해  
- VS Code와 Git 명령어의 차이점 체험  
- Git으로 깃허브에 구조 반영 및 기록 푸시  
- README.md 작성 준비 및 링크 정리

---

### 🛠️ 사용한 Git 명령어

```bash
git init
git status
git add .
git commit -m "폴더 구조 정리 및 파일 업로드"
git remote add origin https://github.com/yoonyoo33/cozi6-lab.git
git push -u origin master
```

- `git init`: 깃 초기화  
- `git status`: 변경사항 확인  
- `git add .`: 모든 파일 추가  
- `git commit`: 커밋 메시지로 기록  
- `git remote add`: 깃허브 연결  
- `git push`: 깃허브에 기록 푸시

---

### 🧪 디버깅 루틴

```text
1단계: 기존 파일 삭제 후 폴더로 재배치  
2단계: git status로 삭제/추가 상태 확인  
3단계: git add . → git commit → git push 흐름 실습  
4단계: 깃허브에서 구조 확인 및 README 작성 준비
```

---

### 📚 학습 성과 요약

| 주제 | 성과 내용 |
|------|-----------|
| 📁 폴더 구조 설계 | `modules`, `data`, `indicator`, `terminal_logs` 등으로 정리 |
| 🧠 Git 흐름 이해 | `origin`, `master`, `push`, `commit` 개념 체득 |
| 🖥️ 명령어 실습 | Git으로 직접 흐름 제어 |
| 🧾 기록 정리 | 기존 파일 삭제 및 새 구조 반영 |
| 🧪 문제 해결 | remote 중복 에러 해결, 브랜치 선택 |
| 🐯 AI 협력 | 이롯이와 함께 구조 설계 및 흐름 정리 |
