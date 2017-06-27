+++
title = "DBLP-conf-sc-LundAMS16"
+++

@inproceedings{DBLP:conf/sc/LundAMS16,
   booktitle={6th Workshop on Python for High-Performance and Scientific Computing, PyHPC@SC 2016, Salt Lake, UT, USA, November 14, 2016},
   crossref={DBLP:conf/sc/2016pyhpc},
   link={https://doi.org/10.1109/PyHPC.2016.014},
   timestamp={Tue, 23 May 2017 01:07:25 +0200},
   author={Jeffrey Lund and
Chace Ashcraft and
Andrew W. McNabb and
Kevin D. Seppi},
   biburl={http://dblp.uni-trier.de/rec/bib/conf/sc/LundAMS16},
   pages={76--85},
   abstract={Mrs is a lightweight Python-based MapReduce implementation designed to make MapReduce programs easy to write and quick to run, particularly useful for research and academia. A common set of algorithms that would benefit from Mrs are iterative algorithms, like those frequently found in machine learning; however, iterative algorithms typically perform poorly in the MapReduce framework, meaning potentially poor performance in Mrs as well. Therefore, we propose four modifications to the original Mrs with the intent to improve its ability to perform iterative algorithms. First, we used direct task-to-task communication for most iterations and only occasionally write to a distributed file system to preserve fault tolerance. Second, we combine the reduce and map tasks which span successive iterations to eliminate unnecessary communication and scheduling latency. Third, we propose a generator-callback programming model to allow for greater flexibility in the scheduling of tasks. Finally, some iterative algorithms are naturally expressed in terms of asynchronous message passing, so we propose a fully asynchronous variant of MapReduce. We then demonstrate Mrs' enhanced performance in the context of two iterative applications: particle swarm optimization (PSO), and expectation maximization (EM).},
   doi={10.1109/PyHPC.2016.014},
   bibsource={dblp computer science bibliography, http://dblp.org},
   year={2016},
   title={Mrs: High Performance MapReduce for Iterative and Asynchronous Algorithms
in Python},
}
