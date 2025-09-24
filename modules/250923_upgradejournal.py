import os
import pypandoc
import time
from tqdm import tqdm  # 진행률 바 추가

def make_pdf_book():
    start = time.time()  # 실행 시간 시작
    print("🚀 PDF 변환 시작!")

    folder = "journals"
    output = "MyDiary.pdf"

    print("📁 journals 폴더 확인 중...")
    os.makedirs(folder, exist_ok=True)

    print("📄 .md 파일 불러오는 중...")
    files = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".md")])

    if not files:
        print("⚠️ 변환할 일기 파일이 없습니다.")
        return

    print("🧾 표지 생성 중...")
    cover_text = """\
# 살랑, 살랑

![](sumi_dot.jpg)

by Jasmine  
(초롱이와 함께한 순간들)

---
"""
    cover_file = os.path.join(folder, "0000-cover.md")
    with open(cover_file, "w", encoding="utf-8") as f:
        f.write(cover_text)
    print("✅ 표지 생성 완료!")

    print("📦 파일 병합 중...")
    all_files = [cover_file] + files
    merged_content = ""
    for f in tqdm(all_files, desc="📄 병합 진행"):
        with open(f, encoding="utf-8") as file:
            merged_content += file.read() + "\n\n"
    print("✅ 파일 병합 완료!")

    print("🖨️ PDF 변환 중 (잠시 기다려주세요)...")
    pypandoc.convert_text(
        merged_content,
        "pdf",
        format="md",
        outputfile=output,
        extra_args=[
            "--pdf-engine=xelatex",
            "--variable=mainfont=NanumGothic Light",
            "--standalone",
            "--toc",
            "--toc-depth=2"
        ]
    )

    print("🖨️ PDF 확인해요...")
    with open("merged_preview.md", "w", encoding="utf-8") as f:
        f.write(merged_content)

    print(f"✅ PDF 변환 완료! '{output}' 파일을 확인하세요.")
    end = time.time()
    print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")

make_pdf_book()
