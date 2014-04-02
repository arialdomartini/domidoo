from collections import OrderedDict

class DictSerializable(object):
    def to_json(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result
