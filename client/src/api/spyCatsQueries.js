import axios from "axios";
import API from "@/api/config";

const mediumOperationsTimeout = 5000;

export function getCats() {
  return axios
    .get(API.SPY_CATS, { timeout: mediumOperationsTimeout })
    .then(({ data }) => data.cats)
    .catch((reason) => {
      console.error("Failed to get cats:", reason);
      return [];
    });
}

export function addCat(catData) {
  return axios
    .post(API.SPY_CATS, catData, { timeout: mediumOperationsTimeout })
    .then(({ data }) => data.cats)
    .catch((reason) => {
      console.error("Failed to add cat:", reason);
      return [];
    });
}

export function updateCatSalary(id, salary) {
  return axios
    .put(API.SPY_CAT(id), { salary }, { timeout: mediumOperationsTimeout })
    .then(({ data }) => data.cats)
    .catch((reason) => {
      console.error("Failed to update salary:", reason);
      return [];
    });
}

export function deleteCat(id) {
  return axios
    .delete(API.SPY_CAT(id), { timeout: mediumOperationsTimeout })
    .then(({ data }) => data.cats)
    .catch((reason) => {
      console.error("Failed to delete cat:", reason);
      return [];
    });
}
