import axios from "axios";
import API from "@/api/config";

export async function getCats() {
  const { data } = await axios.get(API.SPY_CATS);
  return data.cats;
}

export async function addCat(catData) {
  const { data } = await axios.post(API.SPY_CATS, catData);
  return data.cats;
}

export async function updateCatSalary(id, salary) {
  const { data } = await axios.put(API.SPY_CAT(id), { salary });
  return data.cats;
}

export async function deleteCat(id) {
  const { data } = await axios.delete(API.SPY_CAT(id));
  return data.cats;
}
