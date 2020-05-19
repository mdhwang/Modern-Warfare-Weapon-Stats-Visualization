def create_options(category, attachments):
    options = []
    for attachment in attachments:
        line = {}
        line['label'] = category + " - " + attachment
        line['value'] = attachment
        options.append(line)
    return options