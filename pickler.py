import ast
import os
import os.path
import pickle
import hashlib
import inspect
import __main__
from IPython.core.magic import Magics, magics_class, line_cell_magic

FOLDER = 'pickler_dumps'

class AssignmentFinder(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        ast.NodeVisitor.__init__(self, *args, **kwargs)
        self.variables = set()
    
    def visit_Assign(self, node):
        self.variables |= {target.id for target in node.targets}
        ast.NodeVisitor.generic_visit(self, node)


@magics_class
class PicklerMagic(Magics):
    @line_cell_magic
    def dumpit(self, line, cell=None):
        code = line if (cell is None) else cell
        
        hasher = hashlib.md5()
        hasher.update(bytes(code, 'utf-8'))
        filename = hasher.hexdigest() + '.dump'
        path = os.path.join(FOLDER, filename)
        
        visitor = AssignmentFinder()
        visitor.visit(ast.parse(code))
        variables = visitor.variables
        
        try:
            with open(path, 'rb') as dump:
                data, result = pickle.load(dump)
                for variable, value in zip(variables, data):
                    setattr(__main__, variable, value)
                return result
        except FileNotFoundError:
            namespace = {}
            result = exec(code, globals().get(__main__, None), namespace)
            for key, val in namespace.items():
                setattr(__main__, key, val)
            data = tuple(namespace[variable] for variable in variables)
            os.makedirs(FOLDER, exist_ok=True)
            with open(path, 'wb') as dump:
                pickle.dump((data, result), dump)
            return result

ip = get_ipython()
ip.register_magics(PicklerMagic)

