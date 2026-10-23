# rbf_interpreter

A ~150-line brainf*ck interpreter in Python (`main.py`), plus my original 2019 implementation (`2019-implementation/`).

## Run

```sh
python3 main.py <program.bf> [init_data]
```

- `init_data` (optional int, default 0) seeds cell 0; when non-zero, the tape is printed before execution starts.
- Standard 8 commands are supported (`+-[]><.,`), plus a non-standard `$` (see below).
- Cells are 8-bit and wrap (255 → 0 → 255); the tape is unbounded to the right (`<` past cell 0 is an error).

```sh
$ python3 main.py helloworld.bf
Hello World!
```

## Debug features

- **`$` command** — anywhere in your brainf*ck source, `$` prints a state dump: `---debug---`, the tape (up to 20 cells, truncated once no further cells exist), the current program counter, and the data pointer. All other non-command characters are ignored, so you can drop `$` into comments or dead code freely.
- **Init data** — passing a second argument seeds cell 0 and prints the tape first, so you can observe execution from a chosen starting state, e.g. `python3 main.py in1.bf 33`.

## Motivation

Written as a **no-AI, 1-hour interview live-coding task**: implement a working brainf*ck interpreter from scratch, no libraries, no references. The 2026 version in `main.py` is the result; it's kept small on purpose.

## 2019 implementation

`2019-implementation/` is my first attempt, written back when I was a fresh CE student — `RBF.py` is the interpreter, and `RBF_translator.py` transpiles brainf*ck into Python by string-generating function calls. Kept for comparison; expect it to be rough.

## License

GPL — see [LICENSE](LICENSE).
