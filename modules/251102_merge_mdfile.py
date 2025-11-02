import time
import os
from pathlib import Path

start = time.time()

# ✅ 설정: 병합할 폴더 경로와 결과 파일 이름
target_folder = r"C:\Users\YOONYOO\Desktop\논문\Bern파이썬용_09월"
output_file = os.path.join(target_folder, "B_Sep_dialogue.md")  # 파일 이름 포함

# ✅ .md 파일 목록 가져오기
md_files = [f for f in Path(target_folder).glob("*.md") if f.is_file()]

# ✅ 수정일 기준 최신순 정렬
md_files_sorted = sorted(md_files, key=lambda f: f.stat().st_mtime, reverse=True)

# ✅ 상위 100개 파일 병합
with open(output_file, "w", encoding="utf-8") as outfile:
    for i, file in enumerate(md_files_sorted[:100], 1):
        outfile.write(f"\n\n--- 파일 {i}: {file.name} ---\n\n")
        with open(file, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())

end = time.time()
print(f"✅ 병합 완료! 결과 파일: {output_file}")
print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")