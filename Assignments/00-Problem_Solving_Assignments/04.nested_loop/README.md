# Nested-loop solutions

Q-1.py through Q-120.py and B1.py through B8.py solve the [source worksheet](https://github.com/codinggita/CGxSU_Semester_1/blob/main/Semester_1/python/00.Problem_Solving_Assignments/04.nested_for_loop.md), retrieved 22 October 2026. Each script runs independently with Python 3. Run `python3 Q-110.py`, for example.

For scalar inputs, enter one value per line in the order named by the question. Text inputs occupy a complete line. Matrix inputs use one space-separated row per line. Unless fixed in the question, enter row count and column count first. Counts are positive unless a script explicitly handles an empty case.

| Questions | Input details |
| --- | --- |
| 3 | Character, row count, column count |
| 4, 9, 11, 66, 76, 77 | Row count, column count |
| 13, 16 | No input |
| 24, 25, 28, 82, 83, 88, 92 | Two strings or numbers on separate lines |
| 53 | A, B |
| 54 | A, B, limit |
| 56 | N, target |
| 70 | Word, N |
| 73 | Three lines, four marks per line |
| 75, 78 | Student count, day count, one P/A row per student |
| 96, 97, 99, 109, 110, 115, 117-120 | Row count, column count, then rows; Q115 adds target last |
| 98 | Customer count, product count, price row, then quantity rows |
| 100 | Row count, then two cells per row; 0 available, 1 booked |
| 111 | N, then N rows for A and N rows for B |
| 112 | Rows, columns, A rows, B rows |
| 113 | A rows, A columns, B rows, B columns, then A rows and B rows |
| 114 | Three rows of X/O/- separated by spaces |

## Source inconsistencies and chosen rules

- Q14 says 1 to 5 but demonstrates N=3. The solution accepts N.
- Q23 incorrectly says all pairs other than A/A are different for AB. B/B is Same too.
- Q34 prints ordered pairs of different positions, including reverse pairs. Identical characters at different positions have difference zero.
- Q36-Q42 are marked SKIP in the source. Solutions are included because this request covers the folder.
- Q37-Q40 print each unordered pair of different positions once. Q36 and Q41 print every ordered pair.
- Q46 follows the stated inner range 1 through i. For N=4 its rows are empty, 2, 2, and 2 4. The supplied sample instead implies a different range.
- Q64 uses increasing numbers in centered rows of widths 2N-1 down to 1.
- Q69 prints the full square width, including trailing spaces needed to retain the grid.
- Q79-Q90 preserve first appearance on ties unless otherwise stated. Repeated-character searches use original position order.
- Q88 defines matching frequency as the number of equal cross-string position pairs. For ABCA/BCAD, A scores 2 and B/C score 1. The source's B-or-C example conflicts with this rule. The rule and tie handling are explicit in the script.
- Q90 means second distinct frequency. For AABBBCC, A wins the second-place tie by first appearance. When all frequencies tie there is no second distinct frequency.
- Q91 counts distinct shared characters; ties retain the earliest word pair.
- Q92 counts distinct shared digits, so repeating a digit does not inflate the count.
- Q94 uses the general Armstrong definition, digit raised to digit count. Thus 1 through 9 all qualify. The sample omits 2 through 9; a fixed cube rule would match that sample but excludes valid four-digit Armstrong numbers.
- Q95 prints unordered prime pairs in 2 through N. Their prime sum may exceed N.
- Q98's second bill is 1000, from 1×100 + 4×200 + 2×50. The source's 950 is an arithmetic error.
- Q101 gives the main diagonal priority at the center. B5 priority is border, main diagonal, opposite diagonal, then interior.
- Q102 centers string prefixes with spaces between characters so each added character expands the row by two columns.
- Q107 classifies the column number as even or odd; X takes diagonal priority.
- Q109/Q120 use a pass mark of 40 in every subject. Grade thresholds are 90, 75, 60 and 40. Ties retain the first student. Marks must be between 0 and 100.
- Q115 reports zero-based row and column positions.
- Q116 uses ASCII letter/digit classes; other characters are special.
- Q119's sample monthly totals are 250, 250 and 250. The months tie; the solution reports month 1 under the first-on-ties rule, rather than incorrectly calling month 3 strictly highest.

Q120 refers to "13 requested metrics" without listing them. The implemented report covers these 13 metric groups: individual marks, student totals, student averages, student high/low marks, student pass/fail, grades, subject totals, subject averages, subject high/low marks, subject pass/fail counts, class total/average, highest/lowest students and overall marks, and class pass/fail counts with pass percentage. These are documented assumptions, not missing source requirements claimed as known.
