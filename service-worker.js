const CACHE_NAME = "my-app-cache-v1";
const urlsToCache = [
  "/",
  "index.html",  // Assuming this is at the root level
  "manifest.json",
  "robots.txt",

  "production/files/giphy.gif",
  "production/files/v1.2.html",
  "production/files/v1.4.html",
  "production/redirect.html",
  "production/version.txt",

  "assets/img/TypeBlitz-128.png",
  "assets/img/TypeBlitz-192.png",
  "assets/img/TypeBlitz-512.png",
  "assets/img/TypeBlitz.ico",

  "assets/screenshots/1.png",
  "assets/screenshots/2.png",
  "assets/screenshots/3.png",
  "assets/screenshots/4.png",
  "assets/screenshots/5.png",
  "assets/screenshots/6.png",

  "assets/preloader.css",
  "assets/common.css",

  "assets/404.html",
  "assets/offline.html",
  "assets/MIT_License.html",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
      .then(() => self.skipWaiting())
      .catch((error) => {
        console.error("Failed to add URLs to cache:", error);
      })
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) {
        return response;
      }
      return fetch(event.request)
        .then((response) => {
          if (response.status === 404) {
            return caches.match("/files/404.html");
          }
          return caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request.url, response.clone());
            return response;
          });
        })
        .catch(() => {
          return caches.match("/files/offline.html");
        });
    })
  );
});
