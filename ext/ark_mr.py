import ark
import markdown2

@ark.renderers.register('md')
def render_quarto(text):
    return markdown2.markdown(text,extras=["code-friendly","fenced-code-blocks"])
