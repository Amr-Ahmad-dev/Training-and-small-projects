# 04 — Machine Learning: Titanic Logistic Regression

### `Copy_of_S3_Machine_Learning.ipynb`
**Trained on:** the Titanic dataset fetched directly from a GitHub raw CSV URL
(`datasciencedojo/datasets/master/titanic.csv`).

**Problem being solved:** binary classification (survival prediction) walkthrough:
- Load the CSV from the URL
- Binarize the target column and drop rows containing `'?'`/missing values
- Split into `X`/`y`, then train/test split (70/30)
- Train a `LogisticRegression` model (`lbfgs`, up to 10,000 iterations) and check the
  solver's iteration count
- Predict classes and class probabilities on the test set
- Evaluate with a confusion matrix and classification report
- Visualize the confusion matrix as a seaborn heatmap
- Plot the ROC curve and compute the AUC score

### `titanic_logistic_regression.ipynb` / `train.py`
**Trained on:** the Titanic dataset loaded from seaborn's built-in dataset loader
(`sns.load_dataset("titanic")`) — a different source/version of Titanic data than the
notebook above (different columns available, e.g. `alive`, `deck`, `embark_town`).

**Problem being solved:** the same class of problem (predict `survived`) via a more
condensed, "production-script"-style pipeline: drop redundant/leaky columns
(`alive`, `deck`), drop missing values and duplicates, one-hot encode remaining
categoricals (`pd.get_dummies`), split features/target, do a stratified train/test
split, scale features with `StandardScaler`, train a `LogisticRegression`
(`max_iter=1000`), predict on the held-out set, and print accuracy plus a full
classification report. `titanic_logistic_regression.ipynb` is this exact script
split across notebook cells (previously generated in this conversation); `train.py`
is the flat `.py` version it was built from.
