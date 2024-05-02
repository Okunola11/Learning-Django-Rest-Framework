const loginForm = document.getElementById("login-form") as HTMLFormElement;
const container = document.getElementById("content-container");

const baseEndpoint = "http://127.0.0.1:8000/api";

const handleSubmit = async (e: Event) => {
  e.preventDefault();

  const loginEndPoint = `${baseEndpoint}/token/`;

  if (loginForm) {
    const loginFormData = new FormData(loginForm);
    const loginObjectData = Object.fromEntries(loginFormData);

    try {
      const response = await fetch(loginEndPoint, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(loginObjectData),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      console.log(data);
      const { access, refresh } = data;
      saveAndProcessToken(access, refresh);
    } catch (err) {
      console.error(err);
    }
  }
};

if (loginForm) {
  // handle the user login
  loginForm.addEventListener("submit", handleSubmit);
}

const saveAndProcessToken = async (access: string, refresh: string) => {
  const accessToken = localStorage.getItem("access");

  if (!accessToken) {
    localStorage.setItem("access", access);
  }

  // saved accessToken to local storage and left the refresh token in state

  await verifyToken(refresh);
  getProductList();
};

const verifyToken = async (refresh: string) => {
  const savedAccessToken = localStorage.getItem("access");
  const refreshToken = refresh;

  const verifyEndpoint = `${baseEndpoint}/token/verify/`;

  let accessToken;
  accessToken = savedAccessToken;
  // verify that the saved token is still valid
  try {
    const response = await fetch(verifyEndpoint, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({ token: `${savedAccessToken}` }),
    });
    const jsonData = await response.json();

    if (!response.ok && jsonData?.code === "token_not_valid") {
      // GET another access token from refresh endpoint if token not valid
      const response = await fetch(`${baseEndpoint}/token/refresh/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({ refresh: `${refreshToken}` }),
      });

      console.log("Access expired, fetching new Access token");

      if (!response.ok) {
        console.log("Expired refresh token, please login again.");
      }

      const refresh = await response.json();
      console.log(`Refresh response is: ${response}`);

      const { access } = refresh;
      accessToken = access; // set the new access token gotten from refresh
      console.log(`new access token is: ${access}`);
      console.log(`Saved new access token is: ${accessToken}`);
    }
  } catch (err) {
    console.error(err);
  }

  if (accessToken) {
    localStorage.setItem("access", accessToken);
  }
};

const getProductList = async () => {
  const access = localStorage.getItem("access");

  const response = await fetch(`${baseEndpoint}/products`, {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${access}`,
      "Content-type": "application/json",
    },
  });

  const data = await response.json();
  console.log(typeof data);
  console.log(data);

  if (container) {
    container.innerHTML = JSON.stringify(data?.results[0]);
  }
};
