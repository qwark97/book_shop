from django.conf import settings
from django.test import TestCase
from ebook_app_controller.ebook import EBookController, EBook


# Create your tests here.
def run():
    ctrl = EBookController()

    ebook_id = ctrl.create(
        'test1', 21.37
    )
    print(EBook.objects.all())

    ebook = ctrl.read(ebook_id)

    print(str(ebook))

    ctrl.update(ebook, available=True)

    print(str(ebook))

    ctrl.delete(ebook)

    print(EBook.objects.all())


if __name__ == '__main__':
    run()
