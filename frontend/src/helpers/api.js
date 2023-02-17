import axios from "axios";

const baseUrl = "http://localhost:8000";

export const fetchDocuments = async () => {
  const config = {
    method: "get",
    url: `${baseUrl}/documents`,
    headers: {},
  };
  const response = await axios(config);
  return response.data;
};
