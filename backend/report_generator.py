# report_generator.py
import reportlab.platypus
import reportlab.lib.styles
import os

def generate_pdf(report_text: str, filename: str = 'report.pdf'):
    try:
        import importlib
        platypus = importlib.import_module('reportlab.platypus')
        lib_styles = importlib.import_module('reportlab.lib.styles')
        SimpleDocTemplate = platypus.SimpleDocTemplate
        Paragraph = platypus.Paragraph
        Spacer = platypus.Spacer
        getSampleStyleSheet = lib_styles.getSampleStyleSheet
    except ImportError as e:
        raise ImportError(
            "The 'reportlab' package is required to generate PDFs. "
            "Install it with: pip install reportlab"
        ) from e

    styles = getSampleStyleSheet()
    os.makedirs("reports", exist_ok=True)
    filepath = os.path.join("reports", filename)
    doc = SimpleDocTemplate(filepath)
    flow = []
    for line in report_text.split('\n'):
        # ensure Paragraph has at least a space for empty lines
        flow.append(Paragraph(line or ' ', styles['Normal']))
        flow.append(Spacer(1, 6))
    doc.build(flow)
    return filename