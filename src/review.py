from clang_tidy_review import create_review, convert_git_lab_changes_to_unidiff
import unidiff


def review(config):
    comments = []

    diff_changes = config["merge"]["changes"]
    build_dir = config["clang_tidy"]["build_dir"]
    clang_tidy_binary = config["clang_tidy"]["binary_dir"]
    clang_tidy_checks = config["clang_tidy"]["checks"]
    config_file = config["clang_tidy"]["config_file"]
    include = config["clang_tidy"]["include"]
    exclude = config["clang_tidy"]["exclude"]

    result_review = create_review(
        diff_changes,
        build_dir,
        clang_tidy_checks,
        clang_tidy_binary,
        config_file=config_file,
        include=include,
        exclude=exclude,
    )

    print(f"[RESULTADO]={result_review}")

    # TODO IMPLEMENTAR EXTENSION
    #  O OBJETO DE COMENTARIO DEVE POSSUIR O SEGUINTE FORMATO
    #  {
    #      "id": "",
    #      "comment": ""
    #  }

    return comments
