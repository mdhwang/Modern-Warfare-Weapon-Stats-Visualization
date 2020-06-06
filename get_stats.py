import pandas as pd

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

def table_agg(df, weapon, attachemnts,categories):
    table = []
    base = df[(df.Weapon == weapon) & (df.Category == "BASE")].iloc[0,3:].tolist()
    base.insert(0,"STATS")
    base.insert(0,"BASE")
    table.append(base)
    final = df[(df.Weapon == weapon) & (df.Category == "BASE")].iloc[0,3:].tolist()
    for i, attachment in enumerate(attachemnts):
        try:
            diff = df[(df.Weapon == weapon) & (df.Attachment == attachment)].iloc[0,3:].tolist()
            final = [sum(i) for i in zip(final, diff)]
            diff.insert(0,attachment)
            diff.insert(0,categories[i])
            table.append(diff)
        except:
            pass
    final.insert(0,"STATS")
    final.insert(0,"FINAL")
    table.append(final)
    header = ["Category","Attachment",'Accuracy','Damage','Range','Fire Rate','Mobility','Control']
    pd_table = pd.DataFrame(table, columns = header)
    return pd_table
