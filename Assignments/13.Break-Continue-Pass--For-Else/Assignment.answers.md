# Loop-control assignment explanations

Source: [Assignment](https://github.com/codinggita/CGxSU_Semester_1/blob/main/Semester_1/python/13.Break_Continue_Pass_For_Else/Assignment.md).

The scripts retain the worksheet question numbers across A to E. Outputs below use `\n` to mark a line break. These are assistant answers checked by running the code, not learner predictions.

| Question | Exact output |
| --- | --- |
| 1 | `1\n2\n3\n4\nFinished\n` |
| 2 | `s\nk\ny\nl\n` |
| 3 | `2\n4\n6\n` |
| 7 | `1 1\n1 2\n2 1\n2 2\n3 1\n3 2\n` |
| 9 | `1\n2\n3\n5\n6\n` |
| 10 | `dctn` with no final newline in the source |
| 11 | `1\n2\n4\n5\n` |
| 15 | `A 1\nB 1\nA 3\nB 3\nA 4\nB 4\n` |
| 18 | `1\n2\n3\nDone\n` |
| 19 | `1\n3\n4\nCompleted\n` |
| 20 | `1\n2\nOutside loop\n` |
| 21 | `Else block\n` |
| 25 | `All are even\n` |
| 26 | `A\nC\n` |
| 28 | `1\n2\n3\n` |
| 29 | `Finished\n` |
| 30 | `Loop ended\n` |
| 33A | `1\n2\n3\n4\n` |
| 33B | `1\n2\n4\n` |
| 35 | `1\n3\n` |
| 38 | `1 1\n1 3\nInner loop completed\n2 1\n2 3\nInner loop completed\n` |

Q7: `break` affects the nearest loop, so the outer loop starts its next row.

Q15: both `print` statements are skipped when i is 2.

Q16: update n before testing `continue`. Otherwise n stays at 3 forever.

Q26: A runs because `continue` does not break the loop. B does not run because `break` occurs. C runs because an empty iterable finishes without breaking.

Q27: report the first character by original position whose total frequency is at least two. This gives `l` for `level`, not `e`.

Q31: `pass` does nothing, so execution reaches the following print even for even values. The script accepts the upper limit, allowing both 5 and 3.

Q32: the chosen messages are `Option 1 selected` and `Unknown option`. Choice 2 produces only `Program closed`.

Q33: `pass` falls through to print; `continue` skips printing 3.

Q34: use `continue`. `break` would stop at 3, leaving only 1 and 2. `pass` would print 3 too.

Q35: 2 is skipped; 4 breaks the loop. The loop's else does not run.

Q38: rows 1 and 2 finish without a break, so their inner else runs. Row 3 breaks at column 1 and has no output or else.

Q40: in order, use break, continue, for-else, pass, continue, break, for-else, pass.

Source corrections: Q13's `mississippi` example should produce `miiippi`, preserving all four i characters before removing s. Q17's `education` example has four non-vowels, `dctn`. The supplied local Practice.md contains earlier learner answers; corrected answers are in Practice.answers.md so the earlier attempts remain intact.
