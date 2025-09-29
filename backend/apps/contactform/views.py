from django.shortcuts import render
import mysql.connector
import os

def contact_form_view(request):

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


            if not all(lname, gender, email, phone, compnay_name, company_url, company_mail, company_phone, gdbpr_value):
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
                print("All data wehre submittet thank you for your message")

        except ValueError as e:
            print("There is an error in the POST for the email please try again")
            print("The error is: ", e)

    return render(request, "contactform.html")