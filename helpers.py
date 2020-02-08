from app_facade.ebook_controller import EBookController


def serialize(i, n, p, q, cov, av):
    return {
        "id": i,
        "name": n,
        "price": p,
        "quantity": q,
        "cover": cov,
        "available": av,
    }


def get_all_books():
    all_books = [serialize(
        book.id,
        book.name,
        book.price,
        book.quantity,
        book.cover,
        book.availability
    ) for book in EBookController.get_all().values()]
    return all_books
