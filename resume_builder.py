from __future__ import print_function
import emailp
from mailmerge import MailMerge

template = "./resume_template.docx"
document = MailMerge(template)

def personalInformation(name,year,dob,email,enrollment,department,gender,specialization,mobile,graduationYear, graduationCgpa, twelfthOrDiploma, twelfthYear, twelfthBoard, twelfthSchool, twelfthCgpa, tenthYear, tenthBoard, tenthSchool, tenthCgpa, scholastic_achievements, projects, work_exp, position_of_responsibility, extra_curricular, operating_systems, programming_skills, web_designing, software_skills, core_subject, depth_subject) :
    template = "./resume_template.docx"
    document = MailMerge(template)
    document.merge(Name=name.title())
    document.merge(Year=year+" Year")
    document.merge(DOB=dob)
    document.merge(gmail=email)
    document.merge(enrollment=enrollment)
    document.merge(Department=department)
    document.merge(gender=gender)
    document.merge(specialization=specialization)
    document.merge(Mobile=mobile)

    document.merge(graduation_year=graduationYear)
    document.merge(graduation_cgpa=graduationCgpa)
    document.merge(twelfth_Diploma=twelfthOrDiploma)
    document.merge(twelfth_school=twelfthSchool)
    document.merge(twelfth_board=twelfthBoard)
    document.merge(twelfth_pass=twelfthYear)
    document.merge(twelfth_cgpa=twelfthCgpa)
    document.merge(tenth_school=tenthSchool)
    document.merge(tenth_board=tenthBoard)
    document.merge(tenth_pass=tenthYear)
    document.merge(tenth_cgpa=tenthCgpa)

    document.merge(operating_systems=", ".join(operating_systems))
    document.merge(programming_skills=", ".join(programming_skills))
    document.merge(web_designing=", ".join(web_designing))
    document.merge(software_skills=", ".join(software_skills))

    document.merge(core_subject="\n•   ".join(core_subject))
    document.merge(depth_subject="\n•   ".join(depth_subject))

    cust_2 = {
        'status': 'Silver',
        'city': 'Columbus',
        'phone_number': '800-555-5551',
        'Business': 'Fancy Pants',
        'zip': '55551',
        'purchases': '$250,000',
        'shipping_limit': '$2000',
        'state': 'OH',
        'address': '1234 Elm St',
        'discount': '2%',
        'recipient': 'Mrs. Smith'
    }
    document.merge(**cust_2)

    document.merge_rows('sa_description',scholastic_achievements)

    document.merge_rows('pro_description',projects)

    document.merge_rows('work_place',work_exp)

    document.merge_rows('pos_position',position_of_responsibility)

    document.merge_rows('ec_event',extra_curricular)

    filename=enrollment+"_"+name+".docx"

    document.write(filename)

    emailp.sendMail(email, filename)
