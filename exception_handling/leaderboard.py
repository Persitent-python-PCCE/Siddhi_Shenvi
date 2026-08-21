# Leaderboard ordered by rank; quota attainment keyed by rep name.
top_reps = ["A. Chen", "R. Patel", "M. Silva", "K. Osei"] # index 0 = rank 1
quota_hit = {"A. Chen": 112, "R. Patel": 98, "M. Silva": 87} # % of quota

def rep_at_rank(rank):
    """Return the sales rep at a given 1-based rank."""
    # TODO: top_reps[rank - 1] raises IndexError for an out-of-range rank.
    #       Handle it: "No rep at rank {rank}." and return None.
    try:
        return top_reps[rank- 1]
    except IndexError:
        print(f"No rep at rank {rank}")
        return None

def quota_for(rep):
   """Return the quota-attainment % for a rep."""
   # TODO: quota_hit[rep] raises KeyError if the rep has no record.
   #  #       Handle it: "No quota record for {rep}." and return None.
   try:
    return quota_hit[rep]
   except KeyError:
      print(f"No quota record for {rep}")
      return None

def safe_report(rank, rep):
    """Bonus: use ONE 'except LookupError' block to guard BOTH
    top_reps[rank - 1] and quota_hit[rep], then print both results."""
    # TODO: single try / except LookupError wrapping both lookups.
    try:
        rep_name=top_reps[rank - 1]
        quota=quota_hit[rep]

        print(rep_name)

        print(quota)
    except LookupError:
       print("Invalid rank or representative.")
        
       


print(rep_at_rank(2))
print(rep_at_rank(10))
print(quota_for("M. Silva"))
print(quota_for("J. Doe"))
