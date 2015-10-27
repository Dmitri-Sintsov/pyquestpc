# from pudb import set_trace

# Slightly modified version of @accepts decorator.
# https://www.python.org/dev/peps/pep-0318/ Python 2.x
"""
@accepts(int, (int,float), 'any')
@returns((int,float))
def func(arg1, arg2, arg3):
    print arg3
    return arg1 * arg2
"""


def accepts(*types):
    def check_accepts(f):
        # set_trace()
        assert len(types) == f.__code__.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                # Modified by QuestPC to allow non-strict arguments.
                if t == 'any':
                    continue
                assert isinstance(a, t), \
                    "arg %r does not match %s" % (a,t)
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check_accepts


def returns(rtype):
    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), \
                "return value %r does not match %s" % (result,rtype)
            return result
        new_f.func_name = f.func_name
        return new_f
    return check_returns
