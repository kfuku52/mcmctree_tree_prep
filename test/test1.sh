#!/usr/bin/env bash

echo "current directory: `pwd`"

echo "test: unrooted tree 1"

python ../mcmctree_tree_prep.py \
--left_species Amborella_trichopoda \
--right_species Arabidopsis_thaliana \
--lower_bound 200 \
--upper_bound 200 \
--tree ../data/plant1.unroot.nwk \
--add_header

echo "test: point estimate 1"

python ../mcmctree_tree_prep.py \
--left_species Amborella_trichopoda \
--right_species Arabidopsis_thaliana \
--lower_bound 200 \
--upper_bound 200 \
--tree ../data/plant1.root.nwk \
--add_header

echo "test: upper and lower bound 1"

python ../mcmctree_tree_prep.py \
--left_species Oryza_sativa \
--right_species Brachypodium_distachyon \
--lower_bound 40 \
--upper_bound 54 \
--tree ../data/plant1.root.nwk \
--add_header

echo "test: pipe 1"

python ../mcmctree_tree_prep.py \
--left_species Oryza_sativa \
--right_species Brachypodium_distachyon \
--lower_bound 40 \
--upper_bound 54 \
--tree ../data/plant1.root.nwk \
| python ../mcmctree_tree_prep.py \
--left_species Populus_trichocarpa \
--right_species Arabidopsis_thaliana \
--lower_bound 100 \
--upper_bound 120 \
--tree - \
| python ../mcmctree_tree_prep.py \
--left_species Oryza_sativa \
--right_species Arabidopsis_thaliana \
--lower_bound 130 \
--tree - \
| python ../mcmctree_tree_prep.py \
--left_species Amborella_trichopoda \
--right_species Arabidopsis_thaliana \
--upper_bound 200 \
--tree - \
--add_header

echo "test: pipe 2"

python ../mcmctree_tree_prep.py \
--left_species Populus_trichocarpa \
--right_species Arabidopsis_thaliana \
--lower_bound 100 \
--upper_bound 120 \
--tree ../data/plant0.root.nwk \
| python ../mcmctree_tree_prep.py \
--left_species Aquilegia_coerulea \
--right_species Arabidopsis_thaliana \
--lower_bound 130 \
--upper_bound 130 \
--tree - \
--add_header