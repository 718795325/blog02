from datetime import time
import time
from django.utils import timezone
from django.utils.timezone import now


print(timezone.now,type(timezone))
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))