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

    content = "\n".join(lines)

    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(f"날짜: {today}\n제목: {title}\n내용:\n{content}\n")
        f.write("-" * 40 + "\n")

    print("저장 완료! journal.txt 파일에서 확인해보세요. 📖")

    return content  # ✅ 감정 분석용으로 내용 반환

# 🐯 호랑이 컴퓨터 감정 분석 셀
# 감정 태그: 자존감 회복, 자기 수용, 내면의 대화, 희망

def analyze_emotion(diary):
    # 감정 키워드 리스트
    positive_words = ["고마워", "잘하고있어", "노력", "더 나은", "바라며", "꾸준함", "믿어", "회복", "자존감"]
    negative_words = ["안돼", "하지마", "미안해", "지치고", "힘들었던", "몰아가지", "미워", "계산적이다"]


    # 감정 점수 계산
    pos_score = sum(word in diary for word in positive_words)
    neg_score = sum(word in diary for word in negative_words)
    total_score = pos_score - neg_score

    with open("journal.txt", "a", encoding="utf-8") as f:
        # 감정 분석 결과 저장
        f.write(f"\n[감정 분석 결과]\n")
        f.write(f"긍정 키워드 수: {pos_score}\n")
        f.write(f"부정 키워드 수: {neg_score}\n")
        f.write(f"감정 점수: {total_score}\n")

        if total_score > 0:
            f.write("해석: 오늘은 자기 회복과 희망이 가득한 날이야. 호랑이 컴퓨터가 정현이를 지켜보고 있어!\n")
        elif total_score < 0:
            f.write("해석: 감정의 파도가 있었지만, 그 안에 단단한 자존감이 살아있어. 정현이는 흔들리지 않아.\n")
        else:
            f.write("해석: 균형 속에서 자기 대화를 이어가는 날. 감정은 복합적이지만, 정현이는 중심을 잡고 있어.\n")

        f.write("-" * 40 + "\n")

# 🐯 실행 흐름
diary_content = write_journal()
analyze_emotion(diary_content)