import React from 'react';

const ProductFilters = ({ filters, setFilters }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({ ...prev, [name]: value }));
  };

  const categories = [
    'smartphones', 'laptops', 'fragrances',
    'skincare', 'groceries', 'home-decoration'
  ];

  return (
    <div className="bg-white p-4 rounded-lg shadow mb-6 border border-gray-200">
      <h3 className="text-xl font-bold mb-3 text-black">Filtros</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div>
          <label className="block text-sm font-medium text-black mb-1">Buscar</label>
          <input
            type="text"
            name="searchQuery"
            value={filters.searchQuery}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded text-black"
            placeholder="Nombre del producto"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-black mb-1">Precio mínimo</label>
          <input
            type="number"
            name="minPrice"
            value={filters.minPrice}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded text-black"
            placeholder="Mínimo"
            min="0"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-black mb-1">Precio máximo</label>
          <input
            type="number"
            name="maxPrice"
            value={filters.maxPrice}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded text-black"
            placeholder="Máximo"
            min="0"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-black mb-1">Categoría</label>
          <select
            name="category"
            value={filters.category}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded text-black"
          >
            <option value="">Todas</option>
            {categories.map(cat => (
              <option key={cat} value={cat}>
                {cat.charAt(0).toUpperCase() + cat.slice(1)}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
};

export default ProductFilters;