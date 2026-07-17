import { createContext, useContext, useState } from "react";
import api from "../api/axios";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState(localStorage.getItem("access") || null);

  async function login(username, password) {
    const response = await api.post("/token/", { username, password });
    const { access, refresh } = response.data;
    localStorage.setItem("access", access);
    localStorage.setItem("refresh", refresh);
    setAccessToken(access);
  }

  function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    setAccessToken(null);
  }

  return (
    <AuthContext.Provider value={{ accessToken, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}