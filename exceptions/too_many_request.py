from pip._vendor.requests import ConnectTimeout


class TooManyRequests(Exception):
"""Too many requests"""

@task(
   rate_limit='10/s',
   autoretry_for=(ConnectTimeout, TooManyRequests,),
   retry_backoff=True)
def api(*args, **kwargs):
  r = requests.get('placeholder-external-api')

  if r.status_code == 429:
    raise TooManyRequests()