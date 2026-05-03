import os
import json
from config import DOCS_DIR_PATH, SRC_DIR_PATH, DIFFICULTIES, ABBREVIATED_PREFIX_TOPICS

problems = []


for dsa_topic in sorted(os.listdir(DOCS_DIR_PATH)):
    dsa_topic_path = os.path.join(DOCS_DIR_PATH, dsa_topic)
    if not os.path.isdir(dsa_topic_path): continue

    for problem in sorted(os.listdir(dsa_topic_path)):
        problem_path = os.path.join(dsa_topic_path, problem)
        if not os.path.isdir(problem_path): continue

        parts = problem.split("_")
        if len(parts) < 2: continue

        difficulty = parts[1].lower()
        if difficulty not in DIFFICULTIES: continue

        number_str = parts[0]  # Has left padded zeros.
        number = int(parts[0])
        padded_zeros_count = len(number_str) - len(str(number))

        title, doc_id = None, None  # Find .md to get title.

        for file in os.listdir(problem_path):
            if file.endswith(".md") or file.endswith(".mdx"):
                md_path = os.path.join(problem_path, file)
                with open(md_path, "r") as f:
                    content = f.read()

                if content.startswith("---"):
                    for line in content.split("\n")[1:]:
                        if line.startswith("title:"):
                            title = line.replace("title:", "").strip().strip('"')

                        if line == "---": break

                stem = file.rsplit(".", 1)[0]
                doc_id = f"{dsa_topic}/{problem}/{stem}"
                break

        if not title or not doc_id: continue

        image = None  # Find efficiency png.

        for file in os.listdir(problem_path):
            if file.endswith("efficiency.png"):
                image = f"/SkyHorse/img/efficiency/{number_str}_efficiency.png"
                break

        topic_label = dsa_topic.replace("_", " ").title()

        if dsa_topic in ABBREVIATED_PREFIX_TOPICS:  # Needs special treatment.
            words = [word.capitalize() for word in topic_label.split(" ")]

            words[0] = words[0].upper()  # Make prefix entirely upper.
            topic_label = " ".join(words)

        problems.append(
            {
                "number": number,
                "title": title[padded_zeros_count:],  # Remove left padded zeros from title.
                "topic": topic_label,
                "difficulty": difficulty.capitalize(),
                "docId": doc_id,
                "img": image,
            }
        )

problems.sort(key=lambda x: x["number"], reverse=True)

data_directory_path = os.path.join(SRC_DIR_PATH, "data")
problems_json_path = os.path.join(data_directory_path, "problems.json")

with open(problems_json_path, "w") as f:
    json.dump(problems, f, ensure_ascii=False, indent=2)

print(f"Created problems.json. Covered {len(problems)} problems.")
