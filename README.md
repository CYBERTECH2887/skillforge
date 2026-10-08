<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkillForge - GitHub README Preview</title>
    
    <!-- Tailwind CSS for the surrounding UI -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- GitHub Markdown CSS to simulate exact GitHub styling -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown-light.min.css">
    
    <!-- Marked.js for parsing Markdown to HTML -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

    <style>
        /* Custom tweaks to match GitHub's container look */
        body {
            background-color: #f6f8fa; /* GitHub light background */
        }
        .markdown-body {
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }
        @media (max-width: 767px) {
            .markdown-body {
                padding: 15px;
            }
        }
    </style>
</head>
<body class="antialiased text-gray-900 min-h-screen p-4 md:p-8">

    <div class="max-w-5xl mx-auto">
        
        <!-- Mock GitHub Repository Header -->
        <div class="flex items-center gap-2 text-xl mb-4 ml-1">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="fill-gray-500">
                <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
            </svg>
            <span class="text-blue-600 font-semibold hover:underline cursor-pointer">SakirJalal</span>
            <span class="text-gray-400">/</span>
            <span class="text-blue-600 font-bold hover:underline cursor-pointer">SkillForge-2.0</span>
            <span class="border border-gray-300 text-gray-500 text-xs px-2 py-0.5 rounded-full font-semibold ml-2">Public</span>
        </div>

        <!-- The File Container -->
        <div class="bg-white border border-gray-300 rounded-lg shadow-sm overflow-hidden">
            
            <!-- File Header (Mimics GitHub) -->
            <div class="bg-gray-50 border-b border-gray-300 px-4 py-3 flex justify-between items-center sticky top-0 z-10">
                <div class="flex items-center gap-3">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="fill-gray-500">
                        <path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V4.664a.25.25 0 0 0-.073-.177l-2.914-2.914a.25.25 0 0 0-.177-.073ZM8 3.25a.75.75 0 0 1 .75-.75h1.5a.75.75 0 0 1 0 1.5h-1.5A.75.75 0 0 1 8 3.25Zm-3 3a.75.75 0 0 1 .75-.75h5.5a.75.75 0 0 1 0 1.5h-5.5A.75.75 0 0 1 5 6.25Zm0 3a.75.75 0 0 1 .75-.75h5.5a.75.75 0 0 1 0 1.5h-5.5A.75.75 0 0 1 5 9.25Zm0 3a.75.75 0 0 1 .75-.75h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1-.75-.75Z"></path>
                    </svg>
                    <span class="font-semibold text-sm font-sans">README.md</span>
                </div>
                <div class="flex gap-2">
                    <button class="border border-gray-300 bg-gray-50 hover:bg-gray-100 text-gray-700 text-xs font-medium px-3 py-1 rounded-md transition">Raw</button>
                    <button class="border border-gray-300 bg-gray-50 hover:bg-gray-100 text-gray-700 text-xs font-medium px-3 py-1 rounded-md transition">Blame</button>
                </div>
            </div>

            <!-- Parsed Markdown will be injected here -->
            <div id="readme-content" class="markdown-body"></div>
        </div>
    </div>

    <!-- Raw Markdown Data. We put it in a script tag to prevent HTML escaping issues -->
    <script type="text/markdown" id="md-source">
<div align="center">
  <img src="https://img.icons8.com/?size=100&id=42384&format=png&color=F97316" alt="Logo" width="80" height="80">
  <h1 style="border-bottom: none; margin-bottom: 0;">⚡ SkillForge 2.0</h1>
  <p><b>An Advanced "Earn-While-You-Learn" Talent Marketplace</b></p>

  <img src="https://img.shields.io/badge/Python-Flask-blue?style=for-the-badge&logo=python" alt="Python Flask">
  <img src="https://img.shields.io/badge/Tailwind_CSS-Modern-38B2AC?style=for-the-badge&logo=tailwind-css" alt="Tailwind">
  <img src="https://img.shields.io/badge/Vanilla_JS-Animations-F7DF1E?style=for-the-badge&logo=javascript" alt="JavaScript">
</div>

---

> **"Don't buy a certificate. Earn your credentials."**

SkillForge 2.0 is a next-generation startup platform that bridges the gap between theoretical online courses and real-world company demands. Built with a robust **Python Flask** backend and a blazing-fast **Tailwind CSS + Vanilla JS** frontend, it evaluates coding logic, trains weak points adaptively, and pays users to solve real anonymized company micro-tasks.

---

## ✨ Cutting-Edge Features

* **🧠 AI-Adaptive Assessment & Timers:** Live countdown timers built with JS. The system adapts based on user performance, identifying specific gaps in knowledge instead of forcing generic courses.
* **🔍 Live Interactive Marketplace:** Features a real-time Vanilla JS search and filter system. Tasks are anonymized to protect company data but retain exact competency requirements.
* **🏆 The 3D Skill Passport:** Replaces useless PDF certificates. Features a dynamic, cryptographically styled profile with animated skill bars and an interactive **3D Tilt effect** built purely with JavaScript and CSS.
* **🎉 Modern UX/UI Ecosystem:** Completely styled with Tailwind CSS Glassmorphism. Includes advanced UI interactions like `Toastify` notifications and `Canvas Confetti` celebrations upon task completion.

---

## 🛠️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python (Flask)** | Core backend routing, session management, and rendering. |
| **HTML5** | Semantic structure for all dashboard, login, and marketplace screens. |
| **Tailwind CSS (CDN)** | Rapid utility-first styling, gradients, and responsive design. |
| **Vanilla JS** | DOM manipulation, 3D Tilt logic, Live Search, and Timers. |
| **Toastify JS** | Sleek, modern push notifications replacing native alerts. |
| **Canvas Confetti** | Visual celebration rendering on canvas elements. |

---

## 📁 Complete Folder Structure

```text
skillforge_python/
│
├── app.py                     # Python Flask Backend & App Routes
├── requirements.txt           # Python Dependencies (Flask==3.0.2)
├── templates/                 # HTML Templates
│   ├── base.html              # Layout with Navbar & Tailwind CDN
│   ├── index.html             # Landing Page with Typing Animations
│   ├── login.html             # Secure Login Page
│   ├── register.html          # User Registration
│   ├── dashboard.html         # User Dashboard & Earnings Tracker
│   ├── assessment.html        # Adaptive Test with Live Timers
│   ├── tasks.html             # Live Search Marketplace & Confetti
│   ├── passport.html          # 3D Tilt Profile & Skill Bars
│   └── hiring.html            # Company Hiring Hub
│
└── static/                    
    └── style.css              # Custom scrollbars and keyframe animations
```

---

## 🚀 Getting Started (Local Setup)

Follow these instructions to run the platform locally on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/SakirJalal/skillforge-python.git
cd skillforge-python
```

### 2. Set up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server
```bash
python app.py
```

**Access the platform at:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Hackathon Presentation Flow

If you are presenting this at a hackathon, follow this script for maximum impact:
1. **The Hook (`/index`):** Show the landing page. Explain the problem with paid PDF certificates. 
2. **The Verification (`/assessment`):** Take the test. Show the live timer. Pass the test and let the Confetti pop!
3. **The Business Model (`/tasks`):** Open the marketplace. Type in the Live Search bar to show real-time filtering. Click "Simulate Solve" to trigger the Toastify reward notification.
4. **The Moat (`/passport`):** Show the Skill Passport. Hover over the 3D Certificate to show the interactive tilt effect. Explain that this is what employers actually want to see.

---

## 📜 License
This project is open-source and built for Hackathon demonstrations under the [MIT License](LICENSE).
    </script>

    <script>
        // When the page loads, grab the markdown text, parse it, and inject it into the viewer.
        document.addEventListener('DOMContentLoaded', () => {
            const rawMarkdown = document.getElementById('md-source').textContent;
            
            // Configure Marked.js to format nicely
            marked.setOptions({
                gfm: true,
                breaks: true
            });

            // Parse and render
            const htmlContent = marked.parse(rawMarkdown);
            document.getElementById('readme-content').innerHTML = htmlContent;
        });
    </script>
</body>
</html>
