# Technical Learning Guides

Self-paced guides for people who know nothing about a technical subject yet.
Each guide takes you to a working, employable level by building one example
that grows from chapter to chapter.

New to Git or GitHub? Open [START-HERE.pdf](START-HERE.pdf) first.

## The four guide types

| Type | File | What it is |
|---|---|---|
| Learning guide | `<subject>-learning-guide.pdf` | The base guide. Starts from zero, covers one idea per chapter, and ends with a "Beyond the basics" roadmap. |
| Matn | `<subject>-matn.pdf` | The skeleton of the learning guide in a few pages. It states without explaining, so you can memorize it and remember what the guide covered. |
| Beyond the Basics | `<subject>-beyond-the-basics-learning-guide.pdf` | The next level, for someone who has finished the learning guide. |
| Way Beyond the Basics | `<subject>-way-beyond-the-basics-learning-guide.pdf` | The level after that. None written yet. |

Start with the learning guide. Use the matn to keep what you learned. Move on
to Beyond the Basics when your projects need it.

## Catalogue

The numbered folders under [`guides/`](guides) give the reading order. Each
subject has its own folder, which holds every guide type written for it.

### 1. Foundations

| Subject | Guides | Outcome | Prerequisites |
|---|---|---|---|
| Linux command line | [Guide](guides/1-foundations/linux-command-line/linux-command-line-learning-guide.pdf) · [Matn](guides/1-foundations/linux-command-line/linux-command-line-matn.pdf) | From an empty terminal to moving, searching, piping, automating and reusing what you typed. | None |
| Bash | [Guide](guides/1-foundations/bash/bash-learning-guide.pdf) | From a first script to one you can hand to a colleague and trust. | Linux command line |
| Markdown | [Guide](guides/1-foundations/markdown/markdown-learning-guide.pdf) | From an empty text file to a README, a wiki page and a set of docs. | None |
| Git | [Guide](guides/1-foundations/git/git-learning-guide.pdf) · [Habit card](cards/git-habit-card.pdf) | From an empty folder to a confident contributor on a shared repository. | Linux command line |
| Vim | [Guide](guides/1-foundations/vim/vim-learning-guide.pdf) | From "how do I quit this thing" to editing a real project fluently. | Linux command line |
| AI | [Guide](guides/1-foundations/ai/ai-learning-guide.pdf) | From never having asked an AI a question to using one every day as a checked working partner. | None |

### 2. Languages

| Subject | Guides | Outcome | Prerequisites |
|---|---|---|---|
| C | [Guide](guides/2-languages/c/c-learning-guide.pdf) | From a blank file to a multi-file program that manages its own memory. | Linux command line |
| C++ | [Guide](guides/2-languages/cpp/cpp-learning-guide.pdf) | From one compiled file to a multi-file program you can explain in a code review. | Some programming in any language |
| Systems programming | [Guide](guides/2-languages/systems-programming/systems-programming-learning-guide.pdf) | From a memory-managed language to a multi-threaded C tool you own every byte of. | A high-level language |

### 3. Build and test

| Subject | Guides | Outcome | Prerequisites |
|---|---|---|---|
| Make | [Guide](guides/3-build-and-test/make/make-learning-guide.pdf) | From one rule to a Makefile that rebuilds exactly what changed. | C |
| CMake | [Guide](guides/3-build-and-test/cmake/cmake-learning-guide.pdf) · [Matn](guides/3-build-and-test/cmake/cmake-matn.pdf) · [Beyond the Basics](guides/3-build-and-test/cmake/cmake-beyond-the-basics-learning-guide.pdf) | From zero to a tested, multi-directory, dependency-aware C++ project. | C or C++ |
| clang-format | [Guide](guides/3-build-and-test/clang-format/clang-format-learning-guide.pdf) | From one messy file to a codebase that formats itself. | C or C++, Git |
| Google Test | [Guide](guides/3-build-and-test/google-test/google-test-learning-guide.pdf) · [Matn](guides/3-build-and-test/google-test/google-test-matn.pdf) | From one assertion to a mocked, parameterized suite wired into CMake and CTest. | C++, CMake |
| Software-in-the-Loop (SIL) | [Guide](guides/3-build-and-test/sil/sil-learning-guide.pdf) | From a ten-line fake room to a scenario suite that runs your real C controller in CI. | C, a little Python |
| Hardware-in-the-Loop (HIL) | [Guide](guides/3-build-and-test/hil/hil-learning-guide.pdf) | From the SIL suite to the same scenarios running against a real microcontroller. | SIL (required) |

### 4. Systems and infrastructure

| Subject | Guides | Outcome | Prerequisites |
|---|---|---|---|
| Virtual machines | [Guide](guides/4-systems-and-infra/vm/vm-learning-guide.pdf) | From "what is a VM?" to running, cloning and SSH-ing into disposable Linux machines. | Linux command line |
| Docker | [Guide](guides/4-systems-and-infra/docker/docker-learning-guide.pdf) | From "it works on my machine" to a multi-container app you can ship anywhere. | Linux command line |
| CI/CD pipelines | [Guide](guides/4-systems-and-infra/ci-cd-pipeline/ci-cd-pipeline-learning-guide.pdf) | From no automation to a pipeline that tests, builds, deploys and verifies on every change. | Git |
| Signed releases | [Guide](guides/4-systems-and-infra/signed-releases/signed-releases-learning-guide.pdf) · [sha256sum card](cards/sha256sum-explained.png) | From never having heard of a signature to publishing and verifying signed releases with minisign. | Linux command line |

### 5. Web

| Subject | Guides | Outcome | Prerequisites |
|---|---|---|---|
| Web protocols | [Guide](guides/5-web/web-protocols/web-protocols-learning-guide.pdf) | From "two computers want to talk" to a service that speaks HTTP, WebSockets and gRPC. | A little Python |
| OCPP | [Guide](guides/5-web/ocpp/ocpp-learning-guide.pdf) | From a first BootNotification to a backend that runs real charging sessions. | Python with async/await, Web protocols |

### 6. Embedded

| Subject | Guides | Outcome | Prerequisites |
|---|---|---|---|
| Linux vs. RTOS | [Guide](guides/6-embedded/linux-vs-rtos/linux-vs-rtos-learning-guide.pdf) | From "they are both operating systems" to choosing, building and measuring the right one. | C, Linux command line |
| Yocto | [Guide](guides/6-embedded/yocto/yocto-learning-guide.pdf) | From an empty build host to a custom Linux image booting on real hardware. | C, C++ or Python on Linux |
| I2C on Linux | [Guide](guides/6-embedded/i2c-linux/i2c-linux-learning-guide.pdf) | From two wires and a mystery chip to driving an MCP23017 from the shell and from code. | Linux command line |
| Functional safety | [Guide](guides/6-embedded/functional-safety/functional-safety-learning-guide.pdf) | From "the software works" to a safety argument you can defend, with ISO 26262. | C, embedded experience |

### Cards

[`cards/`](cards) holds one-page references for people who have already
learned a subject. A card helps you remember a subject. It does not teach it.

- [Git habit card](cards/git-habit-card.pdf)
- [sha256sum explained](cards/sha256sum-explained.png)
- [Learning guide tracker](cards/learning-guide-tracker.pdf), a printable progress sheet

## How a guide is made

Every subject starts with one question in a chat with Claude:

> Someone doesn't know *&lt;SKILL&gt;* at all. How would you introduce it to them?

You ask "and next?" as many times as you like, and then ask for the learning
guide. [`prompts/learning-guide-prompt.md`](prompts/learning-guide-prompt.md)
turns the conversation into the PDF. The other three guide types are built
from that learning guide. [`prompts/instructions.md`](prompts/instructions.md)
covers how Claude handles each request. How a guide gets reviewed and added
is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Reporting a mistake

Open an issue. Put the guide name and chapter number in the title, for example
`cmake-learning-guide, chapter 3: wrong flag in the configure step`.

## License

[CC BY 4.0](LICENSE).
