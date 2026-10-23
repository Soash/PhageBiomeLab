# 🧬 PhageBiomeLab: Laboratory Information Management System & Research Web Portal

[![Live Site](https://img.shields.io/badge/Live_Site-phagebiomelab.com-2ea44f?style=for-the-badge&logo=google-chrome&logoColor=white)](https://phagebiomelab.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Status](https://img.shields.io/badge/Deployment-Production-success?style=for-the-badge)](https://phagebiomelab.com/)

> **PhageBiomeLab** is a centralized scientific data infrastructure, biobank repository, and academic portal developed for the **PhageBiome Research Group** at the **Shahjalal University of Science and Technology, Sylhet, Bangladesh**. 
> 
> The platform was engineered to solve data fragmentation in microbiology laboratories by integrating biobank isolate tracking (bacterial pathogens and bacteriophages) with academic portfolio and publication management.

---

## 📌 Research & Project Context

Antimicrobial Resistance (AMR) represents one of the most critical threats to modern global public health. The **PhageBiome Lab** conducts *in vivo* and *in silico* investigations into:
- **Bacteriophage Therapy:** Screening and characterizing therapeutic phages targeting multi-drug resistant (MDR) bacterial pathogens.
- **Microbiome Dynamics:** Profiling microbial community shifts under therapeutic interventions.
- **Pathogen Genomics & AMR Profiling:** Correlating genomic determinants with phenotypic resistance patterns.

### The Problem Addressed
Microbiology and genomic research wet-labs frequently face challenges with fragmented spreadsheets, loss of historical isolate metadata (e.g., 16S rRNA sequences, host range, storage temperatures), and lack of synchronized public dissemination. **PhageBiomeLab** provides a structured relational system ensuring data integrity, traceability, and seamless public communication.

---

## 🚀 Core Features & Capabilities

### 1. 🧫 Biological Repository & Biobank Management
- **Bacterial Strain Cataloging:**
  - Tracks taxonomic classification (Species, Strain ID) and clinical/environmental isolation source.
  - Records molecular identification parameters (16S rRNA sequence markers).
  - Documents Antimicrobial Resistance (AMR) susceptibility profiles and ultra-low storage temperatures ($-80^\circ\text{C}$ / liquid nitrogen).
- **Bacteriophage Biobank:**
  - Catalogs phage isolates with verified bacterial host specificity.
  - Stores genetic characteristics, life cycles (lytic vs. lysogenic), particle morphology, and cryopreservation protocols.
  - Filterable public and internal database interface for laboratory benchmarking.

### 2. 🎓 Academic Portfolio & Researcher Profiles
- Comprehensive academic profile management categorized into **Principal Investigators**, **Co-investigators**, **PhD Students**, **MS (Thesis) Students**, **Undergraduate Researchers**, and **Alumni**.
- Relational mapping of academic credentials per researcher:
  - Peer-reviewed publications and conference proceedings.
  - Active and previous research grants and projects.
  - Academic honours, awards, and external affiliations.
  - Pedagogical and teaching appointments.

### 3. 🔬 Research Dissemination Engine
- Dynamic indexing of **ongoing investigations** versus **peer-reviewed publications**.
- Interactive media gallery showcasing laboratory infrastructure, field sampling, and electron/fluorescence microscopy data.
- Built-in rich-text editing (TinyMCE integration) enabling lab members to update project summaries without manual HTML drafting.

### 4. ⚙️ Production-Grade Engineering & Security
- **Decoupled Architecture:** Configuration managed cleanly via environment variables (`django-environ`).
- **Static Asset Pipeline:** Optimized static compression and caching using WhiteNoise.
- **Media Asset Processing:** Automated image optimization with Pillow.
- **Automated Continuous Deployment:** Custom webhook listener (`deploy.php` / `deploy.sh`) triggering automated repository pulls, migration execution, and static asset collection upon branch updates.

---

## 🏛️ System Architecture & Data Schema

The platform is designed around Django's Model-View-Template (MVT) pattern with normalized relational database models:

```
                            ┌────────────────────────┐
                            │      TextContent /     │
                            │      ImageContent      │
                            └────────────────────────┘
                                         ▲
                                         │ CMS & Carousels
┌───────────────────────┐   ┌────────────────────────┐   ┌───────────────────────┐
│     Bacteria Model    │   │      Member Model      │   │ ResearchProject Model │
├───────────────────────┤   ├────────────────────────┤   ├───────────────────────┤
│ • Species & Strain ID │   │ • Name, Category, Bio  │   │ • Title & Description │
│ • Source & Date       │   │ • Contact & Affiliation│   │ • Status (Ongoing /   │
│ • 16S Identification  │   └───────────┬────────────┘   │   Published)          │
│ • AMR Susceptibility  │               │ 1:N            │ • URL & Banners       │
│ • Storage Temperature │       ┌───────┴────────┐       └───────────────────────┘
└───────────────────────┘       │ Relational CV  │
                                ├────────────────┤
┌───────────────────────┐       │ • Publications │
│      Phage Model      │       │ • Awards       │
├───────────────────────┤       │ • Conferences  │
│ • Name & Host Specific│       │ • Teachings    │
│ • Isolation Source    │       │ • Education    │
│ • Life Cycle & Morph. │       │ • Projects     │
│ • Genetic Info        │       └────────────────┘
└───────────────────────┘
```

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **Python 3.10+ / Django 5.1** | Robust ORM, URL routing, authentication, and admin governance |
| **Database** | **SQLite (Dev) / Relational SQL** | Relational data persistence with strict foreign key constraints |
| **Rich Text Editor** | **django-tinymce** | In-browser WYSIWYG editing for complex scientific summaries |
| **Asset Pipeline** | **WhiteNoise & Pillow** | Static asset compression, HTTP caching, and media processing |
| **Frontend** | **HTML5, CSS3, JavaScript, Bootstrap** | Responsive scientific UI and dynamic query filtering |
| **Deployment / CI** | **Linux, cPanel, Git Webhooks, Bash** | Automated build and zero-downtime deployment scripts |

---

## 📂 Repository Structure

```
PhageBiomeLab/
├── app/                        # Core Django application
│   ├── migrations/             # Database migration version control
│   ├── admin.py                # Admin site configuration & inline models
│   ├── models.py               # Biological & academic relational schemas
│   ├── urls.py                 # Application URL dispatcher
│   └── views.py                # Business logic, query filtering, and context builders
├── project/                    # Project settings & WSGI/ASGI gateways
│   ├── settings.py             # Environment-aware Django settings
│   ├── urls.py                 # Root URL configuration
│   └── wsgi.py                 # Web Server Gateway Interface entry point
├── templates/                  # Modular HTML templates
│   ├── admin/                  # Custom admin interface templates
│   ├── base.html               # Master layout with navigation and footer
│   ├── database.html           # Public biobank & isolate database view
│   ├── member_detail.html      # Comprehensive academic CV template
│   ├── members.html            # Lab member directory
│   ├── ongoing_research.html   # Ongoing lab projects view
│   └── published_research.html # Peer-reviewed publications index
├── static/ & staticfiles/      # Compiled stylesheets, JavaScript, and iconography
├── media/                      # Uploaded bio-images, member headshots, and project art
├── manage.py                   # Django CLI management utility
└── requirements.txt            # Explicit dependency pinning
```

---

## 💻 Local Setup & Installation

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Soash/PhageBiomeLab.git
cd PhageBiomeLab
```

### 2. Configure Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root directory:
```env
ENVIRONMENT=development
SECRET_KEY=your-secure-django-secret-key
```

### 5. Apply Migrations & Initialize Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser. Access the administrative dashboard at `http://127.0.0.1:8000/admin/`.

---

## 🚢 Deployment & Continuous Delivery

The live platform is deployed using an automated git-driven webhook pipeline:
1. Pushing commits to the `main` branch triggers a remote webhook endpoint (`deploy.php`).
2. A bash deployment sequence (`deploy.sh`) pulls latest changes, applies schema migrations, and collects static assets:
```bash
git pull origin main
python manage.py migrate --noinput
python manage.py collectstatic --noinput
```

---

## 👤 Developer & Maintainer

**Md Abu Sadat Soash**
- **Role:** Full-Stack Architect & Lead Developer
- **Academic Background:** Department of Genetic Engineering and Biotechnology, Shahjalal University of Science and Technology, Sylhet, Bangladesh
- **Portfolio:** [soash.github.io](https://soash.github.io/)
- **GitHub:** [@Soash](https://github.com/Soash)

*Co-developed with Mutashim Ahammed Rafi.*

---

## 📄 License & Attribution

Developed for **PhageBiome Lab**, Shahjalal University of Science and Technology, Sylhet, Bangladesh. All rights reserved.
