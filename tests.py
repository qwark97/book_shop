from controller import EBookController
from models import EBook

def test_run():
    ctrl = EBookController()

    ebook_id = ctrl.create(
        'test1', 21.37
    )
    print(EBook.all())

    ebook = ctrl.read(ebook_id)

    print(str(ebook))

    ctrl.update(ebook, available=True)

    print(str(ebook))

    ctrl.delete(ebook)

    print(EBook.all())


if __name__ == '__main__':
    run()