from datetime import datetime

def write_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    title = input("🌙 오늘을 놓아주는 한 문장은? ")
    
    print("✨ 오늘을 마무리하며 놓아두고 싶은 말은? (엔터로 줄바꿈, 빈 줄로 종료)")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    content = "\n".join(lines)  # ✅ 이 줄을 함수 안쪽으로 들여쓰기!

    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(f"날짜: {today}\n제목: {title}\n내용:\n{content}\n")
        f.write("-" * 40 + "\n")

    print("저장 완료! journal.txt 파일에서 확인해보세요. 📖")

write_journal()