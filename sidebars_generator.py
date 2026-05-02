import os
import json


BASE = "docs"

DIFFICULTIES = ["easy", "medium", "hard"]
DIFF_ORDERS = {"easy": 1, "medium": 2, "hard": 3}

# Topics with abbreviated prefix.
ABBREVIATED_PREFIX_TOPICS = {"bfs", "dfs", "dp_memoization", "dp_tabulation"}


def get_md_title(md_path: str, fallback: str) -> str:
    """Use frontmatter title; otherwise, use fallback."""
    with open(md_path, "r") as f:
        content = f.read()

    if content.startswith("---"):
        for line in content.split("\n")[1:]:
            if line.startswith("title:"):
                return line.replace("title:", "").strip().strip('"')

            if line == "---": break

    return fallback


def generate_sidebars() -> None:
    dsa_topics_list = []

    for dsa_topic in sorted(os.listdir(BASE)):  # Sort DSA topics.
        topic_path = os.path.join(BASE, dsa_topic)
        if not os.path.isdir(topic_path): continue

        groups = {}
        for problem in sorted(os.listdir(topic_path)):  # Sort w.r.t. problems' numbers.
            problem_path = os.path.join(topic_path, problem)
            if not os.path.isdir(problem_path): continue

            parts = problem.split("_")
            if len(parts) < 2: continue

            difficulty = parts[1].lower()
            if difficulty not in DIFFICULTIES: continue

            number = parts[0]

            for file in os.listdir(problem_path):  # Find .md file.
                if file.endswith(".md") or file.endswith(".mdx"):
                    stem = file.rsplit(".", 1)[0]

                    doc_id = f"{dsa_topic}/{problem}/{stem}"
                    fallback = (
                        f"{number}. {' '.join(w.capitalize() for w in stem.split('_'))}"
                    )

                    md_path = os.path.join(problem_path, file)
                    title = get_md_title(md_path, fallback)

                    groups.setdefault(difficulty, []).append(
                        {
                            "type": "doc",
                            "id": doc_id,
                            "label": title,
                        }
                    )

        if not groups: continue

        diff_categories = []
        for diff in DIFFICULTIES:
            if diff not in groups: continue

            diff_categories.append(
                {
                    "type": "category",
                    "label": diff.capitalize(),
                    "collapsed": True,
                    "items": groups[diff],
                }
            )

        topic_label = dsa_topic.replace("_", " ").title()

        if dsa_topic in ABBREVIATED_PREFIX_TOPICS:  # Needs special treatment.
            words = [word.capitalize() for word in topic_label.split(" ")]

            words[0] = words[0].upper()  # Make prefix entirely upper.
            topic_label = " ".join(words)

        dsa_topics_list.append(
            {
                "type": "category",
                "label": topic_label,
                "collapsed": True,
                "items": diff_categories,
            }
        )

    # Output sidebars.ts.
    output = "import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';\n\n"
    output += "const sidebars: SidebarsConfig = {\n"
    output += f"  tutorialSidebar: {json.dumps(dsa_topics_list, indent=2, ensure_ascii=False)},\n"
    output += "};\n\n"
    output += "export default sidebars;\n"

    with open("sidebars.ts", "w") as f:
        f.write(output)
    print("Created sidebars.ts.")


if __name__ == "__main__":
    generate_sidebars()
