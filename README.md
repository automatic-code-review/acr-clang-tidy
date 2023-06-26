# Automatic Code Review - Clang Tidy
1. Recebe um diff como entrada
2. Executa o clang-tidy com as configurações definidas no config.json
3. Retorna uma lista de comentários com os warnings capturados pelo clang-tidy que serão usados pelo [automatic-code-review-processor](https://github.com/automatic-code-review/automatic-code-review-processor)
4. Resulta em comentários em merges requests com os warnings do clang-tidy

---

## Arquivo config.json
```json
{
    "path_output": "clang-tidy-review-output.json",
    "clang_tidy": {
        "build_dir": "build/",
        "binary_dir": "clang-tidy",
        "checks": "'-*,performance-*,readability-*,bugprone-*,clang-analyzer-*,cppcoreguidelines-*,mpi-*,misc-*'",
        "config_file": ".clang-tidy",
        "include": "*.[ch],*.[ch]xx,*.[ch]pp,*.[ch]++,*.cc,*.hh",
        "exclude" "",
    }
}
```

--- 

## ToDo 
- [] Converter o resultado o clang-tidy-review para o tipo da lista `comments` do processor
- [] Analisar como formatar o `diff` no formato certo com o `unidiff`
- [] Adicionar alguma validação nos campos do .config-json
- [] Trocar o comando do clang-tidy para utilizar o run-clang-tidy.py
- [] Analisar se há dependências 
- [] Criar unitários usando o pytest
- [X] Adicionar as funções úteis do clang-tidy-review

---

## Thanks and Credits
- [@ZedThree](https://github.com/ZedThree)

---

