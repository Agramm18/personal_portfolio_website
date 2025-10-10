from django.shortcuts import render, redirect
import mysql.connector
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
from urllib.parse import quote, urlencode
import pycountry

load_dotenv()

def contact_form_view(request):

    ##create redirect link to glassdor
    if request.method == "POST":
        try:
            salary = request.POST.get("salary", 0)
            job_title = request.POST.get("job_title", "")
            location_country = request.POST.get("location_country", "")
            experience_level = request.POST.get("experience_level", "")

            #Build URL for Google
            values = quote(f"{experience_level} {job_title} {location_country} average salary")
            google_url = f"https://www.google.com/search?q={values}"

            #Check if salary is less than 50k
            #If thats the case the recruier will redirected to glassdor
            float_salary = float(salary)
            if float_salary < 50000:
                return redirect(google_url) 

        except Exception as e:
            print("Error detected", e)

    #################################################################################################
    #Database Logic
    if request.method == "POST":
        try:
            #recruiter-info

            lname = request.POST.get("lname")
            gender = request.POST.get("gender")
            email = request.POST.get("email")
            phone = request.POST.get("tel-number")

            #compnay-info

            compnay_name = request.POST.get("company-name")
            company_url = request.POST.get("website")
            company_mail = request.POST.get("company_email")
            company_phone = request.POST.get("company-phone")

            #other-infos

            gdbpr_value = request.POST.get("gdpr")


            if not all([lname, gender, email, phone, compnay_name, company_url, company_mail, company_phone, gdbpr_value]):
                raise ValueError("This field is empty or no data where transmittet please try again")
        
        except ValueError as e:
            print("There is an Value error in the contact form POST")
            print(e)
        
        except Exception as error:
            print("an error where detected in the contact POST")
            print(error)

        sql_server = mysql.connector.connect (
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            port=3306,
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        cur = sql_server.cursor()

        #put the data in the SQL_TABLE
        sql = """
        INSERT INTO contactform 
        (lname, gender, email, phone, company_name, company_url, company_email, company_phone, gdpr_value, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """

        values = (
            lname,
            gender,
            email,
            phone,
            compnay_name,
            company_url,
            company_mail,
            company_phone,
            gdbpr_value
        )

        cur.execute(sql, values)
        print("All data where transmittet for the database")
        sql_server.commit()
        cur.close()

    ######################################################
    #email_logic

    if request.method == "POST":
        try:
            #Get the dataf from the contact form via POST.get

            #Form sections
            #recruiter-info
            position = request.POST.get("position")
            gender = request.POST.get("gender")
            additional_title = request.POST.get("additional-title")
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("email")
            phone = request.POST.get("tel-number")

            #compnay-info
            compnay_name = request.POST.get("company-name")
            company_url = request.POST.get("website")
            company_mail = request.POST.get("company_email")
            company_phone = request.POST.get("company-phone")
            company_address = request.POST.get("company_address")
            company_industry = request.POST.get("company_industry")
            

            #job-info
            job_title = request.POST.get("job_title")
            location_country = request.POST.get("location_country")
            location_city = request.POST.get("location_city")
            experience_level = request.POST.get("experience_level")
            tasks = request.POST.get("tasks")
            yearly_gross_salary = request.POST.get("salary")


            #other-infos
            additional_information = request.POST.get("other_infos")
            gdbpr_value = request.POST.get("gdpr")

            #check if data exsist
            if not all([
                position, gender, additional_title, fname, lname, email, phone,
                compnay_name, company_url, company_mail, company_phone, company_industry, company_address,
                job_title, location_country, location_city, experience_level, tasks, yearly_gross_salary,
                additional_information, gdbpr_value
            ]):
                raise ValueError("No input where submittet for the email please try again")
                
            else:
                sender_email = os.getenv("SMTP_SENDER_EMAIL")
                reciver_email = os.getenv("SMTP_SENDER_EMAIL")
                app_pwsd = os.getenv("EMAIL_APP_PASSWORD")

                msg = EmailMessage()
                msg["Subject"] = f"New job offer from {compnay_name} the email_adress is: {email} or {company_mail}"
                msg["From"] = sender_email
                msg["To"] = reciver_email
                msg["Reply-To"] = email

                msg.set_content(f"""
                Hello Alex, 

                you have received a new job offer from your website.

                The following person has contacted you:
                {gender} {additional_title} {fname} {lname}

                You can reach this person via:
                Email: {email}
                Phone: {phone}
                Position in the company: {position}

                --- Company Information ---
                Name: {compnay_name}
                Website: {company_url}
                Address: {company_address}
                Industry: {company_industry}
                Contact: {company_mail}, {company_phone}

                --- Job Offer Details ---
                Job Title: {job_title}
                Location: {location_city}, {location_country}
                Experience Level: {experience_level}
                Tasks: {tasks}
                Yearly Gross Salary: {yearly_gross_salary}

                --- Additional Information ---
                {additional_information}
                GDPR Consent: {gdbpr_value} (yes/no)

                Please make sure to respond to this person.  
                Good luck, and thank you!
                """)

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, app_pwsd)
                    server.send_message(msg)
                    return redirect("thankyou")

        except ValueError as e:
            print("There is an error in the POST for the email please try again")
            print("The error is: ", e)

    return render(request, "contactform.html")

def thankyou(request):
    return render(request, "thankyou.html")