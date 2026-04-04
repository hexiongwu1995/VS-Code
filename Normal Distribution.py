import matplotlib.pyplot as plt
import numpy as np
# Required to explicitly type-annotate the axes dictionary.
# Without this import, Pylance cannot resolve 'Axes' as a type.
from matplotlib.axes import Axes
# 'cast' is a zero-cost typing helper: it has NO runtime effect,
# but tells Pylance to treat a value as a specific type.
from typing import cast

mosaic = [['PDF','Hist'], ['PDF','Hist']]
fig, ax = plt.subplot_mosaic(mosaic, figsize=(7,3), width_ratios= [1.1, 1] )
# --- Why cast() is needed here ---
# plt.subplot_mosaic() returns dict[str, Any] according to matplotlib's
# type stubs (*.pyi files), because the keys depend on runtime input and
# cannot be statically determined.
#
# If you use a variable annotation instead:
#   ax: dict[str, Axes]          # annotation
#   fig, ax = plt.subplot_mosaic(...)  # assignment
# Pylance merges the annotated type with the inferred type, producing
# dict[str, Any | Axes].  As a result, ax['PDF'].plot is typed as
# 'Any | (...) -> list[Line2D]', which breaks IntelliSense formatting.
#
# cast(dict[str, Axes], ax) tells Pylance:
#   "Treat 'ax' as exactly dict[str, Axes] — do NOT union with Any."
# This makes ax['PDF'] resolve cleanly as Axes, so hovering over .plot()
# or .hist() shows well-formatted signatures identical to .scatter().

ax = cast(dict[str, Axes], ax)

# --- What does "dict[str, Axes]" mean? ---
# dict[KeyType, ValueType] is Python's generic type annotation syntax for
# dictionaries.  It specifies the exact types of keys and values:
#
#   dict[str, Axes]
#    │         └─ ValueType: every value is a matplotlib Axes object
#    └─────────── KeyType:   every key is a string
#
# After plt.subplot_mosaic(), 'ax' holds a plain Python dict whose keys are
# the subplot labels you defined in 'mosaic', and whose values are the
# corresponding Axes instances, e.g.:
#
#   ax = {
#       'PDF':  <Axes object>,   # key='PDF'  (str),  value=Axes
#       'Hist': <Axes object>    # key='Hist' (str),  value=Axes
#   }
#
# Why not just write "dict" without [str, Axes]?
#
#   Annotation          | What Pylance knows about ax['PDF']
#   -------------------|--------------------------------------
#   dict                | unknown — no type info at all
#   dict[str, Any]      | it's something, but methods are unresolved
#   dict[str, Axes]     | it is an Axes object → full IntelliSense available
#
# Providing the precise value type 'Axes' is what enables Pylance to show
# well-formatted hover documentation for ax['PDF'].plot(), ax['Hist'].hist(),
# etc., identical to what you see for ax.scatter() when ax is a plain Axes.

mu, sigma = 1.2, 2.3

# Probability Density Function
x_PDF = np.linspace(start=mu- 4*sigma, stop=mu+ 4*sigma, num=200, endpoint=True)
y_PDF = 1/(sigma * np.sqrt(2*np.pi)) * np.exp( (-(x_PDF-mu)**2)/(2*sigma**2) )
ax['PDF'].plot(x_PDF, y_PDF, color="blue", linewidth=1, linestyle="solid", label="PDF")
ax['PDF'].set_xlabel(r'$x$', fontsize=8)
ax['PDF'].set_ylabel('Probability  density', fontsize=8)
ax['PDF'].set_title("PDF of Normal Distribution", fontsize=8)
ax['PDF'].axis([mu-4.5*sigma, mu+4.5*sigma, 0, 0.25])
ax['PDF'].set_xticks([mu-3*sigma, mu-2*sigma, mu- sigma, mu, mu+ sigma, mu+ 2*sigma, mu+3*sigma], [r"$\mu -3 \sigma$", r"$\mu -2 \sigma$", r"$\mu - \sigma$", r"$\mu$", r"$\mu + \sigma$", r"$\mu +2 \sigma$", r"$\mu +3 \sigma$"])
ax['PDF'].tick_params(axis="x", labelsize=7, labelrotation=-90, direction='in', color=(0,0,1,0.3))

ax['PDF'].fill_between(x_PDF, y_PDF, 0, where=((x_PDF > mu- 1*sigma) & (x_PDF < mu+ 1* sigma)), color="blue", alpha=0.1, label= r"$\mu \pm 1 \sigma$(68.27%)" )
ax['PDF'].fill_between(x_PDF, y_PDF, 0, where=((x_PDF > mu- 2*sigma) & (x_PDF < mu+ 2* sigma)), color="blue", alpha=0.1, label= r"$\mu \pm 2 \sigma$(95.45%)" )
ax['PDF'].fill_between(x_PDF, y_PDF, 0, where=((x_PDF > mu- 3*sigma) & (x_PDF < mu+ 3* sigma)), color="blue", alpha=0.1, label= r"$\mu \pm 3 \sigma$(99.73%)" )

ax['PDF'].text(mu-4.2*sigma, 0.22, r'$P(x)= \frac{1}{\sqrt{2 \pi  \sigma^2} } exp(-\frac{(x- \mu)^2}{2 \sigma^2} )$', fontsize=8)
ax['PDF'].legend(fontsize=6, loc='upper right')

# Histogram of Normal Distribution

norm_samples=np.random.normal(loc=mu, scale=sigma, size=1000)
ax['Hist'].hist(norm_samples, bins=15, density=True, cumulative=False, histtype='bar', orientation='vertical', color=(0,0,1, 0.2), label='histogram', edgecolor=(1,1,1))
ax['Hist'].set_xticks([mu - 3*sigma, mu - 2*sigma, mu - 1*sigma, mu, mu + 1*sigma, mu + 2*sigma, mu + 3*sigma],[r'$\mu - 3 \sigma$', r'$\mu - 2 \sigma$', r'$\mu - 1 \sigma$', r'$\mu$', r'$\mu + 1 \sigma$', r'$\mu + 2 \sigma$', r'$\mu + 3 \sigma$'])
ax['Hist'].tick_params(axis='x', pad= 2, labelsize=8, labelrotation=-90, direction='in', color=(0,0,1,0.3))
ax['Hist'].set_xlim(left=mu - 4* sigma, right= mu + 4* sigma)
ax['Hist'].set_xlabel(r'normal samples', fontsize=8)
ax['Hist'].set_ylabel('Probability density', fontsize=8)
ax['Hist'].set_title('Histogram of Normal Samples', fontsize=8)
ax['Hist'].legend(fontsize=6, loc='best')

fig.subplots_adjust(left=0.1, wspace=0.5, right=0.95, bottom=0.2, top=0.9)
plt.show()



