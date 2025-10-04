class API {
  static BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8002/";

  static SPY_CATS = API.BASE_URL + "api/cats/";
  static SPY_CAT = (id) => API.BASE_URL + `api/cats/${id}`;
}

export default API;
