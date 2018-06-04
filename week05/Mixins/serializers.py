import json


class JsonableMixin:
    primitives = (int, float, str, bool, list, dict, type(None))

    def get_serializable_dict(self):
        result_dict = {"class_name": self.__class__.__name__, "dict": {}}

        for attr_name, attr_value in self.__dict__.items():
            if type(attr_value) in self.primitives:
                result_dict["dict"][attr_name] = attr_value
            elif isinstance(attr_value, JsonableMixin):
                result_dict["dict"][attr_name] = attr_value.get_serializable_dict()
            else:
                raise ValueError('The class has non serializable attribute!')

        return result_dict

    def to_json(self, indent):
        return json.dumps(
            self.get_serializable_dict(),
            indent=indent
        )

    @classmethod
    def from_json(cls, json_string):
        dict_ = json.loads(json_string)
        kwargs = {}

        if dict_['class_name'] != cls.__name__:
            raise Exception('The serialized class is not correct!')

        for k, v in dict_['dict'].items():
            if type(v) is dict and 'class_name' in v and v['class_name'] in globals():
                kwargs[k] = getattr(globals()[v['class_name']], 'from_json')(json.dumps(v))
            else:
                kwargs[k] = v

        return cls(**kwargs)
