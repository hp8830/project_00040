from fpdf import FPDF

class PdfReport: 
    """
        Creates a pdf file that contains data about flatmates such as flatmate names and due amount and period of bill 
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, flatmate3, bill):
        # save FPDF() class into a 
        # variable pdf
        bill_pdf = FPDF(orientation='P', unit='pt', format='A4')

        # Add a page to the PDF 
        bill_pdf.add_page()

        # Add Icon 
       

        # Add a title
        bill_pdf.set_font(family='Arial', size=24, style= 'B')
        bill_pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        bill_pdf.image("C:/portfolio_2022/python/project_00040/files/house.png", w=30, h=30)

        bill_pdf.set_font(family='Arial', size=14, style='B')
        bill_pdf.cell(w=100, h=40,txt="Period: ", border=0)
        bill_pdf.cell(w=150, h=40,txt=bill.period, border=0, ln=1)
        #Name and due amount of flatmates 
        bill_pdf.cell(w=100, h=40,txt=flatmate1.name, border=0)
        bill_pdf.cell(w=150, h=40,txt=str(round(flatmate1.pays(bill,flatmate2, flatmate3),2)), border=0, ln=1)
        #Name and due amount of flatmates 
        bill_pdf.cell(w=100, h=40,txt=flatmate2.name, border=0)
        bill_pdf.cell(w=150, h=40,txt=str(round(flatmate2.pays(bill,flatmate1, flatmate3),2)), border=0, ln=1)
        #Name and due amount of flatmates 
        bill_pdf.cell(w=100, h=40,txt=flatmate3.name, border=0)
        bill_pdf.cell(w=150, h=40,txt=str(round(flatmate3.pays(bill,flatmate2, flatmate1),2)), border=0, ln=1)


        bill_pdf.output(self.filename)