from pydantic import BaseModel
from typing import List

class Commit(BaseModel):
    message: str

class Changelog(BaseModel):
    changes: List[str] = []

def generate_changelog(commits: List[Commit]) -> str:
    changelog = Changelog()

    for commit in commits:
        changelog.changes.append(commit.message)

    return "\n".join([f"- {change}" for change in changelog.changes])

# Example usage
commits = [
    Commit(message="Add feature A"),
    Commit(message="Fix bug B"),
    Commit(message="Update documentation")
]

changelog = generate_changelog(commits)

with open("CHANGELOG.md", "w") as f:
    f.write(changelog)
