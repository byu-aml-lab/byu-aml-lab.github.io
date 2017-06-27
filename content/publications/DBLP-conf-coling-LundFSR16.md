+++
title =  "Fast Inference for Interactive Models of Text"
authors = ["Jeffrey Lund","Paul Felt","Kevin D. Seppi","Eric K. Ringger"]
bibtex = "bib/DBLP-conf-coling-LundFSR16"
+++

Probabilistic models are a useful means for analyzing large text corpora. Integrating such models
with human interaction enables many new use cases. However, adding human interaction to
probabilistic models requires inference algorithms which are both fast and accurate. We explore
the use of Iterated Conditional Modes as a fast alternative to Gibbs sampling or variational EM.
We demonstrate superior performance both in run time and model quality on three different
models of text including a DP Mixture of Multinomials for web search result clustering, the
Interactive Topic Model, and MOMRESP, a multinomial crowdsourcing model.
