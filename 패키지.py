##모듈 여러개를 모아놓은것을 패키지라 한다.##
#import travel.thailand #뒤에는 모듈이나 패키지만 가능 (클래스나 함수는 임포트 직접 불가능!)
#trip_to = travel.thailand.ThailandPackage()
#trip_to.detail()

##import가 아니고 from은 가능하다##
#from travel.thailand import ThailandPackage
#trip_to = ThailandPackage()
#trip_to.detail()

#from travel import vietnam
#trip_to = vietnam.VietnamPackage()
#trip_to.detail()

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
