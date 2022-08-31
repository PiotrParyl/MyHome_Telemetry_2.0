import test2
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=test2.engine)
session = Session()


def test(namee,int,int2):

    new_data = test2.test_class(namee,int,int2)
    session.add(new_data)
    session.commit()




test('chuj',420,69)