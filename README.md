# wiki

Personal notes and Python experiments published with Quarto.

Site: https://januvojta.github.io/wiki

## Local development

Install [Quarto](https://quarto.org/) and [uv](https://docs.astral.sh/uv/), then run:

```bash
uv sync
uv run quarto preview
```

The Python version is pinned in `.python-version`; dependencies are declared in
`pyproject.toml` and locked in `uv.lock`.

## Site structure

| Path | Purpose |
| --- | --- |
| `_quarto.yml` | Site configuration: navigation, search, footer, HTML options, execution caching, and output directory. |
| `index.qmd` | Home page linking to experiments and notes. |
| `about.qmd` | About page. |
| `experiments/index.qmd` | Experiment listing, sorted newest first, with categories and an RSS feed. |
| `experiments/<slug>/index.py` | Individual executable Python articles. |
| `notes/index.qmd` | Note listing, sorted alphabetically by title. |
| `notes/<slug>.qmd` | Individual reference notes. |
| `assets/` | Shared static assets. |
| `styles.css` | Custom typography, colors, page layout, and responsive styling. |
| `_freeze/` | Committed execution results and figures cached by Quarto. |
| `docs/` | Generated HTML, styles, scripts, and assets served by GitHub Pages. |
| `.nojekyll` | Disables Jekyll processing for the generated site. |
| `agent.md` | Repository guidance for coding agents. |

The navbar links to Experiments, Notes, and About; the site title links home.
Quarto supplies search, a table of contents, code-copy buttons, and KaTeX math
rendering. `styles.css` customizes the Cosmo theme with an ivory/charcoal/clay
palette and DM Sans / Source Serif 4 fonts loaded from Google Fonts.

## Adding content

### Notes

Create `notes/<slug>.qmd` with YAML front matter and Markdown content. Use
`notes/python.qmd` as a starting point. The note listing discovers `.qmd` files
in the `notes/` directory automatically.

### Experiments

Create `experiments/<slug>/index.py`, using `experiments/example/index.py` as a
template. Experiments use percent-format cells: `# %%` for Python and
`# %% [markdown]` for prose. The opening Markdown cell contains YAML metadata
such as title, description, date, categories, and `jupyter: python3`.

The experiment listing discovers `*/index.py` relative to `experiments/`.
Quarto executes the Python cells and embeds their output and figures in the
article. No authored `.ipynb` file or Jupyter user interface is needed.

## Building and publishing

```bash
uv run quarto render
git diff --check
```

Rendering writes the site to `docs/`. With `execute.freeze: auto`, Quarto reuses
cached experiment results until their source changes; execution results are
stored in `_freeze/`. Include updated `docs/` and relevant `_freeze/` files with
source changes when committing. Do not edit generated HTML directly.

GitHub Pages should be configured to **Deploy from a branch**, using **main**
and **/docs**. Publishing uses the committed output rather than a custom build
workflow. The root `.nojekyll` file is copied into `docs/` during rendering.

`_site/`, `.quarto/`, and `.venv/` are ignored local artifacts.
