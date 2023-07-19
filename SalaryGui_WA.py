"""
SalaryGui_WA.py
Author - William Alguera - 07/19/23
Final Python Project - GUI implementation of a Salary calculator 
"""

#imports
from breezypythongui import EasyFrame
from tkinter.font import Font


#Salary class
class SalaryGui(EasyFrame):
    #class constructor method

    def __init__(self):
        EasyFrame.__init__(self, background="#09625F", width=350, height=250, title="Salary Calculator")
        #ui elements 
        #text - #002826
        #bg - #09625F
        #labelbg - #005C59
        #btn - #004845




        #title --- row 0//col 0 // colspan 2
        self.addLabel(text="Salary Calculator",  background="#005C59", foreground="#002826", row=0, column=0, font=Font(family="Monospace",size= 20),columnspan=2, sticky="NSEW")

    #Hourly Wage Input --- row 1//col 0 // colspan #
        self.addLabel(text="Hourly Wage:",  background="#005C59", foreground="#002826", row=1, column=0,sticky="we",font=Font(family="Monospace",size= 10))
        self.hourly = self.addFloatField(row=1, column=1, value=0, state="normal",sticky="w", width=6)

     #Hours worked in week input --- row2 // col 0 // colspan #
        self.addLabel(text="Hours worked this week:",  background="#005C59", foreground="#002826", row=2, column=0,sticky="we",font=Font(family="Monospace",size= 10))
        self.eowhrs = self.addFloatField(row=2, column=1, value=0, state="normal",sticky="w", width=6)
        self.eowhrs["validate"] ="focusout"
        

    #button --- row 3 // col 0 // colspan 2
        submitBtn = self.addButton(text="Submit Payroll", row=3,column=0, columnspan=2, command=self.runpayroll)
        submitBtn["background"] = "#005956"
        submitBtn["fg"] = "#002826"
        submitBtn["activebackground"] = "#005956"
        submitBtn["activeforeground"] = "#763A00"
        submitBtn["font"] = 8

    #results -- row 4 // col 0 // colspan # -- width set to zero to self adjust for larger number self adjustment
        self.addLabel(text="Employee's salary is: ",  background="#005C59", foreground="#002826", row=4, column=0,sticky="we",font=Font(family="Monospace",size= 10))
        self.payroll = self.addFloatField(row=4, column=1, value=0, state="readonly",sticky="w", width=0)
        self.payroll["readonlybackground"] = "#005C59"
        self.payroll["foreground"] = "#002826"
    #Logic processing
    def runpayroll(self):
        try:
            rate= self.hourly.getNumber()
            hours = self.eowhrs.getNumber()
            result = rate * hours 
            self.payroll.setValue(result)
        except ValueError:
            self.messageBox(title= "ERROR", message="INVALID ENTRY: Please enter HOUR(s) as a number")

#Run 
def main():
    #main run funcition
    SalaryGui().mainloop()

if __name__ == "__main__":
    main()