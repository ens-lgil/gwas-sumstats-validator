print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import validate.validator
import tests.test_validator

validate.validator.main()