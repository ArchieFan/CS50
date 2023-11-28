from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering image x=0, y=70, w=0
        self.image("./shirtificate.png", 0, 70, 0)
        # Setting font: helvetica Bold 48
        self.set_font("helvetica", "B", 48)
        # “CS50 Shirtificate” as text, centered horizontally.
        # Printing title:
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        # set x = 0
        self.set_x(0)
        # Performing a line break:
        #self.ln(20)

def shirt(s):
    pdf = PDF()
    # The orientation of the PDF should be Portrait and The format of the PDF should be A4
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    # #set color to white
    pdf.set_text_color(255,255,255)
    #pdf.set_text_color(255,0,0)
    pdf.cell(0, 250, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    shirt(name)

if __name__ == "__main__":
    main()
