# 🚀 Data Science & Machine Learning Curriculum Repository

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Data Wrangling](https://img.shields.io/badge/Data%20Wrangling-Pandas%20%7C%20NumPy-150458.svg)](https://pandas.pydata.org/)
[![Visualization](https://img.shields.io/badge/Visualization-Matplotlib%20%7C%20Seaborn-blueviolet.svg)](https://seaborn.pydata.org/)
[![Ensemble](https://img.shields.io/badge/Ensemble-XGBoost-success.svg)](https://xgboost.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-GitHub%20Publish--Ready-brightgreen.svg)](#)

A structured, end-to-end repository spanning core **Python Foundations**, **Data Preprocessing & Exploratory Analysis**, **Supervised & Unsupervised Machine Learning**, **Ensemble Architectures**, and **Web Scraping**.

---

## 🏛️ Repository Architecture

```text
training/
├── 01-python-foundations/
│   ├── 01-control-flow-and-loops/
│   │   ├── README.md
│   │   └── control_flow_and_loops.ipynb
│   ├── 02-functions-and-modular-programming/
│   │   ├── README.md
│   │   └── functions_and_modular_programming.ipynb
│   └── 03-object-oriented-programming/
│       ├── README.md
│       └── object_oriented_programming.ipynb
│
├── 02-data-preprocessing-and-analysis/
│   ├── 01-numpy-numerical-computing/
│   │   ├── README.md
│   │   └── numpy_numerical_computing.ipynb
│   ├── 02-pandas-data-manipulation/
│   │   ├── README.md
│   │   └── pandas_data_manipulation.ipynb
│   ├── 03-data-visualization-matplotlib-seaborn/
│   │   ├── README.md
│   │   └── data_visualization_matplotlib_seaborn.ipynb
│   └── 04-titanic-eda-and-feature-engineering/
│       ├── README.md
│       └── titanic_eda_and_feature_engineering.ipynb
│
├── 03-machine-learning/
│   ├── 01-linear-and-polynomial-regression/
│   │   ├── README.md
│   │   └── linear_and_polynomial_regression.ipynb
│   ├── 02-feature-engineering-and-regularization/
│   │   ├── README.md
│   │   └── feature_engineering_and_regularization.ipynb
│   ├── 03-knn-and-svm-classification/
│   │   ├── README.md
│   │   └── knn_and_svm_classification.ipynb
│   ├── 04-ensemble-learning-bagging-boosting/
│   │   ├── README.md
│   │   └── ensemble_learning_bagging_boosting.ipynb
│   ├── 05-unsupervised-clustering-kmeans-dbscan/
│   │   ├── README.md
│   │   └── unsupervised_clustering_kmeans_dbscan.ipynb
│   └── 06-breast-cancer-diagnostic-benchmark/
│       ├── README.md
│       └── breast_cancer_diagnostic_benchmark.ipynb
│
└── 04-web-scraping/
    └── 01-web-scraping-bs4-requests/
        ├── README.md
        ├── web_scraping_bs4_requests.ipynb
        └── web_scraping_template.py
```

---

## 🏆 Project Rankings & Comprehensive Evaluation Report

Every notebook in this repository was rigorously inspected for computational depth, architectural completeness, real-world applicability, and visual rigor. Below is the ranked evaluation report:

| Rank | Project Name | Directory | Significance | Score (1-100) | Primary Highlights |
|:---:|---|---|:---:|:---:|---|
| **#1** | **Wisconsin Breast Cancer Diagnostic Benchmark** | [`03-machine-learning/06-breast-cancer-diagnostic-benchmark`](./03-machine-learning/06-breast-cancer-diagnostic-benchmark) | **Significant** (Top Tier) | **99/100** | Full clinical diagnostic ML pipeline, correlation heatmap, 6 competitive ensemble models (HistGradientBoosting, ExtraTrees, RandomForest, AdaBoost, etc.), multi-metric evaluation (Accuracy, Precision, Recall, F1, ROC-AUC), top accuracy of 98.25% with 100% recall. |
| **#2** | **Titanic Survival Analysis: End-to-End EDA** | [`02-data-preprocessing-and-analysis/04-titanic-eda-and-feature-engineering`](./02-data-preprocessing-and-analysis/04-titanic-eda-and-feature-engineering) | **Significant** (Top Tier) | **97/100** | 55-cell end-to-end data science study on real-world passenger records: missing value imputation, multi-variable statistical visualization (histograms, boxplots, violinplots), and feature engineering (`family_size`, `alone`). |
| **#3** | **Ensemble Learning: Bagging, Boosting & XGBoost** | [`03-machine-learning/04-ensemble-learning-bagging-boosting`](./03-machine-learning/04-ensemble-learning-bagging-boosting) | **Significant** (Top Tier) | **95/100** | 36 cells and 175 lines of code. Decision tree bagging with feature importance extraction, KNN bagging with estimator tuning curve (1..50), and a multi-boosting benchmark (AdaBoost vs Gradient Boosting vs XGBoost). |
| **#4** | **Feature Engineering, Overfitting & Regularization** | [`03-machine-learning/02-feature-engineering-and-regularization`](./03-machine-learning/02-feature-engineering-and-regularization) | **Significant** | **92/100** | Demonstrates the bias-variance tradeoff: categorical encoders, feature scalers, deliberate overfitting with 15th-degree polynomials, train/test $R^2$ divergence visualization, and mathematical regularization via Lasso (L1) and Ridge (L2). |
| **#5** | **Statistical Visualization (Matplotlib & Seaborn)** | [`02-data-preprocessing-and-analysis/03-data-visualization-matplotlib-seaborn`](./02-data-preprocessing-and-analysis/03-data-visualization-matplotlib-seaborn) | **Significant** | **90/100** | Systematic visualization masterclass: line plots, scatter, bar charts, histograms, box plots, countplots, heatmaps, subplots layout, and customized styling palettes. |
| **#6** | **Supervised Classification: KNN & SVM** | [`03-machine-learning/03-knn-and-svm-classification`](./03-machine-learning/03-knn-and-svm-classification) | **Significant** | **88/100** | Instance-based vs maximum-margin classification: 5-fold cross-validated grid search across $k$, $k$-accuracy tuning curve, Linear SVM fitting, and 2D decision boundary contour visualization. |
| **#7** | **Object-Oriented Programming (OOP) in Python** | [`01-python-foundations/03-object-oriented-programming`](./01-python-foundations/03-object-oriented-programming) | **Significant** | **86/100** | 258 lines of modular OOP: classes, `__init__`, state encapsulation, inheritance, method overriding, `super()`, and practical domain models (Banking, Library, Student Information System). |
| **#8** | **Data Wrangling & Manipulation with Pandas** | [`02-data-preprocessing-and-analysis/02-pandas-data-manipulation`](./02-data-preprocessing-and-analysis/02-pandas-data-manipulation) | **Significant** | **85/100** | 61 cells covering Series, DataFrames, indexing (`.loc`, `.iloc`), conditional filtering, missing data treatment (`dropna`, `fillna`), groupby aggregation, and relational sorting. |
| **#9** | **Unsupervised Clustering: K-Means & DBSCAN** | [`03-machine-learning/05-unsupervised-clustering-kmeans-dbscan`](./03-machine-learning/05-unsupervised-clustering-kmeans-dbscan) | Foundational / Moderate | **81/100** | Centroid-based vs density-based clustering: feature scaling, K-Means centroid convergence plotting, DBSCAN neighborhood tuning (`eps`, `min_samples`), and spatial outlier isolation. |
| **#10** | **Linear & Polynomial Regression Modeling** | [`03-machine-learning/01-linear-and-polynomial-regression`](./03-machine-learning/01-linear-and-polynomial-regression) | Foundational / Moderate | **79/100** | Simple OLS linear regression, multiple regression, polynomial feature transformation, and visual regression line overlays. |
| **#11** | **Numerical Computing with NumPy** | [`02-data-preprocessing-and-analysis/01-numpy-numerical-computing`](./02-data-preprocessing-and-analysis/01-numpy-numerical-computing) | Foundational | **78/100** | 64 cells of tensor fundamentals: array creation, strided slicing, boolean masking, vectorized broadcasting, dot products, and multi-axis statistical reductions. |
| **#12** | **Python Functions & Modular Programming** | [`01-python-foundations/02-functions-and-modular-programming`](./01-python-foundations/02-functions-and-modular-programming) | Foundational | **75/100** | 52 cells covering function signatures, default arguments, `*args`, `**kwargs`, lambda functions, map/filter, scope rules (LEGB), closures, and decorators. |
| **#13** | **Python Control Flow & Loops** | [`01-python-foundations/01-control-flow-and-loops`](./01-python-foundations/01-control-flow-and-loops) | Foundational | **73/100** | 52 cells covering procedural iteration: `for`, `while`, `break`, `continue`, `range()`, nested loops, and algorithmic patterns (prime numbers, Fibonacci). |
| **#14** | **Web Scraping with BS4 & Requests** | [`04-web-scraping/01-web-scraping-bs4-requests`](./04-web-scraping/01-web-scraping-bs4-requests) | Foundational Lab | **68/100** | Web data extraction: HTTP GET requests with custom User-Agent headers, BeautifulSoup HTML parsing, tag decomposition, and target site testing. |
| **#15** | **Web Scraping Framework Scaffolding** | [`04-web-scraping/01-web-scraping-bs4-requests`](./04-web-scraping/01-web-scraping-bs4-requests) | Scaffolding | **50/100** | Starter import skeleton (`web_scraping_template.py`) including Scrapy, Selenium, BeautifulSoup, and Pandas. |

---

## 🛠️ Technology Stack & Dependencies

| Domain | Libraries & Tools |
|---|---|
| **Core Language** | Python 3.8+ |
| **Data Manipulation** | `pandas`, `numpy`, `scipy` |
| **Visualization** | `matplotlib`, `seaborn` |
| **Machine Learning** | `scikit-learn`, `xgboost` |
| **Web Scraping** | `requests`, `beautifulsoup4`, `html5lib`, `scrapy`, `selenium` |
| **Environment** | Jupyter Notebook / JupyterLab |

---

## ⚡ Quickstart Guide

### 1. Clone or Open the Repository
```bash
git clone https://github.com/<your-username>/data-science-curriculum.git
cd data-science-curriculum
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost requests beautifulsoup4 html5lib scrapy selenium jupyter
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 📜 Documentation Integrity & Compliance
- **Code Preservation**: All original code cells, variable assignments, mathematical formulations, and execution outputs were preserved with 100% integrity without altering logic.
- **Architectural Organization**: Files have been reorganized from unstructured downloads into domain-specific, modular folders.
- **Documentation**: Every project includes an individualized `README.md` and in-notebook overview header.
