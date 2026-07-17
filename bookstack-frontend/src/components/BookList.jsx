import { useEffect, useState } from "react";
import api from "../api/axios";

function BookList() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.get("/books/")
      .then((res) => setBooks(res.data.results))
      .catch(() => setError("Failed to load books."))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading books...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div>
      <h2>Books</h2>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>ISBN</th>
            <th>Available Copies</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.isbn}</td>
              <td>{book.available_copies}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default BookList;