function errorHandeling() {
    try {
        //Collect data from contact form

        //Recruiter
        const position = document.getElementById("position");
        const gender = document.getElementById("gender");
        const additionalTitle = document.getElementById("additional-title");
        const fname = document.getElementById("fname");
        const lname = document.getElementById("lname");
        const recruiterEmail = document.getElementById("email");
        const recruiterPhone = document.getElementById("tel-number");

        //Company
        const companyName = document.getElementById("company-name");
        const companyWebsite = document.getElementById("website");
        const companyEmail = document.getElementById("company_email");
        const companyPhone = document.getElementById("company-phone");
        const companyAdress = document.getElementById("company-address");
        const companyIndustry = document.getElementById("company-industry");

        //Job
        const jobTitle = document.getElementById("job-title");
        const jobLocationCountry = document.getElementById("location-country");
        const jobLocationCity = document.getElementById("location-city");
        const jobExperienceLevel = document.getElementById("experience-level");
        const jobTasks = document.getElementById("tasks");
        const jobSalary = document.getElementById("salary");

        //Other
        const additionalInformation = document.getElementById("other-infos");
        const gdprValue = document.getElementById("gdpr");

        //Check the form fields by category
        //.value.trim() to check actuall content not DOOM Element
        if (!companyName.value.trim() || !companyWebsite.value.trim() || !companyAdress.value.trim() || !companyIndustry.value.trim()) {
            throw new Error("There is an empty field at the Company infos");
        } else if (!position.value.trim() || !gender.value.trim() || !additionalTitle.value.trim() || !fname.value.trim() || !lname.value.trim() || !recruiterEmail.value.trim() || !recruiterPhone.value.trim()) {
            throw new Error("There is an empty field at the Personal/Recruiter infos");
        } else if (!jobTitle.value.trim() || !jobLocationCountry.value.trim() || !jobLocationCity.value.trim() || !jobExperienceLevel.value.trim() || !jobTasks.value.trim() || !jobSalary.value.trim()) {
            throw new Error("There is an empty or wrong field at the Job information");
        }

        //Check every form field
        else if (!position.value.trim()) {
            throw new Error("Please select the position to continue");
        } else if (!gender.value.trim()) {
            throw new Error("Please select the gender to continue");
        } else if (!additionalTitle.value.trim()) {
            throw new Error("Please select an additional title to continue");
        } else if (!fname.value.trim()) {
            throw new Error("Please type in your first name to continue");
        } else if (!lname.value.trim()) {
            throw new Error("Please type in your last name to continue");
        } else if (!recruiterEmail.value.trim()) {
            throw new Error("Please type in your email adress to continue");
        } else if (!recruiterPhone.value.trim()) {
            throw new Error("Please type in your phone number to continue");
        } else if (!companyName.value.trim()) {
            throw new Error("Please type in the name from your company to continue");
        } else if (!companyWebsite.value.trim()) {
            throw new Error("Please type in the URL from your website to continue or atleast a link to your socials");
        } else if (!companyAdress.value.trim()) {
            throw new Error("Please type in the addres from your Company");
        } else if (!companyIndustry.value.trim()) {
            throw new Error("Please type in the addres from your company");
        } else if (!jobTitle.value.trim()) {
            throw new Error("Please type in the job title to continue");
        } else if (!jobLocationCountry.value.trim()) {
            throw new Error("Please type in where the joblocation is (COuntry) to continue");
        } else if (!jobLocationCity.value.trim()) {
            throw new Error("Please type in where the joblocation is (City) to continue");
        } else if (!jobExperienceLevel.value.trim()) {
            throw new Error("Please type in the experience level from the job");
        } else if (!jobTasks.value.trim()) {
            throw new Error("Please type in the task from the job so i know what i do there to continue");
        } else if (!jobSalary.value.trim()) {
            throw new Error("Please type in the yearly gross salary to continue");
        } else if (parseFloat(jobSalary.value) < 50000) {
            
            //convert Values to URL format
            const jobCityURL = jobLocationCity.value.toLowerCase().replace(/\s+/g, "-");
            const jobCountryURL = jobLocationCountry.value.toLowerCase().replace(/\s+/g, "-");
            const jobTitleURL = jobTitle.value.toLowerCase().replace(/\s+/g, "-");

            //Open a new tab in kunu with the anual salary of a software developer if the salary is under 50k
            if (confirm("The entered salary seems to be below the market average. Please enter a value above €50,000. I will open a new tab showing an official website with annual software developer salaries in Switzerland, Germany, and Austria."))
                window.open(`www.glassdoor.com/Salaries/${jobTitleURL}-salary-SRCH_KO0,18.htm&ved=2ahUKEwio5rz38ZeQAxWnBdsEHcBVFK0QFnoECCAQAQ&usg=AOvVaw03KGqtkSBz6Ha18LsOB03Y`);
            return;

        } else if (!gdprValue.checked) //Checked to check if cheked 
        {
            throw new Error("Please select if you agree to my GDPR");
        } else {
            throw new Error("An unexpected error happend please try again");
        }

    } catch (error) {
        console.error("", error.message);
        alert("" + error.message);
    }
}
submitBTN = document.getElementById("submit")

submitBTN.addEventListener("click", (event) => {
    event.preventDefault();
    errorHandeling();
});
