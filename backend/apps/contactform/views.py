from django.shortcuts import render
import mysql.connector
import os


def contact_form_view(request):

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
        print("All data where transmittet")
        sql_server.commit()
        cur.close()

    return render(request, "contactform.html")
