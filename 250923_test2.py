import time
import pypandoc

def make_pdf_book():
    start = time.time()

    # 간단한 테스트용 마크다운 텍스트 (한글 포함)
    merged_content = """\
# 테스트 문서

이 문서는 PDF 변환 테스트를 위한 간단한 예시입니다.
한글이 포함되어 있어 xelatex 엔진이 필요합니다.

- 항목 1
- 항목 2
- 항목 3

감사합니다!
"""

    output = "test.pdf"

    print("🖨️ PDF 변환 중...")
    pypandoc.convert_text(
        merged_content,
        "pdf",
        format="md",
        outputfile=output,
        extra_args=[
            "--pdf-engine=xelatex",  # 한글 지원되는 엔진
            "--variable", "mainfont=NanumGothic",  # 한글 폰트 설정
            "--standalone",
            "--toc",  # 목차 포함
            "--toc-depth=2"
        ]
    )

    print(f"✅ PDF 변환 완료! '{output}' 파일을 확인하세요.")
    end = time.time()
    print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")

make_pdf_book()
