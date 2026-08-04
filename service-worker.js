try {
    importScripts('/sw.js');
} catch (e) {
    console.log('Sw import notice:', e);
}

const CACHE_NAME = 'aktu-results-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/check-result.html',
  '/grade-calculator.html',
  '/attendance-calculator.html',
  '/percentage-calculator.html',
  '/calculators.html',
  '/about.html',
  '/contact.html',
  '/favicon.png',
  '/offline.html'
];

// Install Service Worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
  self.skipWaiting();
});

// Activate Service Worker
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch from cache, fallback to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Cache hit - return response
        if (response) {
          return response;
        }
        
        // Clone the request
        const fetchRequest = event.request.clone();
        
        return fetch(fetchRequest).then((response) => {
          // Check if valid response
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }
          
          // Clone the response
          const responseToCache = response.clone();
          
          caches.open(CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseToCache);
            });
          
          return response;
        }).catch(() => {
          // Return offline page if network fails
          return caches.match('/offline.html');
        });
      })
  );
});

// Background Sync for notifications
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-results') {
    event.waitUntil(syncResults());
  }
});

async function syncResults() {
  // Sync logic here
  console.log('Syncing results...');
}

// Push Notifications
self.addEventListener('push', (event) => {
  const options = {
    body: event.data ? event.data.text() : 'New AKTU result declared!',
    icon: '/favicon.png',
    badge: '/favicon.png',
    vibrate: [200, 100, 200],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'check',
        title: 'Check Now',
        icon: '/favicon.png'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/favicon.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('AKTU Results', options)
  );
});

// Notification click handler
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  
  if (event.action === 'check') {
    event.waitUntil(
      clients.openWindow('/check-result.html')
    );
  }
});
