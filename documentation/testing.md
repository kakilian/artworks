## Testing Overview

This document outlines the **manual** and **automated** testing carried out on the *Artworks* e-commerce site. It includes Lighthouse performance audits, W3C validations, user journey testing, and device responsiveness checks.

---

### 1. Lighthouse Performance Testing

Two audits were run using [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/):

**Desktop:**

| Metric         | Score |
| -------------- | ----- |
| Performance    | 92    |
| Accessibility  | 98    |
| Best Practices | 100   |
| SEO            | 100   |

**Mobile:**

| Metric         | Score |
| -------------- | ----- |
| Performance    | 74    |
| Accessibility  | 98    |
| Best Practices | 100   |
| SEO            | 100   |

> Mobile performance dipped slightly due to third-party scripts and image loading.

---

### 2. W3C Validation

#### CSS Validation

Tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/):

* ✅ Passed with 3 minor errors:

  * Use of comma instead of dot in decimal values (`1,5em`)
  * Misuse of word-spacing and font-size units.
* Warnings mainly stemmed from Bootstrap’s use of vendor extensions (ignored).

#### HTML Validation

Run with [W3C HTML Validator](https://validator.w3.org/):

* ✅ No critical errors.
* Minor warnings related to meta tag duplication and ARIA labels.

---

### 3. Manual Testing

Each page and flow was tested on desktop and mobile:

| Feature                | Tested Path                                |
| ---------------------- | ------------------------------------------ |
| Homepage load          | `/`                                        |
| About page             | `/about/`                                  |
| Artist listing         | `/artworks/artists/`                       |
| Individual artist      | `/artworks/artists/<int:pk>/`              |
| Artwork listing        | `/artworks/`                               |
| Artwork detail         | `/artworks/<int:pk>/`                      |
| Cart add/remove/update | `/cart/`, `/cart/update/`, `/cart/remove/` |
| Checkout flow          | `/checkout/`, `/create-checkout-session/`  |
| Newsletter signup      | any page footer                            |
| Custom 404 page        | `/nonexistent-url/`                        |
| Login/Signup           | `/login/`, `/signup/`                      |
| Order history          | `/orders/`                                 |

---

### 4. Device & Browser Compatibility

Tested on:

* **Devices:** MacBook, iPhone 13 (DevTools), Samsung Galaxy S8 (DevTools)
* **Browsers:** Chrome (latest), Firefox, Edge

Known mobile UI issue:

* Certain full-page screenshots revealed layout shifts in footer and form spacing (see attached screenshots in `/documentation/images/testing/`).

---

### 5. Bugs & Resolved Issues

| Bug                                  | Status  | Notes                            |
| ------------------------------------ | ------- | -------------------------------- |
| Footer layout breaking on cart empty | ✅ Fixed | Adjusted CSS spacing             |
| Signup form overflow on mobile       | ✅ Fixed | Added responsive breakpoints     |
| Broken newsletter image links        | ✅ Fixed | Corrected path casing + filename |


