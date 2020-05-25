def create_options(attachments):
    options = []
    for attachment in attachments:
        line = {}
        line['label'] = attachment
        line['value'] = attachment
        options.append(line)
    return options

def cat_check(options, categories):
    print("OPTIONS")
    print(options)
    print("CATEGORIES")
    print(categories)
    for each in categories:
        try:
            options.remove(each)
        except:
            pass
    return options