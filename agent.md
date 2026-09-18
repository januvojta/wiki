# Agent guide

## Project

This repository is a personal wiki built with Quarto. Source pages are Quarto
Markdown (`.qmd`) and percent-format Python scripts (`.py`). The generated site
is published from `docs/` at https://januvojta.github.io/wiki.

See `README.md` for the directory structure and authoring workflow.

## Working conventions

- Keep changes focused and follow the existing content and styling patterns.
- Edit source files, not generated HTML in `docs/`.
- Put site-wide configuration in `_quarto.yml` and custom styling in `styles.css`.
- Preserve the ivory, charcoal, and clay palette, editorial typography, responsive
  layout, and compact footer with equal top and bottom spacing.
- Author experiments as `experiments/<slug>/index.py` using `# %%` cells. Do not
  replace them with authored `.ipynb` notebooks.
- Author notes as `notes/<slug>.qmd`. Keep title and description metadata useful
  for the listings; experiments also use dates and categories.
- Manage Python dependencies with uv; keep `pyproject.toml` and `uv.lock` in sync.

## Verification and generated output

1. Run `uv sync` when setting up the environment or changing dependencies.
2. After changing site content, configuration, or styles, run
   `uv run quarto render`.
3. Run `git diff --check` and review the generated changes.
4. For layout changes, inspect short and long pages at desktop and mobile widths.
   Check footer spacing and unintended overflow.

Quarto's `freeze: auto` caches experiment execution in `_freeze/`. Include
relevant `_freeze/` and `docs/` updates with source changes. `_site/`, `.quarto/`,
and `.venv/` are local artifacts, not publishing sources.

Publishing uses GitHub Pages from the `main` branch's `/docs` directory. Preserve
`.nojekyll` and its generated copy in `docs/`. Commit or push only when requested.
