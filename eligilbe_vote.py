# Check whether a person is eligible to vote.
def is_eligible_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
    
print(is_eligible_to_vote(20))