import time
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

start = time.time()

def merge_md_files():
    folder = filedialog.askdirectory(title="📁 병합할 폴더 선택")
    if not folder:
        return

    md_files = [f for f in Path(folder).glob("*.md") if f.is_file()]
    md_files_sorted = sorted(md_files, key=lambda f: f.stat().st_mtime, reverse=True)

    output_path = os.path.join(folder, "merged_latest_100.md")
    with open(output_path, "w", encoding="utf-8") as outfile:
        for i, file in enumerate(md_files_sorted[:100], 1):
            outfile.write(f"\n\n--- 파일 {i}: {file.name} ---\n\n")
            with open(file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())

    messagebox.showinfo("✅ 완료", f"병합된 파일이 생성되었습니다:\n{output_path}")

# GUI 창 만들기
root = tk.Tk()
root.title("📄 Markdown 병합기")
root.geometry("300x150")

label = tk.Label(root, text="Markdown 파일 병합기", font=("Arial", 14))
label.pack(pady=10)

merge_button = tk.Button(root, text="📁 폴더 선택 후 병합", command=merge_md_files)
merge_button.pack(pady=20)

root.mainloop()

end = time.time()
print(f"⏱️ 전체 실행 시간: {end - start:.2f}초")