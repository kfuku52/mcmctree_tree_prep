import sys, argparse
from ete3 import Tree

parser = argparse.ArgumentParser(description='This script assists to prepare a newick tree for mcmctree in the PAML package. Use pipe to introduce multiple bounds sequentially.')
parser.add_argument('--left_species', metavar='STR', default=None, type=str, help='default=%(default): Any species in the left clade. If you want to set a bound on the node splitting Homo_sapiens and Mus_musculus, specify one of them (e.g., Homo_sapiens).')
parser.add_argument('--right_species', metavar='STR', default=None, type=str,
                    help='default=%(default): Any species in the right clade deriving from the common ancestor. If '
                         'you want to set a bound on the node splitting Homo_sapiens and Mus_musculus, specify the '
                         'other one that is not used as the left species (e.g., Mus_musculus).')
parser.add_argument('--lower_bound', metavar='FLOAT', default=None, type=str, help='default=%(default): Lower bound of the calibration point.')
parser.add_argument('--lower_offset', metavar='FLOAT', default='0.1', type=str, help='default=%(default): ')
parser.add_argument('--lower_scale', metavar='FLOAT', default='1', type=str, help='default=%(default): ')
parser.add_argument('--lower_tailProb', metavar='FLOAT', default='0.025', type=str, help='default=%(default): Lower tail probability. Use 1e-300 for hard bound. Default=0.025')
parser.add_argument('--upper_bound', metavar='FLOAT', default=None, type=str,
                    help='default=%(default): Upper bound of the calibration point. A point estimate can be specified by setting the same age in both lower and upper bounds (e.g., --lower_bound 5.2 --upper_bound 5.2)')
parser.add_argument('--upper_tailProb', metavar='FLOAT', default='0.025', type=str, help='default=%(default): Upper tail probability. Use 1e-300 for hard bound. Default=0.025')
parser.add_argument('--tree', metavar='PATH', default=None, type=str,
                    help='default=%(default): newick tree file path. "-" for standard input.')
parser.add_argument('--add_header', metavar='BOOL', default=0, type=bool,
                    help='default=%(default): Add the header required for mcmctree when set to 1.')
args = parser.parse_args()
g = dict()
for attr in [a for a in dir(args) if not a.startswith('_')]:
    g[attr] = getattr(args, attr)
args = g

if args['tree'] == '-':
    tree = Tree(sys.stdin.read(), format=1, quoted_node_names=True)
else:
    tree = Tree(args['tree'], format=1, quoted_node_names=True)

assert (len(list(tree.get_children()))==2), 'The input tree is not rooted.'

for node in tree.traverse():
    if not node.is_leaf():
        if any([kw in node.name for kw in ['@', 'B(', 'L(', 'U(']]):
            node.name = '\'' + node.name + '\''
        else:
            node.name = ''

common_anc = tree.get_common_ancestor(args['left_species'], args['right_species'])

if (args['lower_bound'] == args['upper_bound']):
    constraint = '@' + args['lower_bound']
elif (args['lower_bound'] is not None) & (args['upper_bound'] is not None):
    constraint = 'B(' + ', '.join(
        [args['lower_bound'], args['upper_bound'], args['lower_tailProb'], args['upper_tailProb']]) + ')'
elif (args['lower_bound'] is not None):
    constraint = 'L(' + ', '.join(
        [args['lower_bound'], args['lower_offset'], args['lower_scale'], args['lower_tailProb']]) + ')'
elif (args['upper_bound'] is not None):
    constraint = 'U(' + ', '.join([args['upper_bound'], args['upper_tailProb']]) + ')'

constraint = '\'' + constraint + '\''
common_anc.name = constraint

nwk_text = tree.write(format=8, format_root_node=True, quoted_node_names=True)
nwk_text = nwk_text.replace('NoName', '')
nwk_text = nwk_text.replace('\"', '')
if args['add_header']:
    num_leaf = len(list(tree.get_leaf_names()))
    print(num_leaf, '1')
print(nwk_text)
