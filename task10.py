class Document:
    def print_preview(self):
        return "Generic print preview"

class WordDocument(Document):
    def print_preview(self):
        return "Word document preview with formatting"

class PdfDocument(Document):
    def print_preview(self):
        return "PDF preview - read-only view"

docs = [WordDocument(), PdfDocument()]
for doc in docs:
    print(doc.print_preview())