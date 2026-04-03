import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Hashable

# ============================================================================
# UNDERSTANDING ASTERISKS IN FUNCTION DEFINITIONS
# ============================================================================

# SINGLE ASTERISK (*): Marks the boundary for keyword-only arguments
# All parameters after * MUST be passed by name, not by position.
# In subplot_mosaic: sharex, sharey, width_ratios, etc. are keyword-only.
# Example: subplot_mosaic(mosaic, sharex=True) ✓
#          subplot_mosaic(mosaic, True) ✗ (TypeError!)

# DOUBLE ASTERISK (**): Collects any number of keyword arguments into a dict
# In subplot_mosaic: **fig_kw captures extra keyword arguments for Figure()
# These might include: figsize, dpi, facecolor, etc.
# Example: subplot_mosaic(..., figsize=(10,6), dpi=100)

# COMMON MISCONCEPTION:
# Students often confuse (*) with (*args) - they're different!
# (*) forces keyword-only args. (*args) captures positional args as a tuple.

# ============================================================================
# DEMONSTRATION: subplot_mosaic with single and double asterisks
# ============================================================================

# Create a mosaic layout using string specification (most readable)
# Each character represents a subplot label, lines separated by newline
mosaic = [["A", "B"], ["C", "C"]]

# This call uses:
# - Single asterisk: All these must be keyword arguments
# - Double asterisk: figsize and dpi are captured as **fig_kw 

fig, axes = plt.subplot_mosaic( 
    mosaic,  
    # Keyword-only arguments (after the * in definition)
    sharex=False,
    sharey=False,
    # These are captured by **fig_kw
    figsize= (10, 6),
    dpi=100
)

# Plot some data
axes['A'].plot([1, 2, 3], [1, 4, 2], 'b-o')
axes['A'].set_title('Subplot A')

axes['B'].bar([1, 2, 3], [3, 1, 2], color='green')
axes['B'].set_title('Subplot B')

axes['C'].scatter(np.random.rand(10), np.random.rand(10), c='red')
axes['C'].set_title('Subplot C (spans width)')

plt.tight_layout()
plt.show()

print("Code executed successfully!")
print("The (*) in subplot_mosaic forces parameters like sharex to be keyword-only.")
print("The (**fig_kw) allows flexible figure customization without pre-defining all options.")
