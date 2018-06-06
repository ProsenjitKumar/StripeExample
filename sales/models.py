from django.db import models

from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=56)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo/', blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)

        # bring in stripe, and get the api key from settings.py
        import stripe
        stripe.api_key = settings.STRIPE_API_KEY

        self.stripe = stripe

    # store the stripe charge id for this sale
    charge_id = models.CharField(max_length=32)

    # you could also store other information about the sale
    # but I'll leave that to you!

    def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
        """
        Takes a the price and credit card details: number, exp_month,
        exp_year, cvc.

        Returns a tuple: (Boolean, Class) where the boolean is if
        the charge was successful, and the class is response (or error)
        instance.
        """

        if self.charge_id:  # don't let this be charged twice!
            return False, Exception(message="Already charged.")

        try:
            response = self.stripe.Charge.create(
                amount=price_in_cents,
                currency="usd",
                card={
                    "number": number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc,

                    #### it is recommended to include the address!
                    # "address_line1" : self.address1,
                    # "address_line2" : self.address2,
                    # "daddress_zip" : self.zip_code,
                    # "address_state" : self.state,
                },
                description='Thank you for your purchase!')

            self.charge_id = response.id

        except self.stripe.CardError:
            # charge failed
            return False

        return True, response




