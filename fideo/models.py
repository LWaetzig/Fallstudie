from django.db import models


class Share(models.Model):

    share_id = models.CharField(("share_ID"), primary_key=True, max_length=255)
    share_tag = models.CharField(("share_tag"), max_length=255)
    share_name = models.CharField(("share_name"), max_length=255)
    share_sector = models.CharField(("share_sector"), max_length=255)
    share_volatility = models.FloatField(("volatility") , default=0.00)
    share_peg_ratio = models.FloatField(("peg_ratio"), default=0.00)
    share_beta_factor = models.FloatField(("beta_factor"), default=0.00)
    share_historical = models.CharField(("historical"), max_length=255)
    share_compound = models.FloatField(("compound"), default=0.00)
    share_market_cap = models.FloatField(("market_cap") , default=0.00)
    share_volume = models.FloatField(("volume") , default=0.00)
    last_share_price = models.FloatField(("last_close_price"), default=0.00)
    risk_level = models.FloatField(("risk_level") , default=0)


class User(models.Model):
    risk_level = models.IntegerField(("risk_level"), default=0)