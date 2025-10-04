"use client";
import { useEffect, useState } from "react";
import { getCats, addCat, updateCatSalary, deleteCat } from "@/api/spyCatsQueries";

export default function SpyCatsPage() {
  const [cats, setCats] = useState([]);
  const [form, setForm] = useState({ name: "", years_of_experience: "", breed: "", salary: "" });
  const [error, setError] = useState("");

  const loadCats = async () => {
    try {
      const catsList = await getCats();
      setCats(catsList);
    } catch (err) {
      setError("Failed to load spy cats");
    }
  };

  useEffect(() => {
    loadCats();
  }, []);

  const handleAddCat = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const updatedCats = await addCat(form);
      setCats(updatedCats);
      setForm({ name: "", years_of_experience: "", breed: "", salary: "" });
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to add cat");
    }
  };

  const handleUpdateSalary = async (id, value) => {
    const salary = Number(value);
      if (isNaN(salary) || salary < 0) return;

    try {
      await updateCatSalary(id, salary);
      setCats(updatedCats);
      setError("");
    } catch {
      setError("Failed to update salary");
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteCat(id);
      loadCats();
    } catch {
      setError("Failed to delete cat");
    }
  };

  return (
    <div className="max-w-3xl mx-auto py-10">
      <h1 className="text-2xl font-bold mb-6 text-center">🐾 Spy Cats Management</h1>
      {error && <p className="text-red-500 mb-4 text-center">{error}</p>}

      <form onSubmit={handleAddCat} className="flex flex-col gap-2 border p-4 rounded-md mb-8 bg-gray-50">
        <h2 className="text-lg font-semibold">Add New Spy Cat</h2>
        <input
            type="text"
            placeholder="Name"
            value={form.name}
            onChange={(e) => setForm({...form, name: e.target.value})}
            className="border p-2 rounded"
            required
        />
        <input
            type="number"
            placeholder="Years of Experience"
            value={form.years_of_experience}
            onChange={(e) => {
              const value = e.target.value;
              if (value === "" || value === ".") {
                setForm({...form, years_of_experience: value});
                return;
              }

              const num = parseFloat(value);
              if (!isNaN(num) && num >= 0) {
                setForm({...form, years_of_experience: num});
              }
            }}
            step="0.1"
            min="0"
            className="border p-2 rounded"
            required
        />
        <input
            type="text"
            placeholder="Breed"
            value={form.breed}
            onChange={(e) => setForm({...form, breed: e.target.value})}
            className="border p-2 rounded"
            required
        />
        <input
            type="number"
            placeholder="Salary"
            value={form.salary}
            onChange={(e) => {
              const value = e.target.value;
              if (value === "" || value === ".") {
                setForm({...form, salary: value});
                return;
              }

              const num = parseFloat(value);
              if (!isNaN(num) && num >= 0) {
                setForm({...form, salary: num});
              }
            }}
            step="0.1"
            min="0"
            className="border p-2 rounded"
            required
        />
        <button type="submit" className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
          Add Spy Cat
        </button>
      </form>

      <h2 className="text-lg font-semibold mb-2">Existing Spy Cats</h2>
      <div className="space-y-3">
        {cats.map((cat) => (
          <div key={cat.cat_id} className="flex justify-between items-center border p-3 rounded bg-white shadow-sm">
            <div>
              <p className="font-semibold">{cat.name}</p>
              <p className="text-sm text-gray-600">
                {cat.breed ?? "Unknown"} • {cat.years_of_experience ?? 0} yrs exp
              </p>
              <p className="text-sm">💰 Salary: {cat.salary ?? 0}</p>
            </div>

            <div className="flex gap-2">
              <input
                type="number"
                step="0.01"
                defaultValue={Number(cat.salary) || 0}
                placeholder="Salary"
                className="border p-1 rounded w-24"
                id={`salary-${cat.cat_id}`} // унікальний id, щоб можна було знайти input
              />

              <button
                onClick={() => {
                  const input = document.getElementById(`salary-${cat.cat_id}`);
                  const value = parseFloat(input.value);
                  if (!isNaN(value) && value >= 0) {
                    handleUpdateSalary(cat.cat_id, value);
                  }
                }}
                className="bg-green-500 text-white px-2 py-1 rounded hover:bg-green-600"
              >
                Update
              </button>

              <button
                onClick={() => handleDelete(cat.cat_id)}
                className="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
        {cats.length === 0 && <p className="text-gray-500">No spy cats yet.</p>}
      </div>
    </div>
  );
}
