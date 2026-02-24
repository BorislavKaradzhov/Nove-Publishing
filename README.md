# NOVE Publishing - Manuscript Submission Platform

A Django-based web application built for the **Django Basics Exam** @ SoftUni. This platform allows aspiring authors to create profiles, submit book manuscripts, and track their review status, while providing an internal system for editors to manage genres and update submission statuses. The application could serve as a possible feature for the existing website www.novepublishing.bg, which I have designed and developed. 

## 🏆 Exam Requirements Checklist

- [x] **PostgreSQL Database:** Configured via `settings.py` and environment variables.
- [x] **3 Django Apps:** `common` (Core/Landing), `authors` (Profiles), `submissions` (Manuscripts & Genres).
- [x] **3 Database Models:** `Author`, `Submission`, and `Genre`.
- [x] **Relationships:**
  - One-to-Many (`Author` -> `Submission`)
  - Many-to-Many (`Submission` <-> `Genre`)
- [x] **3 Forms:** Customized ModelForms for Authors, Submissions, and Genres.
- [x] **Form Customization:** Disabled/Read-only fields utilized in Delete Views and Editor Update Views.
- [x] **Model Validations:**
  - Custom validator (`validate_letters_and_dashes`) for author names.
  - Built-in `MinLengthValidator` and `unique=True` constraints.
- [x] **CRUD Operations:** Full Create, Read, Update, and Delete functionality implemented using Django Generic Class-Based Views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`).
- [x] **10+ Templates:** Comprehensive UI built with Bootstrap 5, utilizing base template extension (`{% extends %}`).
- [x] **No Authentication:** Strictly adhered to the rule of excluding Django User/Authentication systems while maintaining logical data flow.

## 🚀 Advanced Features (Extra Functionality)

The following features were implemented:

1. **Objects Filtering:** Implemented sorting in the `SubmissionListView`. This allows authors and visitors to sort by the submission's `title` or `status`, as well as by the author's `first_name`, `last_name`, or `email`.
2. **Custom Template Filters:** Created `submission_extras.py` with custom filters (`status_percentage`, `status_color`) to dynamically render a Bootstrap Progress Bar indicating the exact stage of a manuscript's review process.
3. **Editor Status Management:** Implemented a specialized `UpdateView` with a constrained form (`ChangeStatusForm`) allowing staff to update submission statuses without needing to access the Django Admin panel.
4. **Data Normalization:** Overrode the `clean()` method in the `Genre` model to automatically apply Title Case, preventing case-sensitive database duplicates (e.g., "Sci-Fi" vs "sci-fi").
5. **Alphabetical Pagination:** Configured alphabetical ordering and pagination (6 items per page) for the Genre list to ensure a clean UX. Configured pagination for the Submissions and Authors.

## 🗄️ Project Architecture

### 1. `common` App
- Acts as the central hub.
- Contains the `HomePageView` and routing to direct users to either the Author portal or Submission portal.

### 2. `authors` App
- **Model:** `Author` (First Name, Last Name, Email, Bio).
- **Functionality:** Authors can register their profiles, update their bios, and withdraw their profiles from the system.

### 3. `submissions` App
- **Models:** `Submission` (Title, Synopsis, Script, Status) and `Genre` (Name).
- **Functionality:** Handles manuscript submissions, genre categorization, and status tracking (Pending Review -> Under Review -> Accepted for Publication/Rejected).


### Prerequisites ###

To run this project, you will need:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/install/windows) for your applicable OS.
  - On Windows, use Git Bash or the Windows Command Prompt with the <code>git clone</code> command listed in Step. 1 below.
  - On Linux/Ubuntu, Open the terminal and use the <code>git clone</code> command listed in Step. 1 below. Git might need to be installed using your distribution’s package manager.
  - On macOS, open the Terminal app and use the <code>git clone</code> command listed in Step. 1 below. Git comes pre-installed on most Macs, or it can be installed via Xcode Command Line Tools.
- [PostgreSQL](https://www.postgresql.org/download/) for the database.

## 🛠️ Local Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/BorislavKaradzhov/Nove-Publishing.git
    cd Nove-Publishing

2. **Create and activate a virtual environment:**

Copy the .env.template file:
    
    cp .env.template .env
    
#### Windows:
    python -m venv venv
    venv\Scripts\activate
#### macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Set Up the Database:**

Ensure PostgreSQL is running and set up your database using the credentials provided in the <code>.env</code> file. Connect to the database. If new to PostgreSQL, please follow this [tutorial](https://www.w3schools.com/postgresql/postgresql_getstarted.php). To create the database, please execute the following in <code>SQL Shell (psql)</code>:
<code>CREATE DATABASE nove_publishing_db;</code>.
Then, connect to the database in <code>SQL Shell (psql)</code>:
<code>\c nove_publishing_db;</code>.
   
5. **Apply Migrations:**
    ```bash
    python manage.py migrate

6. **Create a Superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    
Follow the prompts to set up the superuser credentials.
   
7. **Run the Server:**
    ```bash
    python manage.py runserver
   
8. **Navigate to <code>http://127.0.0.1:8000/</code> in your browser.**

## 🛠️ Django site admin
**Navigate to <code>http://127.0.0.1:8000/admin/</code> in your browser.**

***To log in, please use the previously created credentials:***

****The "broken" site admin interface is caused by static files not being served locally when <code>DEBUG = False</code>. Such behavior is expected. <code>DEBUG</code> is set to <code>False</code> due to the exam requirement to develop a custom user-facing "404" page.****
