# Automatic Code Review - Clang Tidy
1. Recebe um diff como entrada
2. Executa o clang-tidy com as configurações definidas no config.json
3. Retorna uma lista de comentários com os warnings capturados pelo clang-tidy que serão usados pelo [automatic-code-review-processor](https://github.com/automatic-code-review/automatic-code-review-processor)
4. Resulta em comentários em merges requests com os warnings do clang-tidy

---

## Arquivo config.json
O arquivo de configuração para executar corretamente o clang-tidy com as configurações definidas, estão estruturadas no arquivo config-schema.json
```json
{
    "path_output": "clang-tidy-review-output.json",
    "clang_tidy": {
        "build_dir": "build/",
        "binary_dir": "clang-tidy",
        "checks": "'-*,performance-*,readability-*,bugprone-*,clang-analyzer-*,cppcoreguidelines-*,mpi-*,misc-*'",
        "config_file": ".clang-tidy",
        "include": "*.[ch],*.[ch]xx,*.[ch]pp,*.[ch]++,*.cc,*.hh",
        "exclude": "",
    },
    "merge": {
        "changes": [
            {
                "diff": "@@ -4,9 +4,9 @@\n \n class TestReview {\n public:\n-  int name1;\n   std::string name2;\n   std::string name3;\n+  int name1;\n };\n \n std::string hello(std::string name) {\n",
                "new_path": "main.cpp",
                "old_path": "main.cpp",
                "a_mode": "100644",
                "b_mode": "100644",
                "new_file": false,
                "renamed_file": false,
                "deleted_file": false
            }
        ]
    }
}
```

--- 

## ToDo 
- [X] Testar com diferentes diffs do gitlab e analisar se vai ser necessário adicionar mais saídas na função `convert_git_lab_changes_to_unidiff`. Exemplo quando cria arquivo novo, renomeado etc
- [X] Converter o resultado o clang-tidy-review para o tipo da lista `comments` do processor
- [ ] Adicionar alguma validação nos campos do .config-json
- [ ] Trocar o comando do clang-tidy para utilizar o run-clang-tidy.py
- [ ] Analisar se há dependências 
- [ ] Criar unitários usando o pytest
- [X] Criar uma função para formatar o diff que vem do gitlab com o diff compatível do tipo --git
- [X] Adicionar as funções úteis do clang-tidy-review

---

## Thanks and Credits
- [@ZedThree](https://github.com/ZedThree)

---

