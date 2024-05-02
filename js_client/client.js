var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
var loginForm = document.getElementById("login-form");
var container = document.getElementById("content-container");
var baseEndpoint = "http://127.0.0.1:8000/api";
var handleSubmit = function (e) { return __awaiter(_this, void 0, void 0, function () {
    var loginEndPoint, loginFormData, loginObjectData, response, data, access, refresh, err_1;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                e.preventDefault();
                loginEndPoint = "".concat(baseEndpoint, "/token/");
                if (!loginForm) return [3 /*break*/, 5];
                loginFormData = new FormData(loginForm);
                loginObjectData = Object.fromEntries(loginFormData);
                _a.label = 1;
            case 1:
                _a.trys.push([1, 4, , 5]);
                return [4 /*yield*/, fetch(loginEndPoint, {
                        method: "POST",
                        headers: {
                            "Content-type": "application/json",
                        },
                        body: JSON.stringify(loginObjectData),
                    })];
            case 2:
                response = _a.sent();
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return [4 /*yield*/, response.json()];
            case 3:
                data = _a.sent();
                console.log(data);
                access = data.access, refresh = data.refresh;
                saveAndProcessToken(access, refresh);
                return [3 /*break*/, 5];
            case 4:
                err_1 = _a.sent();
                console.error(err_1);
                return [3 /*break*/, 5];
            case 5: return [2 /*return*/];
        }
    });
}); };
if (loginForm) {
    // handle the user login
    loginForm.addEventListener("submit", handleSubmit);
}
var saveAndProcessToken = function (access, refresh) { return __awaiter(_this, void 0, void 0, function () {
    var accessToken;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                accessToken = localStorage.getItem("access");
                if (!accessToken) {
                    localStorage.setItem("access", access);
                }
                // saved accessToken to local storage and left the refresh token in state
                return [4 /*yield*/, verifyToken(refresh)];
            case 1:
                // saved accessToken to local storage and left the refresh token in state
                _a.sent();
                getProductList();
                return [2 /*return*/];
        }
    });
}); };
var verifyToken = function (refresh) { return __awaiter(_this, void 0, void 0, function () {
    var savedAccessToken, refreshToken, verifyEndpoint, accessToken, response, jsonData, response_1, refresh_1, access, err_2;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                savedAccessToken = localStorage.getItem("access");
                refreshToken = refresh;
                verifyEndpoint = "".concat(baseEndpoint, "/token/verify/");
                accessToken = savedAccessToken;
                _a.label = 1;
            case 1:
                _a.trys.push([1, 7, , 8]);
                return [4 /*yield*/, fetch(verifyEndpoint, {
                        method: "POST",
                        headers: {
                            "content-type": "application/json",
                        },
                        body: JSON.stringify({ token: "".concat(savedAccessToken) }),
                    })];
            case 2:
                response = _a.sent();
                return [4 /*yield*/, response.json()];
            case 3:
                jsonData = _a.sent();
                if (!(!response.ok && (jsonData === null || jsonData === void 0 ? void 0 : jsonData.code) === "token_not_valid")) return [3 /*break*/, 6];
                return [4 /*yield*/, fetch("".concat(baseEndpoint, "/token/refresh/"), {
                        method: "POST",
                        headers: {
                            "content-type": "application/json",
                        },
                        body: JSON.stringify({ refresh: "".concat(refreshToken) }),
                    })];
            case 4:
                response_1 = _a.sent();
                console.log("Access expired, fetching new Access token");
                if (!response_1.ok) {
                    console.log("Expired refresh token, please login again.");
                }
                return [4 /*yield*/, response_1.json()];
            case 5:
                refresh_1 = _a.sent();
                console.log("Refresh response is: ".concat(response_1));
                access = refresh_1.access;
                accessToken = access; // set the new access token gotten from refresh
                console.log("new access token is: ".concat(access));
                console.log("Saved new access token is: ".concat(accessToken));
                _a.label = 6;
            case 6: return [3 /*break*/, 8];
            case 7:
                err_2 = _a.sent();
                console.error(err_2);
                return [3 /*break*/, 8];
            case 8:
                if (accessToken) {
                    localStorage.setItem("access", accessToken);
                }
                return [2 /*return*/];
        }
    });
}); };
var getProductList = function () { return __awaiter(_this, void 0, void 0, function () {
    var access, response, data;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                access = localStorage.getItem("access");
                return [4 /*yield*/, fetch("".concat(baseEndpoint, "/products"), {
                        method: "GET",
                        headers: {
                            "Authorization": "Bearer ".concat(access),
                            "Content-type": "application/json",
                        },
                    })];
            case 1:
                response = _a.sent();
                return [4 /*yield*/, response.json()];
            case 2:
                data = _a.sent();
                console.log(typeof data);
                console.log(data);
                if (container) {
                    container.innerHTML = JSON.stringify(data === null || data === void 0 ? void 0 : data.results[0]);
                }
                return [2 /*return*/];
        }
    });
}); };
