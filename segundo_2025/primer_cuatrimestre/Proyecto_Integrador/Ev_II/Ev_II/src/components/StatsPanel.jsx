import React from 'react';

const StatsPanel = ({ products }) => {
  if (!products || products.length === 0) {
    return (
      <div className="bg-white p-4 rounded-lg shadow mb-6 border border-gray-200">
        <h3 className="text-xl font-bold mb-2 text-black">Estadísticas</h3>
        <p className="text-black">No hay datos disponibles</p>
      </div>
    );
  }

  const stats = {
    count: products.length,
    mostExpensive: products.reduce((max, p) => p.price > max.price ? p : max, products[0]),
    cheapest: products.reduce((min, p) => p.price < min.price ? p : min, products[0]),
    longTitles: products.filter(p => p.title.length > 20).length,
    totalValue: products.reduce((sum, p) => sum + p.price, 0),
    avgDiscount: (products.reduce((sum, p) => sum + p.discountPercentage, 0) / products.length),
    avgRating: (products.reduce((sum, p) => sum + p.rating, 0) / products.length),
    totalStock: products.reduce((sum, p) => sum + p.stock, 0),
    highestStock: products.reduce((max, p) => p.stock > max.stock ? p : max, products[0])
  };

  const StatItem = ({ label, value }) => (
    <div className="p-3 rounded bg-gray-50 border border-gray-200">
      <h4 className="font-medium text-sm text-black">{label}</h4>
      <p className="font-bold text-lg text-black">{value}</p>
    </div>
  );

  return (
    <div className="bg-white p-4 rounded-lg shadow mb-6 border border-gray-200 transition-opacity duration-300">
      <h3 className="text-xl font-bold mb-3 text-black">Estadísticas ({products.length} productos)</h3>
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
        <StatItem label="Producto más caro" value={`${stats.mostExpensive.title.slice(0, 20)}... ($${stats.mostExpensive.price.toFixed(2)})`} />
        <StatItem label="Producto más barato" value={`${stats.cheapest.title.slice(0, 20)}... ($${stats.cheapest.price.toFixed(2)})`} />
        <StatItem label="Valor total" value={`$${stats.totalValue.toFixed(2)}`} />
        <StatItem label="Stock total" value={stats.totalStock} />
        <StatItem label="Rating promedio" value={`${stats.avgRating.toFixed(2)}/5`} />
        <StatItem label="Descuento promedio" value={`${stats.avgDiscount.toFixed(2)}%`} />
        <StatItem label="Títulos largos" value={stats.longTitles} />
        <StatItem label="Mayor stock" value={`${stats.highestStock.title.slice(0, 15)}... (${stats.highestStock.stock}u)`} />
      </div>
    </div>
  );
};

export default StatsPanel;