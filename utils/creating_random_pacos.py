
import names
from pacos.models import Paco

Paco.objects.all().delete()

for i in range(500):
    a = Paco(first_name=names.get_first_name(),
             last_name=names.get_last_name(),
             )
    a.save()



