from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer, HRFlowable
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
import datetime

# --- Cores ---
VERDE_ESCURO  = colors.HexColor("#1a6b3c")
VERDE_CLARO   = colors.HexColor("#e8f5ee")
CINZA_CLARO   = colors.HexColor("#f7f7f7")
CINZA_TEXTO   = colors.HexColor("#555555")
BRANCO        = colors.white
PRETO         = colors.HexColor("#1a1a1a")

# --- Estilos ---
styles = getSampleStyleSheet()

estilo_empresa = ParagraphStyle(
    "empresa",
    fontSize=22,
    fontName="Helvetica-Bold",
    textColor=VERDE_ESCURO,
    alignment=TA_CENTER,
    spaceAfter=2,
)
estilo_subtitulo = ParagraphStyle(
    "subtitulo",
    fontSize=9,
    fontName="Helvetica",
    textColor=CINZA_TEXTO,
    alignment=TA_CENTER,
    spaceAfter=2,
)
estilo_secao = ParagraphStyle(
    "secao",
    fontSize=10,
    fontName="Helvetica-Bold",
    textColor=VERDE_ESCURO,
    spaceAfter=4,
)
estilo_info = ParagraphStyle(
    "info",
    fontSize=9,
    fontName="Helvetica",
    textColor=CINZA_TEXTO,
    leading=14,
)
estilo_rodape = ParagraphStyle(
    "rodape",
    fontSize=8,
    fontName="Helvetica",
    textColor=CINZA_TEXTO,
    alignment=TA_CENTER,
)

# --- Documento ---
pdf = SimpleDocTemplate(
    "recibo.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
)

story = []

# --- Cabeçalho ---
story.append(Paragraph("Plataforma de Aprendizado em Tecnologia", estilo_subtitulo))
story.append(Paragraph("contato@strayb.org  |  www.strayb.org", estilo_subtitulo))
story.append(Spacer(1, 0.3*cm))
story.append(HRFlowable(width="100%", thickness=2, color=VERDE_ESCURO))
story.append(Spacer(1, 0.4*cm))

# --- Título do recibo + número ---
titulo_tabela = Table(
    [[Paragraph("<b>RECIBO DE PAGAMENTO</b>", ParagraphStyle("t", fontSize=13, fontName="Helvetica-Bold", textColor=PRETO)),
      Paragraph(f"<b>Nº 2024-0042</b>", ParagraphStyle("n", fontSize=10, fontName="Helvetica-Bold", textColor=VERDE_ESCURO, alignment=TA_RIGHT))]],
    colWidths=["70%", "30%"],
)
titulo_tabela.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE")]))
story.append(titulo_tabela)
story.append(Spacer(1, 0.4*cm))

# --- Info do cliente ---
hoje = datetime.date.today().strftime("%d/%m/%Y")
info_dados = [
    ["Cliente:", "Rahul Sharma"],
    ["E-mail:", "rahul.sharma@email.com"],
    ["Data de emissão:", hoje],
    ["Forma de pagamento:", "Cartão de Crédito"],
]
tabela_info = Table(info_dados, colWidths=[4*cm, None])
tabela_info.setStyle(TableStyle([
    ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTNAME", (1,0), (1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("TEXTCOLOR", (0,0), (0,-1), CINZA_TEXTO),
    ("TEXTCOLOR", (1,0), (1,-1), PRETO),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("TOPPADDING", (0,0), (-1,-1), 3),
]))
story.append(tabela_info)
story.append(Spacer(1, 0.6*cm))

# --- Tabela de itens ---
story.append(Paragraph("Itens Adquiridos", estilo_secao))

DADOS = [
    ["Data", "Descrição", "Modalidade", "Valor (R$)"],
    ["16/11/2020", "Desenvolvimento Full Stack\ncom React & Node JS — Ao Vivo", "Vitalício", "R$ 10.999,00"],
    ["16/11/2020", "Classes\nSessões ao Vivo", "6 meses", "R$ 9.999,00"],
]

tabela = Table(DADOS, colWidths=[2.5*cm, None, 3*cm, 3*cm])
tabela.setStyle(TableStyle([
    # Cabeçalho
    ("BACKGROUND",   (0,0), (-1,0), VERDE_ESCURO),
    ("TEXTCOLOR",    (0,0), (-1,0), BRANCO),
    ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",     (0,0), (-1,0), 9),
    ("ALIGN",        (0,0), (-1,0), "CENTER"),
    ("BOTTOMPADDING",(0,0), (-1,0), 8),
    ("TOPPADDING",   (0,0), (-1,0), 8),
    # Linhas de dados
    ("BACKGROUND",   (0,1), (-1,1), BRANCO),
    ("BACKGROUND",   (0,2), (-1,2), VERDE_CLARO),
    ("FONTNAME",     (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",     (0,1), (-1,-1), 9),
    ("TEXTCOLOR",    (0,1), (-1,-1), PRETO),
    ("ALIGN",        (0,1), (0,-1), "CENTER"),
    ("ALIGN",        (2,1), (3,-1), "CENTER"),
    ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
    ("BOTTOMPADDING",(0,1), (-1,-1), 8),
    ("TOPPADDING",   (0,1), (-1,-1), 8),
    ("LEFTPADDING",  (1,0), (1,-1), 8),
    # Bordas
    ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
    ("LINEBELOW",    (0,0), (-1,-1), 0.5, colors.HexColor("#dddddd")),
    ("LINEAFTER",    (0,0), (-1,-1), 0.5, colors.HexColor("#dddddd")),
]))
story.append(tabela)
story.append(Spacer(1, 0.3*cm))

# --- Totais ---
dados_total = [
    ["Subtotal",  "R$ 20.998,00"],
    ["Desconto",  "– R$ 3.000,00"],
    ["TOTAL",     "R$ 17.998,00"],
]
tabela_total = Table(dados_total, colWidths=[None, 3.8*cm], hAlign="RIGHT")
tabela_total.setStyle(TableStyle([
    ("FONTNAME",     (0,0), (-1,1), "Helvetica"),
    ("FONTNAME",     (0,2), (-1,2), "Helvetica-Bold"),
    ("FONTSIZE",     (0,0), (-1,1), 9),
    ("FONTSIZE",     (0,2), (-1,2), 11),
    ("TEXTCOLOR",    (0,0), (-1,1), CINZA_TEXTO),
    ("TEXTCOLOR",    (0,2), (-1,2), VERDE_ESCURO),
    ("ALIGN",        (0,0), (-1,-1), "RIGHT"),
    ("BOTTOMPADDING",(0,0), (-1,-1), 5),
    ("TOPPADDING",   (0,0), (-1,-1), 5),
    ("LINEABOVE",    (0,2), (-1,2), 1.5, VERDE_ESCURO),
    ("BACKGROUND",   (0,2), (-1,2), VERDE_CLARO),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
]))
story.append(tabela_total)
story.append(Spacer(1, 0.8*cm))

# --- Rodapé ---
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc")))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Obrigado pela sua compra! Em caso de dúvidas, entre em contato pelo e-mail contato@strayb.org.", estilo_rodape))
story.append(Paragraph("Este documento é um comprovante de pagamento válido.", estilo_rodape))

pdf.build(story)
print("PDF gerado: recibo.pdf")