from app_facade.ebook_controller import EBookController


def serialize(i, n, av):
    return {"id": i, "available": av, "name": n}


def get_all_books():
    all_books = [serialize(book.id, book.name, book.availability) for book in EBookController.get_all().values()]
    return all_books
