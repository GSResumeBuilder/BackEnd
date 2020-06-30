import resume_builder
from flask import *
from flask import request
from flask_cors import CORS
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
@app.route('/', methods = ['POST'])

def personal():
	data = request.get_json()
	f_name = data['first_name']
	l_name = data['last_name']
	year = data['year_of_study']
	dob =data['dob']
	email = data['email_id']
	enrollment = data['enrollment_no']
	department = data['branch']
	gender = "Male" if data['gender'] == "M" else "Female"
	specialization = "None"
	mobile = data['phone_no']

	name = f_name + " " + l_name

	grad_year = data['grad_year']
	grad_cgpa = data['grad_cgpa']

	high_school = data['high_school']
	high_school_year = data['high_school_year']
	high_school_board = data['high_school_board']
	high_school_institute = data['high_school_institute']
	high_school_cgpa = data['high_school_cgpa']

	secondary_school_year = data['secondary_school_year']
	secondary_school_board = data['secondary_school_board']
	secondary_school_cgpa = data['secondary_school_cgpa']
	secondary_school_institute = data['secondary_school_institute']

	scholastic_achievements = data['scholastic_achievements']

	projects = data['projects']

	work_exp = data['work_experience']

	position_of_responsibility = data['positions']

	extra_curricular = data['extracurricular']

	operating_systems = data['platforms_os']
	programming_skills = data['platforms_ps']
	web_designing = data['platforms_wd']
	software_skills = data['platforms_ss']
	core_subject = data['courses_core']
	depth_subject = data['courses_depth']

	print(name,year,dob,email,enrollment,department,gender,specialization,mobile,grad_year, grad_cgpa, high_school, high_school_year, high_school_board, high_school_institute, high_school_cgpa, secondary_school_year, secondary_school_board, secondary_school_institute, secondary_school_cgpa,scholastic_achievements,projects,work_exp,position_of_responsibility,extra_curricular,operating_systems,programming_skills,web_designing,software_skills,core_subject,depth_subject)
	resume_builder.personalInformation(name,year,dob,email,enrollment,department,gender,specialization,mobile,grad_year, grad_cgpa, high_school, high_school_year, high_school_board, high_school_institute, high_school_cgpa, secondary_school_year, secondary_school_board, secondary_school_institute, secondary_school_cgpa,scholastic_achievements,projects,work_exp,position_of_responsibility,extra_curricular,operating_systems,programming_skills,web_designing,software_skills,core_subject,depth_subject)

	return "DONE"


if __name__ == '__main__':
	app.run()
