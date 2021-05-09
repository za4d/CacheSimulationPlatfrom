import numpy
import numpy as np
from lark import Transformer, Token, v_args
from itertools import product

@v_args(inline=True)
class ReadBatch(Transformer):

    def STRING(self, s):
        return str(s)

    def ESCAPED_STRING(self, s):
        return s[1:-1]

    def NUMBER(self, n):
        return float(n)

    def range(self, start, stop, step):
        return list(np.arange(float(start), float(stop), float(step)))
        # print(np.arange(float(start), float(stop), float(step)))
        # print(np.arange(start, stop, step))

    def object_instance(self, obj_name, *kwargs_list):
        kwargs = dict(kwargs_list)
        # self._expand_kw_list(kwargs_list)
        return (str(obj_name), kwargs)

    def KWARG(self, s):
        return str(s)

    def object_definition(self, hyperparam, *instances):
        return  (str(hyperparam).upper(), list(instances))

    def simple_definition(self, hyperparam, value):
        name = str(hyperparam).upper()
        value = value if type(value)==list else [value]
        return (name, value)

    def definitions(self, *data):
        # convert [(name, [value,...])] -> [[(name,value), (name,value), ...]]
        # i.e. convert into list of lists for each parameter
        params_list = list()
        for name, vals in data:
            params_list.append([(name, v) for v in vals])
        # print('!')
        # find the cross product for each list of lists to get list of each instance parameters to be simulated
        return [dict(inst_param) for inst_param in product(*params_list)]


    @v_args(inline=True)
    def kw_value(self, kw, val):
        return (kw, val)

    def _expand_kw_list(self, *data):
        # convert [(name, [value,...])] -> [[(name,value), (name,value), ...]]
        # i.e. convert into list of lists for each parameter
        if not data:
            return None
        params_list = list()
        for name, vals in data:
            params_list.append([(name, v) for v in vals])
        # print('!')
        # find the cross product for each list of lists to get list of each instance parameters to be simulated
        return [dict(inst_param) for inst_param in product(*params_list)]

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
        