import os

# 현재 작업 디렉토리에서 .jpg 확장자를 가진 모든 파일명을 가져옴
jpg_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.jpg')]

# 파일명에서 .jpg 확장자를 제외한 이름만 추출하여 출력
filename_list = []
for jpg_file in jpg_files:
    filename_without_extension = os.path.splitext(jpg_file)[0]
    filename_list.append(filename_without_extension)

# 추출한 파일명 리스트를 텍스트 파일에 저장
with open('filename_list.txt', 'w') as f:
    for filename in filename_list:
        f.write("%s\n" % filename)
