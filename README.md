# ⚡ SkillForge 2.0

> **"Don't buy a certificate. Earn your credentials."**

SkillForge 2.0 is an advanced **Earn-While-You-Learn talent verification platform** built for the modern workforce. It bridges the gap between theoretical online courses and real-world industry demands. Instead of issuing easily faked PDF certificates, SkillForge evaluates actual coding logic, trains weak points, and pays users to solve anonymized micro-tasks from real companies.

---

## 🚀 Key Features

* **🧠 AI-Adaptive Assessments & Live Timers:** Interactive test modules with live reverse countdowns and animated progress bars that pinpoint exact knowledge gaps.
* **🔒 Anonymized Task Marketplace:** Real company tasks stripped of confidential data. Includes **Live Search filtering** and simulated payouts.
* **🛡️ 3D Animated Skill Passport:** A cryptographic, verifiable profile tracking star-ratings, completed tasks, and total earnings featuring a **3D Tilt-Card effect**.
* **🏆 Dynamic Leaderboards:** Ranks users locally (City Rank) and nationally (All India Rank) to foster healthy competition.
* **🤝 Company Hiring Hub:** A dedicated portal where recruiters can bypass resumes and directly hire pre-verified talent based on their platform performance.
* **✨ Modern UI/UX:** Built with Glassmorphism, Vanilla JS Typing effects, **Toastify notifications**, and **Canvas Confetti** for a premium Silicon Valley startup feel.

---

## 🛠️ Tech Stack

**Backend:**
* Python 3.x
* Flask (Web Framework)

**Frontend:**
* HTML5 / CSS3
* Vanilla JavaScript (ES6+)
* Tailwind CSS (via CDN)

**Libraries & UI Effects:**
* [Toastify JS](https://apvarun.github.io/toastify-js/) (Modern Notifications)
* [Canvas Confetti](https://www.kirilv.com/canvas-confetti/) (Success Animations)

---

## 📁 Project Structure

```text
skillforge_python/
│
├── app.py                     # Main Python Flask application & routes
├── requirements.txt           # Python dependencies
├── templates/                 # HTML UI Templates
│   ├── base.html              # Master layout with Navbar & Global JS
│   ├── index.html             # Landing Page (Typing effect)
│   ├── login.html             # Authentication
│   ├── register.html          # Registration
│   ├── forgot_password.html   # Password Recovery
│   ├── dashboard.html         # User Dashboard
│   ├── languages.html         # Domain/Field Selection
│   ├── assessment.html        # Test Module (Timer & Confetti)
│   ├── tasks.html             # Marketplace (Live Search & Toasts)
│   ├── passport.html          # Profile (3D Tilt Certificate & Ranks)
│   └── hiring.html            # Recruiter / Hiring Hub
│
└── static/                    
    └── style.css              # Custom CSS (Animations, Scrollbars, 3D logic)
