import { Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import LoginPage from "./pages/LoginPage";
import BooksPage from "./pages/BooksPage";
import LoansPage from "./pages/LoansPage";

function ProtectedRoute({ children }) {
  const { accessToken } = useAuth();
  return accessToken ? children : <Navigate to="/login" />;
}

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/books" element={<ProtectedRoute><BooksPage /></ProtectedRoute>} />
      <Route path="/loans" element={<ProtectedRoute><LoansPage /></ProtectedRoute>} />
      <Route path="*" element={<Navigate to="/login" />} />
    </Routes>
  );
}

export default App;