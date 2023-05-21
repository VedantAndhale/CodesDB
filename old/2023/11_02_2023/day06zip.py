contents = ['hello', 'namaste', 'holla']
filenames = ["usa.txt", "india.txt", "germany.txt"]
for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
