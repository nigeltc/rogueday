import color

def render_bar(console, current_val, max_val, total_width):
    bar_width = int((float(current_val)/max_val) * total_width)
    console.draw_rect(x=0, y=45, width=20, height=1, ch=1, bg=color.bar_empty)
    if bar_width > 0:
        console.draw_rect(x=0, y=45, width=bar_width, height=1,
                          ch=1, bg=color.bar_filled)
    console.print(x=1, y=45, string=f"HP: {current_val}/{max_val}",
                  fg=color.bar_text)
