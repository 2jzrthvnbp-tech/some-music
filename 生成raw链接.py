# -*- coding: utf-8 -*-

import os
from urllib.parse import quote

# GitHub仓库信息
USER = "2jzrthvnbp-tech"
REPO = "some-music"
BRANCH = "main"

# 输出文件
OUTPUT = "Raw链接列表.txt"


def generate_raw_url(path):
    """
    生成GitHub Raw链接
    """

    path = path.replace("\\", "/")

    encoded_path = "/".join(
        quote(part)
        for part in path.split("/")
    )

    return (
        f"https://raw.githubusercontent.com/"
        f"{USER}/{REPO}/{BRANCH}/{encoded_path}"
    )


def main():

    music_ext = (
        ".mp3",
        ".ogg",
        ".wav"
    )

    result = []

    for root, dirs, files in os.walk("."):

        # 排除git目录
        if ".git" in root:
            continue

        for file in files:

            if file.lower().endswith(music_ext):

                filepath = os.path.join(
                    root,
                    file
                )

                filepath = filepath[2:]

                url = generate_raw_url(filepath)

                result.append(
                    f"{file}\n{url}\n"
                )


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(result)
        )


    print(
        f"完成，共生成 {len(result)} 个链接"
    )


if __name__ == "__main__":
    main()