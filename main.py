print("파일 열기")
file_object = open('example.txt', 'r')

print("현재 파일 위치 확인")
position = file_object.tell()
print("Current position: ", position)

print("파일 포인터 위치 변경")
file_object.seek(7)

print("변경된 위치 확인")
position = file_object.tell()
print("New position:", position)

print("파일 닫기")
file_object.close()