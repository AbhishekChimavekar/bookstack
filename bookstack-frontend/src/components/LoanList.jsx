import { useEffect, useState } from "react";
import api from "../api/axios";

function LoanList() {
  const [loans, setLoans] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.get("/loans/")
      .then((res) => setLoans(res.data.results))
      .catch(() => setError("Failed to load loans."))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading loans...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div>
      <h2>Loans</h2>
      <table>
        <thead>
          <tr>
            <th>Book</th>
            <th>Borrower</th>
            <th>Email</th>
            <th>Start Date</th>
            <th>Due Date</th>
            <th>Returned</th>
          </tr>
        </thead>
        <tbody>
          {loans.map((loan) => (
            <tr key={loan.id}>
              <td>{loan.book}</td>
              <td>{loan.borrower_name}</td>
              <td>{loan.borrower_email}</td>
              <td>{loan.start_date}</td>
              <td>{loan.due_date}</td>
              <td>{loan.returned ? "Yes" : "No"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default LoanList;