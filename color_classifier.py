def color_classifier(segment):
    colors = {}
    values = ['border','base','boost','break','remain']
    for each in values:
        colors[each] = 0
        
    for each in segment:
        if each < 40:
            colors['border'] += 1
        elif each < 70:
            colors['remain'] += 1
        elif each < 110:
            colors['break'] += 1
        elif each < 145:
            colors['base'] += 1
        else:
            colors['boost'] += 1
    total = colors['base'] + colors['boost'] + colors['break'] + colors['remain']
    value = colors['base'] + colors['boost'] - colors['break']
    add = colors['boost']
    weak = colors['break']
    value_pct = round(value*100 / total,2)
    add_pct = round(add*100 / total,2)
    weak_pct = round(weak*100 / total,2)
    return value_pct, add_pct, weak_pct
            