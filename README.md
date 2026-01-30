# WordCollector

WordCollector is an automation project that searches for a word using a public API, retrieves its definitions and usage examples, stores the data in a local database, and sends the results by email.

The project was designed to practice backend fundamentals, automation, and integration between services, with future plans to run it periodically on a cloud server.

---

## 🛠 Technologies Used

- Python  
- SQLite  
- Bash  
- External Dictionary API  
- SMTP (Email sending)  
- dotenv (.env configuration)

---

## ✨ Features

- Search for a word using an external API  
- Retrieve definitions and usage examples  
- Store results in a SQLite database  
- Send the collected information via email  
- Environment variable configuration using `.env`  
- Ready for future automation with Bash and AWS

---

## 🔄 Process

1. The user defines a word to be searched  
2. Python sends a request to a dictionary API  
3. Definitions and examples are processed  
4. The data is saved into a SQLite database  
5. An email is sent containing the collected information  
6. (Planned) Bash script will automate execution on an AWS server

> ⚠️ To enable email sending, the user must configure the `.env` file and generate an application-specific password by enabling 2FA on their Google account.

---

## 📚 Lessons Learned

- Working with external APIs and handling responses  
- Managing environment variables securely with `.env`  
- Using SQLite for lightweight data persistence  
- Sending emails programmatically via SMTP  
- Structuring a project for future scalability and automation  
- Understanding how Bash can be used to automate backend routines
