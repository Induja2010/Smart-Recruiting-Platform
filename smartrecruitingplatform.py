class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Role: {self.role}"


class Job:
    def __init__(self, title, description, department, location, employment_type, salary_range, deadline,
                 required_qualifications, preferred_qualifications, status):
        self.title = title
        self.description = description
        self.department = department
        self.location = location
        self.employment_type = employment_type
        self.salary_range = salary_range
        self.deadline = deadline
        self.required_qualifications = required_qualifications
        self.preferred_qualifications = preferred_qualifications
        self.status = status

    def __str__(self):
        return (f"Title: {self.title}\nDescription: {self.description}\nDepartment: {self.department}\n"
                f"Location: {self.location}\nEmployment Type: {self.employment_type}\n"
                f"Salary Range: {self.salary_range}\nApplication Deadline: {self.deadline}\n"
                f"Required Qualifications: {self.required_qualifications}\n"
                f"Preferred Qualifications: {self.preferred_qualifications}\nStatus: {self.status}")


class SmartRecruitingPlatform:
    def __init__(self):
        self.users = []
        self.jobs = []
        self.logged_in_user = None

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. User Management")
            print("2. Job Posting and Management")
            print("3. View Jobs")
            print("4. Exit")

            choice = input("Please select an option: ")

            if choice == '1':
                self.user_management()
            elif choice == '2':
                if self.logged_in_user and self.logged_in_user.role == "HR Manager":
                    self.job_posting_management()
                else:
                    print("Access Denied. Only HR Managers can access this feature.")
            elif choice == '3':
                self.view_jobs()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def user_management(self):
        print("\nUser Management:")
        print("1. Login")
        print("2. Sign Up")
        print("3. View Users (Admin Only)")

        choice = input("Please select an option: ")

        if choice == '1':
            self.login()
        elif choice == '2':
            self.sign_up()
        elif choice == '3':
            if self.logged_in_user and self.logged_in_user.role == "Admin":
                self.view_users()
            else:
                print("Access Denied. Only Admins can view users.")
        else:
            print("Invalid choice. Please try again.")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.email == email and user.password == password:
                self.logged_in_user = user
                print(f"Login successful! Welcome, {user.name}.")
                return

        print("Invalid email or password. Please try again.")

    def sign_up(self):
        name = input("Enter your full name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        role = input("Enter your role (Admin/HR Manager/Candidate): ")

        if role not in ["Admin", "HR Manager", "Candidate"]:
            print("Invalid role. Please select from Admin, HR Manager, or Candidate.")
            return

        new_user = User(name, email, password, role)
        self.users.append(new_user)
        print("Sign Up successful! You can now log in.")

    def view_users(self):
        print("\nRegistered Users:")
        for user in self.users:
            print(user)

    def job_posting_management(self):
        print("\nJob Posting and Management:")
        print("1. Create Job")
        print("2. View Jobs")
        print("3. Edit/Update Job")

        choice = input("Please select an option: ")

        if choice == '1':
            self.create_job()
        elif choice == '2':
            self.view_jobs()
        elif choice == '3':
            print("Edit/Update Job functionality is not implemented yet.")
        else:
            print("Invalid choice. Please try again.")

    def create_job(self):
        title = input("Enter the Job Title: ")
        description = input("Enter the Job Description: ")
        department = input("Enter the Department: ")
        location = input("Enter the Job Location: ")
        employment_type = input("Enter the Employment Type (Full-time/Part-time/Contract/Internship): ")
        salary_range = input("Enter the Salary Range (e.g., 50000-80000): ")
        deadline = input("Enter the Application Deadline (YYYY-MM-DD): ")
        required_qualifications = input("Enter Required Qualifications: ")
        preferred_qualifications = input("Enter Preferred Qualifications: ")

        print("\n1. Save as Draft")
        print("2. Publish")

        status_choice = input("Please select an option: ")
        status = "Draft" if status_choice == '1' else "Published"

        new_job = Job(title, description, department, location, employment_type, salary_range, deadline,
                      required_qualifications, preferred_qualifications, status)
        self.jobs.append(new_job)

        print(f"Job {status.lower()} successfully!")

    def view_jobs(self):
        print("\nJob Listings:")
        for job in self.jobs:
            if job.status == "Published":
                print(job)
                print("------------------------------")


if __name__ == "__main__":
    platform = SmartRecruitingPlatform()
    platform.main_menu()
