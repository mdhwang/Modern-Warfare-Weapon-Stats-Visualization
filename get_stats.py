def base_stats(df, weapon):
    base = df[(df.Weapon == weapon) & (df.Category == "BASE")].iloc[0,3:].tolist()
    return base

def attachment_stats(df, weapon, attachment):
    attachment = df[(df.Weapon == weapon) & (df.Attachment == attachment)].iloc[0,3:].tolist()
    return attachment

def aggregate(df, weapon, attachments):
    stats = df[(df.Weapon == weapon) & (df.Category == "BASE")].iloc[0,3:].tolist()
    for attachment in attachments:
        try:
            diff = df[(df.Weapon == weapon) & (df.Attachment == attachment)].iloc[0,3:].tolist()
            stats = [sum(i) for i in zip(stats, diff)]
        except:
            pass
    return stats
