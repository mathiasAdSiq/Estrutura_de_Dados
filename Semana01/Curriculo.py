# -*- coding: utf-8 -*-
from fpdf import FPDF

resume_data = {
    "name": "Mathias Almeida de Siqueira",
    "linkedin": "https://www.linkedin.com/in/mathias-almeida-de-siqueira-875779417/",
    "github": "https://github.com/mathiasAdSiq",
    "email": "mathias.adsiqueira@gmail.com",
    "mobile": "+55 55 991624554",
    "summary": "Sou Mathias Almeida de Siqueira, de São João do Polêsine RS, 18 anos e venho construindo a minha trajetória na área de Analista de IA. Cursando Sistemas de informação na Faculdade Antônio Meneghetti."
    "Ao longo do caminho, já vivi experiências que me ajudaram a crescer, como 3 meses trabalhando como Garçom em um restaurante, com atendimento ao público. Entre os meus pontos fortes estão Trabalho em equipe, Pontualidade e Entender as coisas de maneira rápida."
    ,
    "skills": [
        ("Language:", "Python"),
        ("General:", "Clean Code"),

    ],
    "experience": [
        {
            "role": "Garcon",
            "company": "Restaurante Dipaolo",
            "location": "Restinga Seca - Brasil",
            "period": "Fevereiro 2026 - Marco 2026",
            "points": [
                "Tive a oportunidade de ter o meu primeiro emprego formal em um restaurante,"
                " onde aprendi varias ensinamentos.",
            ],
            "context": "Eu trabalei no Restaurante Dipaolo, Brasil,."
        },
        {
            "role": "Bolsista do Projeto Cultivando",
            "company": "Antonio Meneghetti College",
            "location": "Restinga Sêca - Brazil",
            "period": "Ago 2026 - Current",
            "points": [
                "O Projeto cultivando é outra etapa de aprendizado na minha carreira, que resultara em uma melhora .    " 
                ],
        },
        
    ],

    "education": [

        {
            "institution": "Antonio Meneghetti College",
            "degree": "Bachelor's degree",
            "field": "Sistemas de Informação",
            "period": "mar 2026 - Dec 2030"
        }
    ],


}


class ResumePDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(20, 10, 20)
        self.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
        self.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)

    def add_section_title(self, title):
        self.set_font("DejaVu", "B", 12)
        self.cell(0, 8, title, ln=True, align="L")
        self.line(self.get_x(), self.get_y(), self.get_x() + 170, self.get_y())
        self.ln(4)

    def add_header(self, data):
        self.set_font("DejaVu", "B", 22)
        self.cell(0, 10, data["name"], ln=True, align="L")
        self.ln(2)
        self.set_font("DejaVu", "", 9)
        self.cell(80, 5, f"LinkedIn: {data['linkedin']}")
        self.cell(0, 5, f"Email: {data['email']}", ln=True, align="R")
        self.cell(80, 5, f"GitHub: {data['github']}")
        self.cell(0, 5, f"Mobile: {data['mobile']}", ln=True, align="R")
        self.ln(6)

    def add_summary(self, summary_text):
        self.add_section_title("Summary")
        self.set_font("DejaVu", "", 10)
        self.multi_cell(0, 5, summary_text, align='J')
        self.ln(4)

    def add_skills(self, skills):
        self.add_section_title("Skills")
        category_col_width = 45
        line_height = 6
        for category, skill_list in skills:
            y_before_line = self.get_y()
            self.set_font("DejaVu", "B", 10)
            self.multi_cell(category_col_width, line_height, f"• {category}", align='L')
            y_after_category = self.get_y()
            self.set_xy(self.l_margin + category_col_width, y_before_line)
            self.set_font("DejaVu", "", 10)
            self.multi_cell(0, line_height, skill_list, align='L')
            self.set_y(max(y_after_category, self.get_y()))
            self.ln(1)
        self.ln(4)

    def add_experience(self, experiences):
        self.add_section_title("Experience")
        for job in experiences:
            self.set_font("DejaVu", "B", 11)
            self.cell(0, 6, job["role"], ln=True)
            self.set_font("DejaVu", "B", 10)
            self.cell(85, 6, job["company"])
            self.set_font("DejaVu", "", 10)
            self.cell(85, 6, job["location"] + " " + job["period"], ln=True, align="R")
            self.ln(2)
            for point in job["points"]:
                self.cell(6, 5, "•")
                self.multi_cell(0, 5, point, align='J')
                self.ln(1)
            self.set_font("DejaVu", "B", 10)
            self.cell(0, 5, "Context:", ln=True)
            self.set_font("DejaVu", "", 10)
            self.multi_cell(0, 5, job["context"], align='J')
            self.ln(7)

    def add_education(self, educations):
        self.add_section_title("Education")
        for edu in educations:
            self.set_font("DejaVu", "B", 11)
            self.cell(85, 6, edu["institution"])
            self.set_font("DejaVu", "", 10)
            self.cell(85, 6, edu["degree"], align="R", ln=True)
            self.set_font("DejaVu", "", 10)
            self.cell(85, 6, edu["field"])
            self.cell(85, 6, edu["period"], align="R", ln=True)
            self.ln(3)

    def add_simple_section(self, title, items):
        self.add_section_title(title)
        date_width = 40
        for item in items:
            y_start = self.get_y()
            title_width = self.w - self.l_margin - self.r_margin - date_width
            self.set_font("DejaVu", "B", 10)
            self.multi_cell(title_width, 6, item["title"], align='J')
            y_after_title = self.get_y()
            self.set_xy(self.l_margin + title_width, y_start)
            self.set_font("DejaVu", "", 10)
            self.cell(date_width, 6, item["period"], align="R")
            self.set_y(y_after_title)
            self.ln(1)
            self.set_font("DejaVu", "", 9)
            self.multi_cell(0, 5, item.get("description", ""), align='J')
            self.ln(3)

    def add_certifications(self, certifications):
        self.add_section_title("Certifications")
        for cert, date in certifications:
            self.set_font("DejaVu", "", 10)
            self.cell(85, 6, cert)
            self.cell(85, 6, date, align="R", ln=True)
        self.ln(3)

    def add_volunteering(self, volunteering):
        self.add_section_title("Volunteering")
        for item in volunteering:
            self.set_font("DejaVu", "B", 10)
            self.cell(85, 6, item["role"])
            self.set_font("DejaVu", "", 10)
            self.cell(85, 6, item["period"], align="R", ln=True)
            self.set_font("DejaVu", "", 9)
            self.multi_cell(0, 5, item["description"], align='J')
            self.ln(3)


try:
    pdf = ResumePDF()
    pdf.add_page()

    pdf.add_header(resume_data)
    pdf.add_summary(resume_data["summary"])

    if resume_data.get("skills"):
        pdf.add_skills(resume_data["skills"])

    if resume_data.get("experience"):
        pdf.add_experience(resume_data["experience"])

    if resume_data.get("education"):
        pdf.add_education(resume_data["education"])

    if resume_data.get("talks"):
        pdf.add_simple_section("Talks", resume_data["talks"])

    if resume_data.get("publications"):
        pdf.add_simple_section("Publications", resume_data["publications"])

    if resume_data.get("certifications"):
        pdf.add_certifications(resume_data["certifications"])

    if resume_data.get("volunteering"):
        pdf.add_volunteering(resume_data["volunteering"])

    output_filename = "Augusto_Gehrke_CV.pdf"
    pdf.output(output_filename)

    print(f"Sucesso! O currículo atualizado foi salvo como '{output_filename}'")

except FileNotFoundError:
    print("\nERRO: Arquivos de fonte DejaVu ('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf') não encontrados.")
    print("Baixe-os de https://www.fontsquirrel.com/fonts/dejavu-sans e coloque na mesma pasta do script.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")
