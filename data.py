# Portfolio data - projects, bio, and contact information

# Project data with chronological ordering
projects = [
    {
        "title": "Sale-Performance",
        "description": """Sale-Performance is a system developed specifically for sales teams. It provides a dashboard where users can view their own performance and pull data directly from the website. Previously, this data had to be requested from the IT department, which could take up to 20 minutes or more. With this system, users can access the information instantly, making their work more efficient. Additionally, weekly and monthly reports have been integrated into the system, eliminating routine tasks and allowing the team to focus more on supporting other departments and increasing sales. 
        \n For managers, the system allows them to view data for all salespeople, all customers, and compare sales performance against targets. This enables managers to track their team's progress and ensure that salespeople are engaging with their assigned customers, preventing lost sales opportunities.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "Bootstrap 5", "JavaScript", "Bash Script", "MySql", "SQL Server", "Pandas", "Chart.js", "IIS", "pyodbc", "Jinja2", "xlwings", "Excel Macro"],
        "github_url": "https://sales-performance-c3y2.onrender.com",
        "year": 2025,
        "image_path": "/static/images/projects/sales-performance.jpg"
    },
    {
        "title": "Portfolio Website",
        "description": """This portfolio website is created to collect and showcase all the works of Thanapurt Sopon
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "HTML/CSS", "Bootstrap 5", "JavaScript", "Jinja2"],
        "github_url": "https://github.com/thanapat2304/Portfolio",
        "year": 2025,
        "image_path": "/static/images/projects/port.jpg"
    },
    {
        "title": "Asset-System",
        "description": """Asset-System is a system developed for the accounting department to automate the calculation of asset depreciation. It was designed to ensure accurate tax filings and reduce manual workload. Previously, the process relied on Excel-based calculations, which were time-consuming and prone to human error.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "MySql", "Chart.js", "IIS", "pyodbc", "Jinja2"],
        "github_url": "https://asset-system.onrender.com",
        "year": 2024,
        "image_path": "/static/images/projects/Asset-System.jpg"
    },
    {
        "title": "Transport-Route",
        "description": """Transport-Route is a system developed for the warehouse department to streamline fuel cost calculations and monitor delivery routes. This system was created to solve issues related to manual fuel tracking, where delivery personnel previously had to jot down fuel purchases on paper and recall fuel prices to summarize transport costs. This process was time-consuming and often inaccurate due to incomplete or incorrect entries."
        \n With this system, users only need to input the odometer reading, delivery date, and sales amount. The system then automatically calculates fuel consumption and matches it with real-time fuel prices retrieved from Bangchak's fuel price API. This significantly improves efficiency, reduces human error, and provides accurate data for end-of-month reporting.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "MySql", "Chart.js", "IIS", "pyodbc", "Jinja2", "API Integration", "Windows Task Scheduler"],
        "github_url": "https://transport-route.onrender.com",
        "year": 2024,
        "image_path": "/static/images/projects/route.jpg"
    },
    {
        "title": "Valolyze Project",
        "description": """Valolyze is a system developed to analyze the game Valorant by leveraging the MoViNet-PyTorch deep learning model. It extracts player actions from gameplay video recordings, allowing users to perform detailed and efficient game analysis. The system is specifically designed to support esports coaches and Valorant game analysts.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Python", "Flask", "HTML/CSS", "JavaScript", "Deep learning", "pytorch"],
        "github_url": "https://nattakonjpg.github.io/Valolyze/",
        "year": 2023,
        "image_path": "/static/images/projects/valolyze.jpg"
    },
    {
        "title": "Telegram Bot Invoice",
        "description": """Telegram_Bot_Invoice is designed to deliver shipping details for each branch via Telegram. Each branch is assigned to its own dedicated group chat, where the bot sends daily summary reports of all shipments. The bot automatically sends these reports three times a day: at 9:00 AM, 2:00 PM, and 5:00 PM.
        \n This bot was created to reduce the workload of the warehouse team, who previously had to manually compile and summarize shipping data in Excel every day.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Python", "Telegram Bot API", "Windows Task Scheduler", "Batch scripting", "SQL", "SQL Server"],
        "github_url": "https://github.com/thanapat2304/Telegram_Bot_Invoice",
        "year": 2024,
        "image_path": "/static/images/projects/telegram.jpg"
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
        "image_path": "/static/images/projects/e-ticket.jpg"
    },
    {
        "title": "IT-Service",
        "description": """This system was developed to provide all employees with a convenient and structured way to report issues or request assistance from the IT department. Once a request is submitted, a real-time notification is automatically sent to all IT staff via Telegram, ensuring prompt awareness and response.
        \n After resolving an issue, IT personnel record the details of the resolution process, including the methods used, in the system. This documentation allows others to reference and follow the same steps if similar problems arise in the future. Additionally, the system serves as a valuable tool for collecting service data, which can be used to evaluate the IT department's annual KPIs more effectively.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "MySql", "Chart.js", "IIS", "Jinja2", "Telegram Bot API"],
        "github_url": "https://it-service-lf5x.onrender.com",
        "year": 2024,
        "image_path": "/static/images/projects/it.jpg"
    },
    {
        "title": "FDA-Service",
        "description": """Developed to solve inefficiencies in retrieving FDA certification documents. Previously, sales staff had to request certificates from the import department, who then manually searched through multiple folders—often taking a long time or sometimes failing to find the correct files due to inconsistent naming. This system centralizes and automates document retrieval, reducing search time to 1–2 minutes, significantly improving workflow efficiency and supporting increased sales effectiveness.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "Bootstrap 5", "MySql", "Chart.js", "IIS", "Jinja2", "os"],
        "github_url": "https://fda-service.onrender.com",
        "year": 2025,
        "image_path": "/static/images/projects/fda.jpg"
    },
    {
        "title": "Forecasting-System",
        "description": """The Forecasting-System was developed to support the Import department in consolidating monthly sales forecast data from the sales team. Previously, each salesperson submitted their individual forecast requests via email, requiring the Import team to open and review each email manually, then compile the data into Excel. This process was time-consuming and prone to data omissions.
        \n The Forecasting-System directly addresses this issue by allowing the Import team to instantly view consolidated forecast data by product, along with the number of salespeople and customers involved. On the sales side, instead of sending emails, sales staff can now conveniently submit their forecasts through a dedicated Forecasting menu within the Sales-Performance system. This streamlines the workflow and significantly improves operational efficiency for both teams.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "HTML/CSS", "JavaScript", "Bootstrap 5", "MySql", "Chart.js", "IIS", "Jinja2"],
        "github_url": "https://forecasting-system.onrender.com",
        "year": 2025,
        "image_path": "/static/images/projects/frorecast.jpg"
    },
    {
        "title": "Line-Chatbot",
        "description": """This Line Chatbot was developed as an extension of the Forecasting-System, designed to provide users with a fast and convenient way to check product availability relevant to their own sales quota.
        \n Users can send a message in the format: "คงเหลือ 10313 ของ 4567 เดือน 7" to inquire about the remaining stock of product code 10313, under the responsibility of salesperson ID 4567, for the month of July. 
        \n The system instantly calculates: "Forecast Quantity – Actual Sales" and returns the real-time remaining balance.
        \n This function addresses a long-standing challenge where sales staff were previously unable to check their available stock on demand. They had to rely on other departments for this information, which often caused delays, increased the risk of overcommitting stock, or even led to missed sales opportunities due to waiting for confirmations.
        \n Additionally, users can check overall warehouse stock by sending a message such as: "ตรวจ Y-127771" 
        \n to view the total remaining quantity of product code Y-127771 across all sales. This is especially useful when an individual salesperson's quota is insufficient—they can quickly check if another salesperson has excess stock and coordinate a transfer, helping prevent lost sales due to stockouts.
        \n You can view a live demo of this project by clicking the "View Project" button below. """,
        "technologies": ["Flask", "Python", "SQL", "MySql", "LINE Messaging API", "Webhook Handling", "IIS"],
        "github_url": "https://github.com/thanapat2304/Line-Chatbot",
        "year": 2025,
        "image_path": "/static/images/projects/line.jpg"
    },
    {
        "title": "Intranet-Service",
        "description": """The Intranet-Service system has been developed as a centralized hub for internal organizational system links, designed to facilitate quick and easy access to various platforms. Additionally, the system efficiently supports the announcement and dissemination of important news and information within the organization.
        \n You can view a live demo of this project by clicking the "View Project" button below.""",
        "technologies": ["Flask", "Python", "SQL", "MySql", "HTML/CSS", "JavaScript", "IIS", "Jinja2"],
        "github_url": "https://intranet-service.onrender.com",
        "year": 2024,
        "image_path": "/static/images/projects/intranet.jpg"
    }
]

# Bio information for About page
bio_data = {
    "name": "Thanapurt Sopon",
    "tagline": "Python Developer & Full-stack Developer",
    "profile_image_class": "fa-solid fa-user-circle fa-10x",
    "intro": "I'm a passionate software developer with expertise in web development, data science, and technologies.",
    "story": """
    I began my technology journey in 2022 by developing small-scale web applications and learning the fundamentals of programming. Since then, I have expanded my skill set to include backend development, database design, and deep learning. I enjoy creating web applications that solve real-world problems and automate tasks to save time and improve efficiency. My approach combines technical expertise with a strong focus on user experience and clean design. When I'm not coding, I enjoy reading finance books, exploring technology blogs, and going for runs to stay active.
    """,
    "education": [
        {
            "degree": "Statistics and Data Science Major: Informatics, Statistics and Data Science faculty of Science",
            "institution": "Khonkaen University",
            "year": "2020-2024"
        }
    ],
    "experience": [
        {
            "workplace": "American-European Products (AEP)",
            "position": "Developer",
            "year": "2024-2025"
        }
    ],
    "skills": [
        "Python", "Flask", "SQL (MySQL, SQL Server)", "HTML/CSS/JavaScript", "Bootstrap", 
        "API Integration", "Batch Scripting", "Excel Macro", 
        "IIS (Internet Information Services)"
    ]
}

# Contact information
contact_info = {
    "email": "thanapat.sop@gmail.com",
    "github": "https://github.com/thanapat2304",
    "linkedin": "https://linkedin.com/in/yourusername",
    "phon": "+66 617066959",
    "message": "I'm currently seeking opportunities to join a dynamic and innovative team where I can contribute my skills, grow professionally, and take on meaningful challenges. If you're hiring or open to collaboration, feel free to reach out—I'd love to connect."
}
