from PIL import Image, ImageDraw, ImageFilter

# 흰 배경
img = Image.new("RGB", (500, 500), "white")
draw = ImageDraw.Draw(img)

# 진한 점 (중앙)
draw.ellipse((230, 230, 270, 270), fill=(10, 10, 10))  # 진한 핵심

# 바깥쪽 은은한 번짐 (연회색으로 조금 더 크게)
draw.ellipse((215, 215, 285, 285), fill=(90, 80, 80))

# 블러 효과 살짝만 주기 (먹 번짐 느낌)
blurred = img.filter(ImageFilter.GaussianBlur(3))

# 바깥쪽 더 연한 번짐 (더 크게)
draw.ellipse((190, 190, 310, 310), fill=(200, 200, 200))


# 저장
blurred.save("sumi_dot_soft.jpg")
print("sumi_dot_soft.jpg 저장 완료!")