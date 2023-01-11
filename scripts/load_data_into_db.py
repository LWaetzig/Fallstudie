from fideo.models import Share
import csv


def run():
    with open("fideo/data/sharesdata.csv") as f:
        reader = csv.reader(f)
        next(reader)

        Share.objects.all().delete()

        for row in reader:
            print(row)

            share = Share(
                share_id=row[0],
                share_tag=row[1],
                share_name=row[2],
                share_sector=row[3],
                share_peg_ratio=row[4],
                share_beta_factor=row[5],
                share_historical=row[6],
                share_volatility=row[7],
                share_market_cap=row[8],
                share_volume=row[9],
                last_share_price=row[10],
                share_compound=row[11],
                risk_level=row[12]

            )

            share.save()
