from lark import Lark, tree
from parse_batch import ReadBatch
import sys

def make_dot(parser, filename):
    tree.pydot__tree_to_dot(parser.parse(ex), filename)

def make_png(parser, filename):
    tree.pydot__tree_to_png( parser.parse(ex), filename)

example_file = 'example.csp'

if __name__ == '__main__':
    with open('batch_grammer.lark', 'r') as grammer_f:
        with open(example_file, 'r') as example_f:
            grammer = grammer_f.read()
            ex = example_f.read()
            parser = Lark(grammer, start='definitions', ambiguity='explicit')
            t = parser.parse(ex)
            print(t.pretty())
            make_png(parser,'test.png')
            print('#'*10)
            parsed = ReadBatch().transform(t)
            print(parsed)



    # make_png(sys.argv[1])

    # ([('NUM ITERATIONS', 3.0), ('NUM REQUESTS', 1000.0), ('CACHE SIZE', 100.0), ('LIBRARY SIZE', 1000.0), ('CACHING ALGORITHM', (('min', {}),)), ('PERFORMANCE METRIC', (('gain', {'hit_weight': 2.0, 'miss_weight': 3.0}),)), ('REQUEST MODAL', (('gaussian', {'mean': 500.0, 'std': 15.0, 'test_string': Token('ESCAPED_STRING', '"hello"')}), ('zipfian', {'eta': array([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])}))), ('COST MODAL', (('static_uniform_cost', {'cost': 99.0}),))],)

