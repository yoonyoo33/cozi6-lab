import time
import pypandoc

def make_pdf_book():
    start = time.time()

    merged_content = "# Test\nThis is a test document.\nPDF conversion check."
    output = "test.pdf"

    print("🖨️ PDF 변환 중...")
    pypandoc.convert_text(
        merged_content,
        "pdf",
        format="md",
        outputfile=output,
        extra_args=[
            "--pdf-engine=xelatex",
            "--standalone"
        ]
    )

    print(f"✅ PDF 변환 완료! '{output}' 파일을 확인하세요.")
    end = time.time()
    print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")

make_pdf_book()
