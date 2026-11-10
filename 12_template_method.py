class Report:
    # Template method: define el orden, no se sobreescribe
    def generate(self, data: dict) -> str:
        parts = [self.header(data), self.body(data), self.footer(data)]
        return "\n".join(parts)

    def header(self, data): raise NotImplementedError
    def body(self, data): raise NotImplementedError
    def footer(self, data): raise NotImplementedError


class TextReport(Report):
    def header(self, data): return f"=== {data['title']} ==="
    def body(self, data): return data['content']
    def footer(self, data): return f"-- Generado por {data['author']} --"


class HTMLReport(Report):
    def header(self, data): return f"<h1>{data['title']}</h1>"
    def body(self, data): return f"<p>{data['content']}</p>"
    def footer(self, data): return f"<footer>{data['author']}</footer>"


data = {"title": "Ventas Q4", "content": "Crecimos 12%", "author": "C. Sierra"}
print(TextReport().generate(data))
print()
print(HTMLReport().generate(data))
