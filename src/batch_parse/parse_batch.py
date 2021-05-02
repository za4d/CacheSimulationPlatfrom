import lark
import numpy
import numpy as np

from lark import Transformer, Token, v_args

@v_args(inline=True)
class ReadBatch(Transformer):

    def STRING(self, s):
        return str(s)

    def ESCAPED_STRING(self, s):
        return s[1:-1]

    def NUMBER(self, n):
        return float(n)

    def range(self, start, stop, step):
        return np.arange(float(start), float(stop), float(step))
        # print(np.arange(float(start), float(stop), float(step)))
        # print(np.arange(start, stop, step))

    def object_instance(self, obj_name, *kwargs_list):
        kwargs = dict(kwargs_list)
        return (str(obj_name), kwargs)

    def KWARG(self, s):
        return str(s)

    def object_definition(self, hyperparam, *instances):
        return  (str(hyperparam).upper(), list(instances))

    def literal_definition(self, hyperparam, value):
        return  (str(hyperparam).upper(), value)

    def definitions(self, *data):
        # (defs,) = data
        # return defs
        return dict(data)

    @v_args(inline=True)
    def kw_val(self, kw, val):
        return (kw, val)

    # def object_instance(self, data):
    #     # kwargs = dict(kwargs_list) if kwargs_list else dict()
    #     a = data
    #     return data

    # def val_num(self, data):
    #     return float(data)

    # def val_str(self, data):
    #     return str(data)

    # def val(self, data):
    #     tok = data[0]
    #     if type(tok) == Token:
    #         if tok.type=='NUMBER':
    #             return float(tok.value)
    #         elif tok.type=='ESCAPED_STRING':
    #             # TODO remove ["]s
    #             return str(tok.value)
    #     elif type(tok)==numpy.ndarray:
    #         return tok
    #     else:
    #         # TODO correct Error
    #         raise ValueError


    # def object_instance(self, data):
    #     a = data
    #     return data


class BatchJob:
    
    def __init__(self, args):
        arg_lists = {'NUM ITERATIONS': None, 'NUM REQUESTS': None, 'CACHE SIZE': None, 'LIBRARY SIZE': None, 'CACHING ALGORITHM': None, 'PERFORMANCE METRIC': None, 'REQUEST MODAL': None, 'COST MODAL': None}

    def compile(self,):
        'NUM ITERATIONS'
        'NUM REQUESTS'
        'CACHE SIZE'
        'LIBRARY SIZE'
        'CACHING ALGORITHM'
        'PERFORMANCE METRIC'
        'REQUEST MODAL'
        'COST MODAL'
        