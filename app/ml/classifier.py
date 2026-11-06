from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def build_classifier() -> Pipeline:
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
