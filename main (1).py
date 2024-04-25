flag = False
def guess_password():
  print("\033\143")
  global flag
  guess = input('A password is needed to access this network:')
  if guess != 'TheKey':
    print('That is incorrect.')
    print()
    input('Press Enter to continue')
    guess_password()
  else:
    flag = True
guess_password()
print('That is correct you now have access!')