class college:
    student = 'Sachin'
    branch = 'CSE'
    sem = 6

    def __init__(self):
      print("The message is from constractor")
      
    def department(self,deptName):
        self.deptName = deptName
    
    def mianBranch(self):
      print(self.deptName)    
      
            
collegeObj = college()
#print(collegeObj.student+'is from '+collegeObj.branch+' and sem '+str (collegeObj.sem))

print(collegeObj.department("CSE,ISE,ECE"))
print(collegeObj.mianBranch())



