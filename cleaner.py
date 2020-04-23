import os
import shutil


def create_folders(directories, dir_path):
    
    for key in directories:
        if key not in os.listdir(dir_path):
            os.mkdir(dir_path + '/' + key)


def organize_folders(directories, dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(dir_path + '/' + file):
            src_path = dir_path + '/' + file
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(dir_path, key, file)
                    shutil.move(src_path, dest_path)
                    break


def organize_remaining_files(dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(dir_path + '/' + file):
            src_path = dir_path + '/' + file
            dest_path = os.path.join(dir_path, "OTHER", file)
            shutil.move(src_path, dest_path)


def organize_remaining_folders(directories, dir_path):
    list_dir = os.listdir(dir_path)
    organized_folders = []
    for folder in directories:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = dir_path + '/' + folder
            dest_path = os.path.join(dir_path, "FOLDERS", folder)
            shutil.move(src_path, dest_path)


if __name__ == '__main__':
    dir_path = r"C:\Users\Deepanshu\Downloads"
    directories = {
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "Java" : (".java" , ".class"),
        "JavaScript":".js",
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg",
                   ".heif", ".psd"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd"),
        "Spreadsheets" : ( ".xls", ".xlsx", ".csv"),

        "Presentation" : (".ppt", "pptx"),

        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PLAINTEXT": (".txt", ".in", ".out"),
        "PDF": (".pdf"),
        "PYTHON": ".py",
        "EXE": ".exe",
        "OTHER": "",
        "FOLDERS": ""
    }
    create_folders(directories, dir_path)
    organize_folders(directories, dir_path)
    organize_remaining_files(dir_path)
    organize_remaining_folders(directories, dir_path)