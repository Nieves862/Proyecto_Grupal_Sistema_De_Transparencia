import React from 'react';

export const ProductStats = ({ products }) => {
  
  if (!products || products.length === 0) {
    return <div className="p-4 text-gray-500">No hay productos para mostrar estadísticas</div>;
  }

  
const stats = {
    mostExpensive: products.reduce((max, p) => (p.price > max.price ? p : max), products[0]),
    cheapest: products.reduce((min, p) => (p.price < min.price ? p : min), products[0]),
    longTitles: products.filter(p => p.title.length > 20).length,
    totalPrice: products.reduce((sum, p) => sum + p.price, 0),
    avgDiscount: products.reduce((sum, p) => sum + p.discountPercentage, 0) / products.length,
    avgRating: products.reduce((sum, p) => sum + p.rating, 0) / products.length
  };

 
const StatCard = ({ title, value }) => (
    <div className="bg-gray-50 p-3 rounded border">
      <h4 className="font-semibold text-sm text-gray-600">{title}</h4>
      <p className="font-bold text-lg">{value}</p>
    </div>
  );

return (
    <div className="bg-white p-4 rounded-lg shadow mb-6">
      <h3 className="text-xl font-bold mb-3">Estadísticas</h3>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
        <StatCard 
          title="Producto más caro" 
          value={`${stats.mostExpensive.title} ($${stats.mostExpensive.price.toFixed(2)})`} 
        />
        <StatCard 
          title="Producto más barato" 
          value={`${stats.cheapest.title} ($${stats.cheapest.price.toFixed(2)})`} 
        />
        <StatCard 
          title="Títulos largos (>20 chars)" 
          value={stats.longTitles} 
        />
        <StatCard 
          title="Valor total" 
          value={`$${stats.totalPrice.toFixed(2)}`} 
        />
        <StatCard 
          title="Descuento promedio" 
          value={`${stats.avgDiscount.toFixed(2)}%`} 
        />
        <StatCard 
          title="Rating promedio" 
          value={stats.avgRating.toFixed(2)} 
        />
      </div>
    </div>
  );
};
