# %% [markdown]
# ---
# title: A small decay experiment
# description: A minimal percent-format Python article rendered by Quarto.
# date: 2026-09-18
# categories: [python, visualization]
# draft: false
# jupyter: python3
# ---

# %% [markdown]
"""
This page is authored as a `.py` file using Jupyter percent cells. It does not
require an `.ipynb` notebook file or the Jupyter user interface.
"""

# %%
#| label: fig-decay
#| fig-cap: Exponential decay from a small Python computation.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4, 200)
y = np.exp(-x)

fig, ax = plt.subplots(figsize=(7, 3.5), facecolor="#faf9f5")
ax.set_facecolor("#faf9f5")
ax.plot(x, y, color="#d97757", linewidth=2.5)
ax.set(xlabel="time", ylabel="value", ylim=(0, 1.05))
ax.spines[["top", "right"]].set_visible(False)
plt.show()

# %% [markdown]
"""
The curve follows $y = e^{-x}$. See @fig-decay.
"""
