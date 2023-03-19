for i in range(100):
  for attempt in range(10):
    try:
      # do thing
    except:
      # perhaps reconnect, etc.
    else:
      break
  else:
    # we failed all the attempts - deal with the consequences.