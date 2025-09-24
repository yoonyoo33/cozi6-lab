
from datetime import datetime
print("hello,world")

def write_journal():
    today = datetime.now().strftime("%Y-%m-%d")
    title = input("오늘 글 제목을 입력하세요: ")
    content = input("오늘의 글을 적어주세요: ")

    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(f"날짜: {today}\n제목: {title}\n내용: {content}\n")
        f.write("-" * 40 + "\n")

    print("저장 완료! journal.txt 파일에서 확인해보세요. 📖")

# 함수 실행
write_journal()