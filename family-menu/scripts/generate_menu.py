#!/usr/bin/env python3
"""
Generate a beautiful family menu PDF for the week.
"""

import os
import random
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

class MenuDesign:
    """Different design styles for the menu."""
    
    # Design themes with color palettes and style attributes
    THEMES = {
        'fun_and_colorful': {
            'colors': {
                'bg': colors.HexColor('#FFF8DC'),
                'header': colors.HexColor('#FF6B6B'),
                'day': colors.HexColor('#4ECDC4'),
                'accent': colors.HexColor('#FFE66D'),
                'text': colors.HexColor('#2C3E50')
            },
            'fonts': {
                'title': ('FredokaOne-Regular', 36),
                'subtitle': ('Poppins-MediumItalic', 12),
                'day': ('Poppins-Bold', 14),
                'meal': ('Poppins-Regular', 11),
                'detail': ('Poppins-Light', 9)
            }
        },
        'clean_and_modern': {
            'colors': {
                'bg': colors.white,
                'header': colors.HexColor('#2C3E50'),
                'day': colors.HexColor('#3498DB'),
                'accent': colors.HexColor('#E74C3C'),
                'text': colors.black
            },
            'fonts': {
                'title': ('Poppins-Bold', 38),
                'subtitle': ('Poppins-Light', 12),
                'day': ('Poppins-Medium', 14),
                'meal': ('Poppins-Regular', 11),
                'detail': ('Poppins-LightItalic', 9)
            }
        },
        'rustic': {
            'colors': {
                'bg': colors.HexColor('#F5E6D3'),
                'header': colors.HexColor('#8B4513'),
                'day': colors.HexColor('#A0522D'),
                'accent': colors.HexColor('#CD853F'),
                'text': colors.HexColor('#3E2723')
            },
            'fonts': {
                'title': ('DejaVuSerif-Bold', 36),
                'subtitle': ('DejaVuSerif-Italic', 12),
                'day': ('DejaVuSerif-Bold', 14),
                'meal': ('DejaVuSerif', 11),
                'detail': ('DejaVuSerif-Italic', 9)
            }
        },
        'elegant': {
            'colors': {
                'bg': colors.HexColor('#FAFAFA'),
                'header': colors.HexColor('#1A1A1A'),
                'day': colors.HexColor('#4A4A4A'),
                'accent': colors.HexColor('#B8860B'),
                'text': colors.HexColor('#2C2C2C')
            },
            'fonts': {
                'title': ('PlayfairDisplay-Bold', 40),
                'subtitle': ('PlayfairDisplay-Regular', 12),
                'day': ('PlayfairDisplay-Bold', 14),
                'meal': ('PlayfairDisplay-Regular', 11),
                'detail': ('Lora-Italic-Variable', 9)
            }
        },
        'bold_and_playful': {
            'colors': {
                'bg': colors.HexColor('#FFF5E1'),
                'header': colors.HexColor('#E91E63'),
                'day': colors.HexColor('#9C27B0'),
                'accent': colors.HexColor('#FF9800'),
                'text': colors.black
            },
            'fonts': {
                'title': ('FredokaOne-Regular', 38),
                'subtitle': ('Poppins-Medium', 12),
                'day': ('FredokaOne-Regular', 13),
                'meal': ('Poppins-Medium', 11),
                'detail': ('Poppins-Light', 9)
            }
        }
    }

def register_fonts():
    """Register all available fonts."""
    fonts_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'fonts')
    
    # Get all .ttf files from the fonts directory
    registered_fonts = set()
    
    if os.path.exists(fonts_dir):
        for font_file in os.listdir(fonts_dir):
            if font_file.endswith('.ttf'):
                font_path = os.path.join(fonts_dir, font_file)
                font_name = font_file.replace('.ttf', '')
                try:
                    pdfmetrics.registerFont(TTFont(font_name, font_path))
                    registered_fonts.add(font_name)
                except Exception as e:
                    pass  # Skip if font registration fails
    
    return registered_fonts

def create_menu_pdf(menu_data, output_path, design_style=None):
    """
    Create a beautiful menu PDF.
    
    Args:
        menu_data: Dictionary with menu information
        output_path: Path where to save the PDF
        design_style: Optional specific design style, otherwise random
    """
    registered_fonts = register_fonts()
    
    # Choose design style
    if design_style is None or design_style not in MenuDesign.THEMES:
        design_style = random.choice(list(MenuDesign.THEMES.keys()))
    
    theme = MenuDesign.THEMES[design_style]
    
    # Validate and fallback fonts if needed
    def get_safe_font(font_name, fallback='Helvetica'):
        """Return font name if registered, otherwise fallback."""
        return font_name if font_name in registered_fonts else fallback
    
    # Create canvas
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Background
    c.setFillColor(theme['colors']['bg'])
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Header
    y_position = height - 1.2 * inch
    
    # Title
    title_font, title_size = theme['fonts']['title']
    title_font = get_safe_font(title_font, 'Helvetica-Bold')
    c.setFont(title_font, title_size)
    c.setFillColor(theme['colors']['header'])
    c.drawCentredString(width / 2, y_position, menu_data.get('title', 'This Week\'s Menu'))
    
    y_position -= 0.4 * inch
    
    # Subtitle with date range
    subtitle_font, subtitle_size = theme['fonts']['subtitle']
    subtitle_font = get_safe_font(subtitle_font, 'Helvetica')
    c.setFont(subtitle_font, subtitle_size)
    c.setFillColor(theme['colors']['text'])
    subtitle = menu_data.get('subtitle', f"Week of {datetime.now().strftime('%B %d, %Y')}")
    c.drawCentredString(width / 2, y_position, subtitle)
    
    # Decorative line
    y_position -= 0.3 * inch
    c.setStrokeColor(theme['colors']['accent'])
    c.setLineWidth(2)
    c.line(1.5 * inch, y_position, width - 1.5 * inch, y_position)
    
    # Menu items
    y_position -= 0.5 * inch
    meals = menu_data.get('meals', [])
    
    day_font, day_size = theme['fonts']['day']
    day_font = get_safe_font(day_font, 'Helvetica-Bold')
    meal_font, meal_size = theme['fonts']['meal']
    meal_font = get_safe_font(meal_font, 'Helvetica')
    detail_font, detail_size = theme['fonts']['detail']
    detail_font = get_safe_font(detail_font, 'Helvetica')
    
    for meal in meals:
        # Check if we need a new page
        if y_position < 2 * inch:
            c.showPage()
            c.setFillColor(theme['colors']['bg'])
            c.rect(0, 0, width, height, fill=1, stroke=0)
            y_position = height - 1 * inch
        
        # Day header
        c.setFont(day_font, day_size)
        c.setFillColor(theme['colors']['day'])
        c.drawString(1 * inch, y_position, meal.get('day', ''))
        
        y_position -= 0.05 * inch
        
        # Small accent line under day
        c.setStrokeColor(theme['colors']['accent'])
        c.setLineWidth(1.5)
        c.line(1 * inch, y_position, 3 * inch, y_position)
        
        y_position -= 0.25 * inch
        
        # Meal name
        c.setFont(meal_font, meal_size)
        c.setFillColor(theme['colors']['text'])
        meal_name = meal.get('name', '')
        c.drawString(1.2 * inch, y_position, f"• {meal_name}")
        
        y_position -= 0.2 * inch
        
        # Protein highlight (if exists)
        if 'protein' in meal and meal['protein']:
            c.setFont(detail_font, detail_size)
            c.setFillColor(theme['colors']['accent'])
            c.drawString(1.4 * inch, y_position, f"Protein: {meal['protein']}")
            y_position -= 0.18 * inch
        
        # Additional details (prep time, notes, etc.)
        if 'prep_time' in meal and meal['prep_time']:
            c.setFont(detail_font, detail_size)
            c.setFillColor(theme['colors']['text'])
            c.drawString(1.4 * inch, y_position, f"⏱ {meal['prep_time']}")
            y_position -= 0.18 * inch
        
        if 'notes' in meal and meal['notes']:
            c.setFont(detail_font, detail_size - 1)
            c.setFillColor(theme['colors']['text'])
            # Wrap notes if too long
            notes = meal['notes']
            if len(notes) > 60:
                notes = notes[:57] + "..."
            c.drawString(1.4 * inch, y_position, f"Note: {notes}")
            y_position -= 0.18 * inch
        
        # Space between meals
        y_position -= 0.15 * inch
    
    # Footer with design style credit
    c.setFont(detail_font, 7)
    c.setFillColor(theme['colors']['text'])
    footer_text = f"Menu style: {design_style.replace('_', ' ').title()} • Generated with ❤️"
    c.drawCentredString(width / 2, 0.5 * inch, footer_text)
    
    c.save()
    return design_style

if __name__ == "__main__":
    # Test example
    test_menu = {
        'title': 'Family Dinner Menu',
        'subtitle': f'Week of {datetime.now().strftime("%B %d, %Y")}',
        'meals': [
            {'day': 'Monday', 'name': 'Grilled Chicken with Roasted Vegetables', 'protein': 'Chicken breast', 'prep_time': '35 min'},
            {'day': 'Tuesday', 'name': 'Monday Leftovers', 'notes': 'Use remaining chicken and veggies'},
            {'day': 'Wednesday', 'name': 'Salmon with Quinoa and Asparagus', 'protein': 'Salmon fillet', 'prep_time': '25 min'},
            {'day': 'Thursday', 'name': 'Beef Stir-Fry', 'protein': 'Beef sirloin', 'prep_time': '30 min'},
            {'day': 'Friday', 'name': 'Homemade Pizza Night! 🍕', 'notes': 'Everyone makes their own pizza'},
            {'day': 'Saturday', 'name': 'Restaurant Night', 'notes': 'Try the new Italian place downtown'},
            {'day': 'Sunday', 'name': 'Slow Cooker Pot Roast', 'protein': 'Chuck roast', 'prep_time': '15 min prep, 6 hrs cooking'},
        ]
    }
    
    output = '/tmp/test_menu.pdf'
    style = create_menu_pdf(test_menu, output)
    print(f"Created test menu with '{style}' design at: {output}")
