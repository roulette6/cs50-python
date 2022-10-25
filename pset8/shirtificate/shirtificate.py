from fpdf import FPDF


def main():

    name = input("Name: ")

    # A4 = is 210mm wide by 297mm tall
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", size=48)

    # default margin is 1 cm, so make cell
    # width page width - 10
    pdf.cell(w=200, h=50, txt="CS550 Shirtificate", align="C")

    # insert centered image
    # x = (page_width - image_width) / 2
    # y = page_heigh - image_height / 2
    pdf.image("./shirtificate.png", x=25, y=68.5, w=160, h=160)

    # overlay student name
    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(115)
    pdf.cell(w=190, txt=f"{name} took CS50", align="C")

    # create PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
