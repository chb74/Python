
# -- By liverpools@gmail.com -- # 
# -- On .... -- # 

from pytz import timezone, common_timezones
from datetime import datetime 


fmt = "%Y-%m-%d %H:%M:%S %Z%z"

Utc = datetime.now(timezone('UTC'))
Kst = datetime.now(timezone('Asia/Seoul'))

print()
print(Utc.strftime(fmt))
print(Kst.strftime(fmt))

