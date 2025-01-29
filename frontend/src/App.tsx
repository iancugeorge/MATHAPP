import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import MyComponent from "../components/signup"; // Adjust path if needed

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-100">
          <Routes>
            {/* Default route shows Signup component */}
            <Route path="/" element={<Signup />} />
          </Routes>
        </div>
      </Router>
    </QueryClientProvider>
  );
}

const Signup: React.FC = () => {
  return (
    <div>
      <MyComponent />
    </div>
  );
};

export default App;
