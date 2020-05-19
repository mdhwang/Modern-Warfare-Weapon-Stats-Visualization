def create_options(attachments):
    options = []
    for attachment in attachments:
        line = {}
        line['label'] = attachment
        line['value'] = attachment
        options.append(line)
    return options