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
      vote_info = {
          'party': party,
          'name': name,
          'votes': {}
          }
      voters[voter_id] = vote_info

    if vote_id not in voters[voter_id]:
      voters[voter_id]['votes'][vote_id] = encode_vote(vote)


print "voter,name,party," + ",".join(vote_ids)
for voter_id, voter_info in voters.iteritems():
  row = [] 
  row.append(voter_id)
  row.append("\"" + voter_info['name'] + "\"")
  row.append(voter_info['party'])
  for vote_id in vote_ids:
    if vote_id in voter_info['votes']:
      row.append(str(voter_info['votes'][vote_id]))
    else:
      row.append("0")

  print ",".join(row)


