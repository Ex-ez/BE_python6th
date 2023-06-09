import os

concurrent_directory = os.getcwd()
print(concurrent_directory)

# os.mkdir('new_directory')

# os.makedirs('parent_directory/child_directory/grandchild_directory1')

# os.chdir('new_directory')
# current_directory2 = os.getcwd()
# print(current_directory2)

# with open('example.txt', 'w') as file_object:
#     file_object.write('Hello, World!')

# os.rename('old_directory', 'new_directory')
#
# os.rmdir('new_directory')

# os.removedirs('parent_directory/child_directory/grandchild_directory1/2/3/4/5')

for dirpath, dirnames, filenames in os.walk('parent_directory'):
    print(f"디렉터리 경로: {dirpath}")
    print(f"디렉터리 이름: {dirnames}")
    print(f"파일 이름: {filenames}")
