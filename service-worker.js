const CACHE_NAME = "my-app-cache-v1";
const urlsToCache = [
  "/",
  "/index.html",
  "assets/preloader.css",
  "assets/common.css",
  "assets/img/skill.png",
  "assets/img/6139.jpg",
  "assets/img/skill-128.png",
  "assets/img/skill-192.png",
  "assets/img/skill-512.png",
  "/assets/v1.2.html",
  "/assets/v1.2.6.8.html",
  "/assets/v1.6.html",
  "/assets/v1.8.html",
  "/assets/v2.0.html",
  "/assets/v2.2.html",
  "/assets/v2.0.0.4.html",
  "assets/screenshots/1.png",
  "assets/screenshots/2.png",
  "assets/screenshots/3.png",
  "assets/screenshots/4.png",
  "assets/screenshots/5.png",
  "assets/screenshots/6.png",
  "assets/screenshots/7.png",
  "assets/screenshots/8.png",
  "assets/404.html",
  "assets/offline.html",
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
