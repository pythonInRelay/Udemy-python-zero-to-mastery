class CamelCaseName():
    this_is_called_a_class_attribute = 'here is a string value'  # this is static

    def __init__(self, parameter1, parameter2):  # these are dynamic
        self.parameter1 = something
        self.parameter2 = something_else

    def a_method_available_to_this_class(self):
        # code here

    @classmethod  # uses the class, doesn't require instanciation
    def here_we_use_cls_not_self(cls, parameter3, parameter4):
        return some_value

    @staticmethod
    def we_dont_get_to_use_cls_here(parameter5, parameter6):
        # code here
