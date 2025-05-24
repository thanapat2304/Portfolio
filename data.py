# Portfolio data - projects, bio, and contact information

# Project data with chronological ordering
projects = [
    {
        "title": "Sale-Performance",
        "description": """Sale-Performance is a system developed specifically for sales teams. It provides a dashboard where users can view their own performance and pull data directly from the website. Previously, this data had to be requested from the IT department, which could take up to 20 minutes or more. With this system, users can access the information instantly, making their work more efficient. Additionally, weekly and monthly reports have been integrated into the system, eliminating routine tasks and allowing the team to focus more on supporting other departments and increasing sales. 
        \n For managers, the system allows them to view data for all salespeople, all customers, and compare sales performance against targets. This enables managers to track their team’s progress and ensure that salespeople are engaging with their assigned customers, preventing lost sales opportunities.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "Bootstrap 5", "JavaScript", "Bash Script", "MySql", "SQL Server", "Pandas", "Chart.js", "IIS", "pyodbc", "Jinja2", "xlwings", "Excel Macro"],
        "github_url": "https://sales-performance-c3y2.onrender.com",
        "year": 2025,
        "image_class": "fa-solid fa-chart-simple"
    },
    {
        "title": "Portfolio Website",
        "description": "A Flask-based portfolio website with a chronological storytelling layout and dark theme, showcasing projects by year with GitHub repository links.",
        "technologies": ["Flask", "Python", "HTML/CSS", "Bootstrap 5", "JavaScript"],
        "github_url": "https://github.com/yourusername/portfolio-website",
        "year": 2023,
        "image_class": "fa-solid fa-globe" # Font Awesome icon class
    },
    {
        "title": "Asset-System",
        "description": """Asset-System is a system developed for the accounting department to automate the calculation of asset depreciation. It was designed to ensure accurate tax filings and reduce manual workload. Previously, the process relied on Excel-based calculations, which were time-consuming and prone to human error.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "MySql", "Chart.js", "IIS", "pyodbc", "Jinja2"],
        "github_url": "https://asset-system.onrender.com",
        "year": 2024,
        "image_class": "fa-solid fa-computer"
    },
    {
        "title": "Transport-Route",
        "description": """Transport-Route is a system developed for the warehouse department to streamline fuel cost calculations and monitor delivery routes. This system was created to solve issues related to manual fuel tracking, where delivery personnel previously had to jot down fuel purchases on paper and recall fuel prices to summarize transport costs. This process was time-consuming and often inaccurate due to incomplete or incorrect entries."
        \n With this system, users only need to input the odometer reading, delivery date, and sales amount. The system then automatically calculates fuel consumption and matches it with real-time fuel prices retrieved from Bangchak’s fuel price API. This significantly improves efficiency, reduces human error, and provides accurate data for end-of-month reporting.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "MySql", "Chart.js", "IIS", "pyodbc", "Jinja2", "API Integration", "Windows Task Scheduler"],
        "github_url": "https://transport-route.onrender.com",
        "year": 2024,
        "image_class": "fa-solid fa-truck"
    },
    {
        "title": "Valolyze Project",
        "description": """Valolyze is a system developed to analyze the game Valorant by leveraging the MoViNet-PyTorch deep learning model. It extracts player actions from gameplay video recordings, allowing users to perform detailed and efficient game analysis. The system is specifically designed to support esports coaches and Valorant game analysts.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Python", "Flask", "HTML/CSS", "JavaScript", "Deep learning", "pytorch"],
        "github_url": "https://nattakonjpg.github.io/Valolyze/",
        "year": 2023,
        "image_class": "fa-solid fa-chart-line"
    },
    {
        "title": "Telegram Bot Invoice",
        "description": """Telegram_Bot_Invoice is designed to deliver shipping details for each branch via Telegram. Each branch is assigned to its own dedicated group chat, where the bot sends daily summary reports of all shipments. The bot automatically sends these reports three times a day: at 9:00 AM, 2:00 PM, and 5:00 PM.
        \n This bot was created to reduce the workload of the warehouse team, who previously had to manually compile and summarize shipping data in Excel every day.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Python", "Telegram Bot API", "Windows Task Scheduler", "Batch scripting", "SQL", "SQL Server"],
        "github_url": "https://github.com/thanapat2304/Telegram_Bot_Invoice",
        "year": 2024,
        "image_class": "fa-solid fa-comment"
    },
    {
        "title": "Sticker-System",
        "description": """Sticker-System was developed to resolve challenges in the sticker printing request and management process. Previously, job requests were submitted via the Line application, which often resulted in miscommunication, overlooked tasks, and unclear tracking of job statuses.
        \n The new system enables users to submit requests online and monitor progress in real time, with instant notifications sent directly to a dedicated Telegram group. This significantly reduces errors such as unrecorded pickups and missing work, while enhancing transparency throughout the entire workflow—from job submission and production to final collection.
        \n Sticker-System has become a vital tool for improving operational efficiency and facilitating seamless, structured collaboration across teams.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "MySql", "Chart.js", "IIS", "Jinja2", "Telegram Bot API"],
        "github_url": "https://sticker-system.onrender.com",
        "year": 2024,
        "image_class": "fa-solid fa-note-sticky"
    },
    {
        "title": "Personal Blog",
        "description": "A personal blog built from scratch with a custom CMS for managing posts and categories.",
        "technologies": ["PHP", "MySQL", "JavaScript", "CSS", "Markdown Support"],
        "github_url": "https://github.com/yourusername/personal-blog",
        "year": 2020,
        "image_class": "fa-solid fa-pen-to-square"
    },
    {
        "title": "Recipe Sharing Platform",
        "description": "A community platform for sharing and discovering recipes with rating and comments.",
        "technologies": ["Flask", "SQLAlchemy", "PostgreSQL", "JavaScript", "Cloudinary API"],
        "github_url": "https://github.com/yourusername/recipe-platform",
        "year": 2019,
        "image_class": "fa-solid fa-utensils"
    }
]

# Bio information for About page
bio_data = {
    "name": "Thanapurt Sopon",
    "tagline": "Automation Engineer & Full-stack Developer",
    "profile_image_class": "fa-solid fa-user-circle fa-10x",
    "intro": "I'm a passionate software developer with expertise in web development, data science, and cloud technologies.",
    "story": """
    I began my technology journey in 2022 by developing small-scale web applications and learning the fundamentals of programming. Since then, I have expanded my skill set to include backend development, database design, and deep learning. I enjoy creating web applications that solve real-world problems and automate tasks to save time and improve efficiency. My approach combines technical expertise with a strong focus on user experience and clean design. When I’m not coding, I enjoy reading finance books, exploring technology blogs, and going for runs to stay active.
    """,
    "education": [
        {
            "degree": "Statistics and Data Science Major: Informatics, Statistics and Data Science faculty of Science",
            "institution": "Khonkaen University",
            "year": "2020-2024"
        }
    ],
    "skills": [
        "Python", "JavaScript", "Flask", "Django", "React", 
        "SQL/NoSQL Databases", "RESTful APIs", "Docker", 
        "Cloud Services (AWS, GCP)", "Machine Learning"
    ]
}

# Contact information
contact_info = {
    "email": "thanapat.sop@gmail.com",
    "github": "https://github.com/thanapat2304",
    "linkedin": "https://linkedin.com/in/yourusername",
    "phon": "+66 617066959",
    "message": "I'm currently looking for opportunities to join a forward-thinking team where I can apply my skills and continue learning. If you're hiring or interested in collaborating, please don’t hesitate to reach out."
}
