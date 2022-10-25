def main():
    filename = input("File name: ").strip().lower()

    if "." in filename:
        file_ext = filename.split(".")[-1]
    else:
        file_ext = "foo"

    print(extension(file_ext))


def extension(ext):
    match ext:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "zip":
            return "application/zip"
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"

main()