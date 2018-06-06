'''
class P_main:
    def main_method(self, lol):
        return self.lol_method(lambda param: param + 96, lol)

    def lol_method(self, add, args):
        return add(args)

    class Pro:
        #__class__ = 'P'

        def __init__(self, lol):
            self.name = lol

        def __str__(self):

            return self.name

        def function(self):

            print("lol")


    Pro_obj = Pro('Prosenjit')




obj = P_main()
obj_2 = obj.Pro_obj

print(obj_2, obj_2.function())
hey = obj.main_method(5)
print(hey)
'''

from sales.forms import SalePaymentForm
from django.forms import formset_factory


payment_form_set = formset_factory(SalePaymentForm)
formset = payment_form_set()
if
for form in formset:
    print(form.as_table())













