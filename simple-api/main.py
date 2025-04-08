from fastapi import FastAPI
import random

app = FastAPI()
# we will build two simple endpoints
# side_hustles and money_quotes

side_hustles = [
   " Freelance Writing- Writing articles, blogs, copy.",
   "Dropshipping Business- Selling products without inventory.",
   "Social Media Management- Curating and scheduling posts.",
   "Affiliate Marketing- Earning commissions through referrals.",
   "Online Tutoring- Teaching subjects virtually online.",
]
money_quotes = [
    "The hustle never stops, and neither does the opportunity.",
    "Success starts with one step—take it today!",
    "Your side hustle is your future's foundation.",
    "Turn passion into profit, one day at a time.",
    "Money flows where hustle grows.",
]

@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random side hustle idea"""
    return {"money_quotes": random.choice(money_quotes)}
