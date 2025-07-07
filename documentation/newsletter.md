# Newsletter Signup & Brevo Integration

This project includes a robust newsletter signup feature, built with Django and designed for seamless integration with modern email marketing platforms such as [Brevo (formerly Sendinblue)](https://www.brevo.com/).

---

## ✉️ Feature Overview

- **Atomic newsletter app:** The signup feature is handled by a dedicated Django app, ensuring clear code structure and easy future updates.
- **Footer integration:** Users can sign up directly from any page via the footer.
- **Confirmation logic:** After successful signup, the form is replaced with a thank-you message and custom image for clean UX.
- **No duplicate signups:** Attempting to sign up again with the same email shows a clear, user-friendly error.
- **Responsive design:** The signup form, feedback messages, and all visuals adapt perfectly on mobile, tablet, and desktop.

---

## 🚀 Brevo (Sendinblue) Setup Walkthrough

### 1. Brevo Dashboard (Home)
Overview of the Brevo dashboard where all email marketing features are managed.

![Brevo Contacts](documentation/images/newsletter/brevo-contacts.png)

---

### 2. Initial Setup & API Keys
Shows the settings/API page, where you connect your Django app for real mailing list integration.

![Brevo Setup Screenshot](documentation/images/newsletter/brevo-setting-up.png)

---

### 3. Contacts Management
How new subscribers are managed as contacts, ready for newsletters and updates.

![Brevo Contacts Screenshot](documentation/images/newsletter/brevo-contacts.png)

---

## 💡 Why This Matters

- **Realistic e-commerce workflow:** Mimics industry-standard newsletter capture.
- **Session logic:** Hides the form after signup for this session to prevent spam or confusion.
- **Easy to extend:** Swap Brevo for Mailchimp, Moosend, or any other provider.
- **GDPR-Ready:** Double opt-in and user privacy can be toggled via Brevo.

---

## 🛠️ How To Change Provider

To swap in another email marketing tool:
- Update the form action/endpoint in `newsletter_form.html` and settings as needed.
- See the official docs for Mailchimp, Moosend, etc.

---

## 📷 Screenshots

**1. Newsletter signup form in the footer:**  
Users can enter their email on any page to join the mailing list.

![Newsletter signup form](documentation/images/newsletter/newsletter-signup-form.png)

**2. Confirmation message after successful signup:**  
Users instantly see feedback — “Thanks for subscribing!” — and the form disappears.

![Newsletter confirmation](documentation/images/newsletter/newsletter-confirmation.png)

**3. Footer after signup (form hidden):**  
Once subscribed, the newsletter form is hidden from the footer for the rest of the session, creating a distraction-free experience.

![Footer after signup](documentation/images/newsletter/newsletter-footer-after.png)

---

*For further questions or to suggest improvements, reach out on [LinkedIn](https://www.linkedin.com/in/katarina-kilian-645242313/).*

