from clang_tidy_review import create_review
import unidiff


def review(config):
    comments = []

    diff = [unidiff.PatchSet(config["merge"]["changes"]["diff"])[0]]
    build_dir = config["clang_tidy"]["build_dir"]
    clang_tidy_binary = config["clang_tidy"]["binary_dir"]
    clang_tidy_checks = config["clang_tidy"]["checks"]
    config_file = config["clang_tidy"]["config_file"]
    include = config["clang_tidy"]["include"]
    exclude = config["clang_tidy"]["exclude"]

    result_review = create_review(
        diff,
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
