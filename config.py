import os


ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR_PATH = os.path.join(ROOT, "docs")
SRC_DIR_PATH = os.path.join(ROOT, "src")


DIFFICULTIES = ["easy", "medium", "hard"]
DIFF_ORDERS = dict(
    zip(
        DIFFICULTIES, range(1, len(DIFFICULTIES) + 1)
    )
)


# Topics with abbreviated prefix.
ABBREVIATED_PREFIX_TOPICS = {"bfs", "dfs", "dp_memoization", "dp_tabulation"}
