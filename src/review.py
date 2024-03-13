import hashlib

from clang_tidy_review import create_review


def review(config):
    comments = []

    diff_changes = config["merge"]["changes"]
    build_dir = config["clang_tidy"]["build_dir"]
    clang_tidy_binary = config["clang_tidy"]["binary_dir"]
    clang_tidy_checks = config["clang_tidy"]["checks"]
    config_file = config["clang_tidy"]["config_file"]
    include = config["clang_tidy"]["include"]
    exclude = config["clang_tidy"]["exclude"]
    path_source = config["path_source"]

    result_review = create_review(
        diff_changes,
        build_dir,
        clang_tidy_checks,
        clang_tidy_binary,
        path_source,
        config_file=config_file,
        include=include,
        exclude=exclude,
    )

    if result_review:
        for comment in result_review["comments"]:
            comments.append(
                {
                    "id": __generate_md5(comment["body"] + comment["path"]),
                    "comment": comment["body"],
                    "position": {
                        "language": "c++",
                        "path": __format_from_path_source_to_acr_processor(
                            path_source, comment["path"]
                        ),
                        "startInLine": comment["line"],
                        "endInLine": comment["line"],
                    },
                }
            )

    return comments


def __format_from_path_source_to_acr_processor(path_source: str, path: str):
    print(f'acr-clang-tidy Format path source [PATH_SOURCE] {path_source} - [PATH_CLANG] {path}')
    result = path.replace(path_source, "")
    if result.startswith("/"):
        result = path[1:]

    print(f'acr-clang-tidy Format path source [PATH_OUTPUT] {result}')

    return result


def __generate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode("utf-8"))

    return md5_hash.hexdigest()
