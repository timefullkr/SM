from PIL import Image

# 이미지 파일 경로를 지정합니다.
image_path = 'images/carA.png'

# 이미지의 배경을 투명하게 만드는 작업은 복잡할 수 있으며,
# PIL만으로는 자동으로 배경을 제거하기 어려울 수 있습니다.
# 하지만, 이 경우 이미지가 단색 배경이므로 시도해 볼 수 있습니다.

# 이미지를 다시 로드하고 배경을 투명하게 바꿉니다.
with Image.open(image_path) as img:
    # 이미지를 RGBA 모드로 변환하여 알파 채널이 생깁니다.
    img = img.convert("RGBA")

    # 데이터를 가져옵니다.
    datas = img.getdata()

    # 새로운 이미지 데이터 리스트를 생성합니다.
    new_data = []
    # 이 반복문은 모든 픽셀을 확인하고, 배경색인 경우 투명하게 만듭니다.
    for item in datas:
        # 픽셀이 흰색이거나 완전히 투명한 경우, 투명하게 바꿉니다.
        if item[0] == 255 and item[1] == 255 and item[2] == 255 or item[3] == 0:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    # 새 데이터로 이미지를 업데이트합니다.
    img.putdata(new_data)

    # 투명 배경의 이미지를 저장합니다.
    transparent_img_path = 'images/carAAA.png'
    img.save(transparent_img_path, "PNG")

transparent_img_path
