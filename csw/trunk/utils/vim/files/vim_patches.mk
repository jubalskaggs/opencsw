# Vim Patchlist
PATCHDIRLEVEL = 2
PATCHFILES += vim_7.0.001.diff
PATCHFILES += vim_7.0.002.diff
PATCHFILES += vim_7.0.003.diff
PATCHFILES += vim_7.0.004.diff
PATCHFILES += vim_7.0.006.diff
PATCHFILES += vim_7.0.007.diff
PATCHFILES += vim_7.0.008.diff
PATCHFILES += vim_7.0.009.diff
PATCHFILES += vim_7.0.010.diff
PATCHFILES += vim_7.0.011.diff
PATCHFILES += vim_7.0.012.diff
PATCHFILES += vim_7.0.013.diff
PATCHFILES += vim_7.0.014.diff
PATCHFILES += vim_7.0.015.diff
PATCHFILES += vim_7.0.016.diff
PATCHFILES += vim_7.0.017.diff
PATCHFILES += vim_7.0.018.diff
PATCHFILES += vim_7.0.019.diff
PATCHFILES += vim_7.0.020.diff
PATCHFILES += vim_7.0.021.diff
PATCHFILES += vim_7.0.022.diff
PATCHFILES += vim_7.0.023.diff
PATCHFILES += vim_7.0.024.diff
PATCHFILES += vim_7.0.025.diff
PATCHFILES += vim_7.0.026.diff
PATCHFILES += vim_7.0.029.diff
PATCHFILES += vim_7.0.030.diff
PATCHFILES += vim_7.0.031.diff
PATCHFILES += vim_7.0.033.diff
PATCHFILES += vim_7.0.034.diff
PATCHFILES += vim_7.0.035.diff
PATCHFILES += vim_7.0.036.diff
PATCHFILES += vim_7.0.037.diff
PATCHFILES += vim_7.0.038.diff
PATCHFILES += vim_7.0.039.diff
PATCHFILES += vim_7.0.040.diff
PATCHFILES += vim_7.0.041.diff
PATCHFILES += vim_7.0.042.diff
PATCHFILES += vim_7.0.043.diff
PATCHFILES += vim_7.0.044.diff
PATCHFILES += vim_7.0.046.diff
PATCHFILES += vim_7.0.047.diff
PATCHFILES += vim_7.0.048.diff
PATCHFILES += vim_7.0.049.diff
PATCHFILES += vim_7.0.050.diff
PATCHFILES += vim_7.0.051.diff
PATCHFILES += vim_7.0.052.diff
PATCHFILES += vim_7.0.053.diff
PATCHFILES += vim_7.0.054.diff
PATCHFILES += vim_7.0.055.diff
PATCHFILES += vim_7.0.056.diff
PATCHFILES += vim_7.0.058.diff
PATCHFILES += vim_7.0.059.diff
PATCHFILES += vim_7.0.060.diff
PATCHFILES += vim_7.0.061.diff
PATCHFILES += vim_7.0.062.diff
PATCHFILES += vim_7.0.063.diff
PATCHFILES += vim_7.0.064.diff
PATCHFILES += vim_7.0.066.diff
PATCHFILES += vim_7.0.067.diff
PATCHFILES += vim_7.0.068.diff
PATCHFILES += vim_7.0.069.diff
PATCHFILES += vim_7.0.070.diff
PATCHFILES += vim_7.0.071.diff
PATCHFILES += vim_7.0.072.diff
PATCHFILES += vim_7.0.073.diff
PATCHFILES += vim_7.0.075.diff
PATCHFILES += vim_7.0.076.diff
PATCHFILES += vim_7.0.077.diff
PATCHFILES += vim_7.0.078.diff
PATCHFILES += vim_7.0.080.diff
PATCHFILES += vim_7.0.081.diff
PATCHFILES += vim_7.0.082.diff
PATCHFILES += vim_7.0.083.diff
PATCHFILES += vim_7.0.084.diff
PATCHFILES += vim_7.0.085.diff
PATCHFILES += vim_7.0.086.diff
PATCHFILES += vim_7.0.087.diff
PATCHFILES += vim_7.0.089.diff
PATCHFILES += vim_7.0.090.diff
PATCHFILES += vim_7.0.091.diff
PATCHFILES += vim_7.0.092.diff
PATCHFILES += vim_7.0.093.diff
PATCHFILES += vim_7.0.094.diff
PATCHFILES += vim_7.0.096.diff
PATCHFILES += vim_7.0.097.diff
PATCHFILES += vim_7.0.098.diff
PATCHFILES += vim_7.0.099.diff
PATCHFILES += vim_7.0.100.diff
PATCHFILES += vim_7.0.101.diff

LASTPATCH = $(word $(words $(PATCHFILES)), $(PATCHFILES))
PATCHREV = $(patsubst vim_$(DISTVERSION).%.diff,%,$(LASTPATCH))
GARVERSION = $(DISTVERSION).$(PATCHREV)

