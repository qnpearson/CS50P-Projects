from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica","B",30)
        self.cell(0, 60, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
        self.image("shirtificate.png", h=self.eph, w=self.epw)
        self.text(x=62, y=145, txt=f"{name} took CS50")

    def make_pdf(self, name):
        self.output(name)

shirtificate = Shirtificate(input("Name: "))
shirtificate.make_pdf("shirtificate.pdf")