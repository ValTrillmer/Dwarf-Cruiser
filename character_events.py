import random
from name_data import male_given
from name_data import female_given
from name_data import surname

#character stories are formed by the vevents of their lives

class event:
	def generate(self):
		pass

class birth(event):
	def __init__(self, m_given, m_sur, f_given, f_sur, sex, given, sur):
		event.__init__(self)
		self.m_given = m_given
		self.m_sur = m_sur
		self.f_given = f_given
		self.f_sur = f_sur
		self.sex = sex
		self.given = given
		self.sur = sur

	def __repr__(self):
		x = self.m_given+" "+self.m_sur
		y = self.f_given+" "+self.f_sur
		sex_dict = {0 : "girl", 1 : "boy"}
		s = sex_dict[self.sex]
		pronoun_dict = {0 : "her", 1 : "him"}
		pnoun = pronoun_dict[self.sex]
		n = self.given+" "+self.sur
		return "On Feb 1st, 2571, a baby "+s+" was born to "+x+" and "+y+". They named "+pnoun+" "+n+"."


	def generate(self):
		self.m_given = female_given[random.randint(0,len(female_given)-1)]
		self.m_sur = surname[random.randint(0,len(surname)-1)]
		self.f_given = male_given[random.randint(0,len(male_given)-1)]
		self.f_sur = surname[random.randint(0,len(surname)-1)]
		#0 = female; 1 = male
		self.sex = random.randint(0,1)
		if self.sex == 0:
			self.given = female_given[random.randint(0,len(female_given)-1)]
		else:
			self.given = male_given[random.randint(0,len(male_given)-1)]
		self.sur = self.f_sur