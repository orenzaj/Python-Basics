# Finally, make a variable named sorted_challenges that is all of the Challenge records, ordered by the steps attribute on the model. The order should be ascending, which is the default direction.

from models import Challenge


all_challenges = Challenge.select()
Challenge.create(language = "Ruby", name = "Booleans")
sorted_challenges = Challenge.select().order_by(Challenge.steps)

print(sorted_challenges)
