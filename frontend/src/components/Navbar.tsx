import { useNavigate } from "react-router-dom";

interface NavbarProps {
  username: string;
  handleLogout: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ username, handleLogout }) => {
  const navigate = useNavigate();

  return (
    <nav className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <span
              className="text-2xl font-bold text-blue-600 cursor-pointer"
              onClick={() => navigate("/dashboard")}
            >
              Blackbird Academy
            </span>
          </div>
          <div className="flex items-center space-x-4">
            <span className="text-gray-700">Welcome, {username}!</span>
            <button
              onClick={handleLogout}
              className="bg-red-600 text-black px-4 py-2 rounded-md hover:bg-red-700 transition-colors"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
