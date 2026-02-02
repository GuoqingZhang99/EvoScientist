"""Middleware configuration for the EvoScientist agent."""

from pathlib import Path

from deepagents.middleware.skills import SkillsMiddleware

from .backends import MergedReadOnlyBackend

_DEFAULT_SKILLS_DIR = str(Path(__file__).parent / "skills")


def create_skills_middleware(
    skills_dir: str = _DEFAULT_SKILLS_DIR,
    workspace_dir: str = "./workspace/",
) -> SkillsMiddleware:
    """Create a SkillsMiddleware that loads skills.

    Merges user-installed skills (workspace/skills/) with system skills
    (package built-in). User skills take priority on name conflicts.

    Args:
        skills_dir: Path to the system skills directory (package built-in)
        workspace_dir: Path to the workspace root (user skills live under workspace/skills/)

    Returns:
        Configured SkillsMiddleware instance
    """
    merged = MergedReadOnlyBackend(
        primary_dir=str(Path(workspace_dir) / "skills"),
        secondary_dir=skills_dir,
    )
    return SkillsMiddleware(
        backend=merged,
        sources=["/"],
    )
