contents = ["All carrots are healthy",
            "Dogs are animals",
            "The weather is sunny today."]
filenames = ["doc.txt", "animals.txt", "weather.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
