import os

# 현재 작업 디렉토리에서 .jpg 확장자를 가진 모든 파일명을 가져옴
jpg_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.jpg')]

# 파일명에서 .jpg 확장자를 제외한 이름만 추출하여 출력
for jpg_file in jpg_files:
    filename_without_extension = os.path.splitext(jpg_file)[0]
    print(filename_without_extension)
