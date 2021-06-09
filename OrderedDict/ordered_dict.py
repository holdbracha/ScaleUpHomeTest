class OrderedDict():

    def __init__(self):
        self._order_keys = []
        self._dict = {}

    def insert(self, key, value):
        if not self._dict.get(key):
            self._order_keys.append(key)

        self._dict[key] = value

    def clear(self):
        self._order_keys = []
        self._dict.clear()
    
    def get(self, *args, **kwargs):
        if len(args):
            key = args[0]
            default = args[1] if len(args) > 1 else None

        else:
            key = kwargs.get('key')
            default = kwargs.get('default')

        return self._dict.get(key, default)
    
    def keys(self):
        return self._order_keys
    
    def pop(self, k, d=None):
        val = self._dict.get(k)
        if val is not None:
            self._dict.pop(k)
            self._order_keys.remove(k)
            return val

        if d is not None:
            return d

        raise KeyError("Key {} is not found and default return value was not given".format(k))

    def popfirstitem(self):
        if not len(self._order_keys):
            raise KeyError("Dictionary is empty")

        return self._dict.pop(self._order_keys.pop(0))

    def update(self, E=None, **F):
        if E:
            if type(E) == type(dict()):
                for k in E:
                    self._dict[k] = E[k]

            else:
                for k, v in E:
                    self._dict[k] = v
        
        for k in F:
            self._dict[k] = F[k]
