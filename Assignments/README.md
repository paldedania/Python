# Python assignment solutions

Completed against the [CodingGita Semester 1 Python folder](https://github.com/codinggita/CGxSU_Semester_1/tree/main/Semester_1/python), retrieved on 22 October 2026. The source inventory contains 38 files from `main`, with verified Git blob hashes in [the source manifest](verification/source-manifest.json).

The existing folder names and question numbering are retained. Each numbered script runs independently. Written answers cover theory, output questions and requested explanations. These are assistant-generated solutions, not evidence that the learner completed the exercises or predicted outputs before execution.

## Find a section

| Source topic | Local solutions and written answers |
| --- | --- |
| 00, if/else problem solving | [30 programs](00-Problem_Solving_Assignments/01.python_if_else/) |
| 00, basic nested loops | [25 programs](00-Problem_Solving_Assignments/02.python_for_loops_nested/) |
| 00, mixed problem solving | [50 programs](00-Problem_Solving_Assignments/03.python_for_loop/) |
| 00, extended nested loops | [120 programs and eight bonus programs](00-Problem_Solving_Assignments/04.nested_loop/README.md) |
| 01, introduction | [Written answers](01-basics-python/answers.md), [welcome.py](01-basics-python/welcome.py), [about_python.py](01-basics-python/about_python.py) |
| 02, variables | [Written answers and program references](02-variables/answers.md) |
| 03, data types | [Written answers and program references](03-Data-Type/answers.md) |
| 04, arithmetic | [Written answers](04-arithmetics_operators/answers.md), Q-1.py through Q-21.py, [combined practical file](04-arithmetics_operators/all_tasks.py) |
| 05, strings | [Written answers](05.Python_String_Operations/answers.md), Q-1.py through Q-40.py, [combined practical file](05.Python_String_Operations/all_tasks.py) |
| 06, Boolean expressions | [30 answers and programs](06.boolean_and_logical_expressions/README.md) |
| 07, input/output | [Explanations](07.Input_and_Output/answers.md), Q-1.py through Q-30.py |
| 08, conditions | [30 programs](08.Conditional_Statements/) |
| 09, understanding problems | [Five programs with problem analysis](09.intoduction_to_problem_solving/01/) |
| 09, IPO and algorithms | [Six programs with IPO, algorithms and dry runs](09.intoduction_to_problem_solving/02/) |
| 09, flowcharts and pseudocode | [30 programs with pseudocode and Mermaid flowcharts](09.intoduction_to_problem_solving/03.flowcharts_and_pseudocode/README.md) |
| 10, for loops | [30 programs and final challenge Q-31.py](10-For_Loop/) |
| 11, while loops | [31 existing while-loop practice programs](11-While_Loop/) |
| 12, match-case | [40 programs](12.Match_Case/), [44 output-practice answers](12.Match_Case/Practice.answers.md) |
| 13, loop controls | [40 programs and explanations](13.Break-Continue-Pass--For-Else/Assignment.answers.md), [35 output-practice answers](13.Break-Continue-Pass--For-Else/Practice.answers.md) |
| 14, input validation | [24 programs](14.Input_Validation/README.md) |
| 15, functions | [70 programs and written answers across three lessons](15.functions/README.md) |

The existing `03.python_while_nested_loop_EXTRA` folder contains 25 additional exercises. `template/` is a blank starter template, not an unfinished assignment section. Earlier learner answers in the loop-control `Practice.md` remain available; use `Practice.answers.md` for checked answers.

## Run a solution

Use Python 3.10 or later because the match-case exercises require it. From this folder:

```bash
python3 06.boolean_and_logical_expressions/Q-25.py
python3 00-Problem_Solving_Assignments/04.nested_loop/Q-110.py
python3 15.functions/02.parameters_return_arguments/Q-21.py
```

Follow any prompts. New scripts generally use plain `input()` without a prompt. Enter scalar values on separate lines and matrix rows as space-separated values. The extended nested-loop [README](00-Problem_Solving_Assignments/04.nested_loop/README.md) lists input order and interpretation choices. Input-validation Q16 takes the first number, operator, then second number. Q17 continues until menu option 4.

For Q110, for example, enter:

```text
3
3
1 2 3
4 5 6
7 8 9
```

The totals are 45 overall, 40 on the border, 15 on each diagonal and 5 inside.

The arithmetic and string worksheets request one file containing their practical tasks. Their `all_tasks.py` files provide that format alongside the separate question files. The string combined file asks for input as it reaches tasks 30 and 38 through 40. Names, cities and other example personal details are sample values.

## Verification

Run:

```bash
python3 verification/verify.py
```

The [recorded run](verification/results.json) on Python 3.14.7 passed all 783 execution cases. It checked syntax for 738 Python files, including the 30 starter templates and verification runner, and ran all 707 solution scripts at least once. Of the execution cases, 351 assert expected output or specific report values; the remaining cases check that programs finish successfully with representative input. This is not exhaustive proof for every possible input.

Checks include exact pattern spacing, all supplied loop-control programming examples with documented source corrections, Boolean boundaries, input-validation retry paths, rectangular matrix multiplication, empty strings, frequency ties, negative maxima and tic-tac-toe states. Each program has an eight-second timeout. The [fixtures](verification/cases.json) make the inputs and assertions reviewable.

## Source ambiguities

The extended nested-loop [README](00-Problem_Solving_Assignments/04.nested_loop/README.md) documents contradictory examples and rules chosen for unspecified questions. In particular, Q120 refers to 13 metrics without listing them; its implemented report metrics are listed there.

Additional choices in the mixed 50-question worksheet follow the existing solutions: password strength uses 4-5 satisfied conditions for Strong and 2-3 for Medium; usernames need five characters and an initial letter for Valid; a security scan treats password-like words or repeated special characters as Suspicious; multiplication classification gives multiples of five priority. These thresholds are implementation choices where the source gives no complete rule. Ties generally retain the first occurrence. Money and marks inputs follow the exercise assumptions rather than general application validation.
