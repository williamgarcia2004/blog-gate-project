import markdown, bleach

def render_markdown(text): 
    html = markdown.markdown(
        text, 
        extensions=[
            "markdown.extensions.extra",      # Soporta tablas, listas, definiciones, etc.
            "markdown.extensions.codehilite",  # Soporta bloques de código con estilos
            "markdown.extensions.nl2br",        # Salto de línea automático
            "markdown.extensions.sane_lists"    # Mejora las listas    
        ],
        
        output_format="html5"  # Utiliza etiquetas modernas HTML
    )
    
    tags_permitidos = [
        'p', 'strong', 'em', 'ul', 'ol', 'li',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'blockquote', 'code', 'pre', 'br', 'hr',
        'a', 'img'
    ]
    
    atributos_permitidos = {
        'a': ['href', 'title'],
        'img': ['src', 'alt', 'title'],
    }
    
    html_limpio = bleach.clean(
        html,
        tags=tags_permitidos,
        attributes=atributos_permitidos,
        strip=True  # Elimina etiquetas no permitidas en vez de escaparlas
    )
    
    return html_limpio
