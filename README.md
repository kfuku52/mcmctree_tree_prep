# Overview

**mcmctree_tree_prep** is a tool to prepare input tree files for **mcmctree** in the [**PAML**](http://web.mit.edu/6.891/www/lab/paml.html) package. 
This program allows to introduce fossil constraints in a command-line interface for the divergence time estimation subsequently done by **mcmctree**. 
This script has been tested with **PAML 4.9** and supports:

* Lower bound
* Upper bound
* Pair bound
* Point estimate

Parameters such as tail probability can be specified. See [PAML MANUAL](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf) for details.

# Input file
* A rooted tree in the newick format. The input tree can contain support values and branch lengths, which will be removed from the output to be compatible with **mcmctree**.

# Dependency
* [python 3.x](https://www.python.org/)
* [ete3](https://github.com/etetoolkit/ete)

# Usage
See complete options by typing `mcmctree_tree_prep.py -h` after downloading the script.

# Example
You can use pipes to add multiple constraints. **--add_header** should be specified only in the final step.
```
python mcmctree_tree_prep.py \
--left_species Populus_trichocarpa \
--right_species Arabidopsis_thaliana \
--lower_bound 100 \
--upper_bound 120 \
--tree input.nwk \
| python mcmctree_tree_prep.py \
--left_species Aquilegia_coerulea \
--right_species Arabidopsis_thaliana \
--lower_bound 130 \
--upper_bound 130 \
--tree - \
--add_header \
> output.nwk
```
#### input.nwk
```
(Aquilegia_coerulea:0.23566,((Arabidopsis_thaliana:0.366634,Populus_trichocarpa:0.167905)100:0.0447481,Vitis_vinifera:0.139353)99:0.0680463)1:0;
```

#### output.nwk
```
4 1
(Aquilegia_coerulea,((Arabidopsis_thaliana,Populus_trichocarpa)'B(100, 120, 0.025, 0.025)',Vitis_vinifera))'@130';
```

# Licensing
This program is BSD-licensed (3 clause). See [LICENSE](LICENSE) for details.

