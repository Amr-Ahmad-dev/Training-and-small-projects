# 03 — Data Preprocessing & Visualization

### `assigment2.py` (+ `students_dataset.xlsx` / `students_dataset_cleaned.csv`)
**Trained on:** `students_dataset.xlsx` — 210 rows with columns `Student_ID`, `Name`,
`Department`, `Age`, `Gender`, `Math`, `Physics`, `Chemistry`, `English`,
`Attendance`. `students_dataset_cleaned.csv` is this script's own output: the same
data after cleaning, written back out at the end of the script.

**Problem being solved:** an end-to-end pandas/NumPy/Matplotlib exercise on a
gradebook dataset:
- Load the Excel file and inspect it (`head`, `tail`, `info`, `shape`, `describe`)
- Clean it: drop missing values, drop full duplicates, drop duplicate `Student_ID`s
- Feature engineer `Average` and `total` marks across the four subjects, and derive a
  letter `Grade` from the average via nested `np.where`
- Compute male/female counts, highest/lowest average, students scoring ≥85, and
  students with attendance ≤70
- Sort by average and pull the top/bottom 10 students
- Append a computed "Average_row" summary row to the dataframe
- Build a 2×2 Matplotlib figure: bar chart of per-subject averages, pie chart of
  department distribution, histogram of averages, and a line plot of average vs. name
- Export the cleaned dataframe to `students_dataset_cleaned.csv`
- A short NumPy segment at the end: convert the four subject columns to a NumPy
  array and inspect its shape/ndim/dtype, slice a row/column, and clip scores after
  adding 5 points (capped at 100)

### `S3_Preprocessing_and_Visualization_task.ipynb`
**Trained on:** seaborn's built-in `tips` dataset (restaurant bills and tips), loaded
via `sns.load_dataset('tips')`.

**Problem being solved:** a tour of seaborn plot types on the same dataset, one plot
type per cell — line plot, scatter plot, bar plot (grouped by day/sex), histogram,
box plot, violin plot, pair plot, count plot, and joint plot — practicing when to
reach for each visualization for numeric vs. categorical relationships.
