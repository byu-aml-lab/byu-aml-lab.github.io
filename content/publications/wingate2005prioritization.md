+++
title =  "Prioritization methods for accelerating MDP solvers"
authors = ["David Wingate","Kevin D Seppi"]
bibtex = "bib/wingate2005prioritization"
+++

The performance of value and policy iteration can be dramatically improved by eliminating redundant
or useless backups, and by backing up states in the right order. We study several methods
designed to accelerate these iterative solvers, including prioritization, partitioning, and variable
reordering. We generate a family of algorithms by combining several of the methods discussed, and present extensive empirical evidence demonstrating that performance can improve by several
orders of magnitude for many problems, while preserving accuracy and convergence guarantees.
