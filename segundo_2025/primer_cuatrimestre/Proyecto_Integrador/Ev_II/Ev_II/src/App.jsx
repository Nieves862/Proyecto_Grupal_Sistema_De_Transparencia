import { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import ProductList from './components/ProductList';
import StatsPanel from './components/StatsPanel';
import ProductFilters from './components/ProductFilters';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    searchQuery: '',
    minPrice: '',
    maxPrice: '',
    category: '',
    minRating: '0'
  });

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const { data } = await axios.get('https://dummyjson.com/products');
        setProducts(data.products);
      } catch (error) {
        console.error('Error fetching products:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  const filteredProducts = useMemo(() => {
    return products.filter(product => {
      const matchesSearch = filters.searchQuery === '' || 
        product.title.toLowerCase().includes(filters.searchQuery.toLowerCase());
      const matchesPrice = (filters.minPrice === '' || product.price >= Number(filters.minPrice)) &&
        (filters.maxPrice === '' || product.price <= Number(filters.maxPrice));
      const matchesCategory = filters.category === '' || product.category === filters.category;
      const matchesRating = filters.minRating === '0' || product.rating >= Number(filters.minRating);

      return matchesSearch && matchesPrice && matchesCategory && matchesRating;
    });
  }, [products, filters]);

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-8">
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold text-black">Tienda de Productos</h1>
        <p className="text-gray-600 mt-2">Filtra y analiza nuestros productos</p>
      </header>

      <ProductFilters filters={filters} setFilters={setFilters} />
      <StatsPanel products={filteredProducts} />
      <ProductList products={filteredProducts} loading={loading} />

      <footer className="mt-12 text-center text-sm text-gray-600">
        <p>© {new Date().getFullYear()} Tienda de Productos - Datos de DummyJSON</p>
      </footer>
    </div>
  );
}

export default App;