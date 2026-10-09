extension = input("Enter extension: ").strip().lower().lstrip(".")

match extension:
    case "pdf":
        print("Document File")
    case "jpg" | "png":
        print("Image File")
    case "mp3":
        print("Audio File")
    case "mp4":
        print("Video File")
    case _:
        print("Unknown File Type")
