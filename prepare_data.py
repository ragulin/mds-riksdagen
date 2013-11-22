import csv
import sys
vote_ids = [] 
# voters
voters = {}
def encode_vote(vote):
  if vote == "Ja":
    return  1
  elif vote == "Nej":
    return -1
  else:
    return 0  

with open(sys.argv[1], 'rb') as csv_file:
  reader = csv.reader(csv_file, delimiter=',')
  for row in reader:
    vote_id = row[2]
    name = row[4]
    voter_id = row[5]
    party = row[6]
    vote = row[8]

    if vote_id not in vote_ids:
      vote_ids.append(vote_id)

    if voter_id not in voters:
      voters[voter_id] = {}

    if vote_id not in voters[voter_id]:
      voters[voter_id][vote_id] = encode_vote(vote)


print "voter," + ",".join(vote_ids)
for voter_id, voter_votes in voters.iteritems():
  row = [] 
  row.append(voter_id)
  for vote_id in vote_ids:
    if vote_id in voter_votes:
      row.append(str(voter_votes[vote_id]))
    else:
      row.append("0")

  print ",".join(row)


