from app_facade.ebook_controller import EBookController
from models.ebook import EBook


def test_run():

    created_ebook = EBookController.create(
        'test1', 21.37
    )
    print(EBook.get_all())

    ebook = EBookController.read(created_ebook._id)

    print(str(ebook))

    EBookController.update(ebook, available=True)

    print(str(ebook))

    EBookController.delete(ebook)

    print(EBook.get_all())

    return "Everything works fine!"


if __name__ == '__main__':
    test_run()
