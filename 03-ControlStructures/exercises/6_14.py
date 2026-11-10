# A program that checks whether a person is a good influencer
# (has at least two accounts: Facebook, Twitter or Instagram).

facebook = True
twitter = False
instagram = True

print(f'facebook = {facebook}')
print(f'twitter = {twitter}')
print(f'instagram = {instagram}')

# at least two accounts means at least one pair of accounts
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print('You are a good influencer!')
else:
    print('You are not a good influencer.')
