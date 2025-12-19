# 💼 Personal Portfolio Website

This project is my **personal portfolio website**, developed using **Django**, **MySQL**, and **Vanilla JavaScript**.
It showcases my skills, projects, and professional experience, and includes a fully functional contact form that sends messages via SMTP and stores data in a MySQL database.

---

## ⚙️ Backend Technologies

**Framework:** Django

### Apps

* **Contactform**

  * Handles all contact form logic
  * Includes:

    * MySQL integration (via `mysql.connector`)
    * Email sending logic (via `smtplib`)
* **Portfolio Core**

  * Main views and URL configurations for the website

---

## 🎨 Frontend Technologies

* **HTML5**
* **Vanilla/Classic CSS**
* **JavaScript (ES6)**

---

## 🧭 Pages Overview

| Page             | Description                                                                     |
| ---------------- | ------------------------------------------------------------------------------- |
| **Home**         | Start page introducing the portfolio                                            |
| **About**        | Personal information, career history, and interests                             |
| **Projects**     | A collection of my projects with GitHub links and descriptions                  |
| **Contact Me**   | A contact form to send information about yourself, your company, or a job offer |
| **Social**       | My social media links (alternative to the contact form)                         |
| **Legal Notice** | Imprint page                                                                    |
| **Legal Rights** | All legal information such as GDPR, cookies, and privacy details                |
| **Chatbot**      | A Chatbot that answer your questions based on the pages from the website        |

---

## 🧱 Folder Structure & Security

Several folders and files are **excluded via `.gitignore`** for security reasons:

* `.env` (environment variables)
* `security/`
* `documents/`
* `pdfs/`
* `deployment/`

These files contain sensitive information such as credentials and should **never** be published publicly.

---

## 📦 Required Libraries

* Django
* MySQL Connector (`mysql-connector-python`)
* smtplib

---

## 🧩 Database Setup

To test the contact form, you may need to create your own MySQL table using the following fields:

| Field           | Type     | Description             |
| --------------- | -------- | ----------------------- |
| `lname`         | VARCHAR  | Last name               |
| `gender`        | VARCHAR  | Gender                  |
| `email`         | VARCHAR  | Email address           |
| `phone`         | VARCHAR  | Phone number            |
| `company_name`  | VARCHAR  | Company name            |
| `company_url`   | VARCHAR  | Company website         |
| `company_email` | VARCHAR  | Company email           |
| `company_phone` | VARCHAR  | Company phone number    |
| `gdpr_value`    | BOOLEAN  | GDPR checkbox value     |
| `created_at`    | DATETIME | Timestamp of submission |

---

### Example – Django `request.POST` Structure

```python
gender = request.POST.get("gender")
fname = request.POST.get("fname")
lname = request.POST.get("lname")
email = request.POST.get("email")
phone = request.POST.get("tel-number")

company_name = request.POST.get("company-name")
company_url = request.POST.get("website")
company_mail = request.POST.get("company_email")
company_phone = request.POST.get("company-phone")

gdpr_value = request.POST.get("gdpr")
```

---

## ⚙️ Database Configuration

**File:** `backend/apps/contactform`

Make sure to update your MySQL connection settings:

```python
sql_server = mysql.connector.connect(
    database=os.getenv("DB_NAME"),
    host=os.getenv("DB_HOST"),
    port=3306,
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
```

**Parameters:**

* `database`: Name of your database
* `host`: `"localhost"`
* `port`: `3306`
* `user`: Your MySQL username
* `password`: Your MySQL password (root or custom user)

---

## ✉️ SMTP Configuration

You need a **Google App Password** for the SMTP client and two email addresses (sender & receiver).
Replace the following environment variables with your own data:

```python
sender_email = os.getenv("SMTP_SENDER_EMAIL")
receiver_email = os.getenv("SMTP_SENDER_EMAIL")
app_pw = os.getenv("EMAIL_APP_PASSWORD")
```

⚠️ Without these variables, Django will raise authentication errors when sending emails.

---

## ⚙️ Django Settings Adjustment

Make sure to update your database configuration in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "portfolio_website"),
        "USER": os.getenv("DB_USER", "agramm"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "3306"),
    }
}
```
---
> You don’t need to modify path variables in the HTML links— Django uses relative paths for child apps, so all directories are already configured correctly in the main project settings.
---

## 👨‍💻 Author

**Alex (Agramm18)**
📍 Augsburg, Germany
💻 [GitHub Profile](https://github.com/Agramm18)

---

## 🧾 Notes

* If you test this project locally, ensure you have MySQL and Python installed.
* Always store credentials securely in your `.env` file.
* Do **not** upload any sensitive or private data to public repositories.
* If everything goes as planed the website will be released in 2026
---

## ⭐ Tip

If you like this project, feel free to ⭐ **star the repository** on GitHub — it helps others discover it and supports my work!

---

## 📜 License

This project is open-source and available under the **MIT License**.
