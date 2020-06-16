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
            final = [round(sum(i),2) for i in zip(final, diff)]
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

    stats = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']
    for each in stats:
        string = each + "_color"
        # print(pd_table[each])
        pd_table[string] = color_selector(pd_table[each])
    return pd_table

def color_selector(column):
    try:
        colors = []
        col = column.to_list()
        values = col[1:-1]
        for value in values:
            if value > 0:
                colors.append("rgba(100, 200, 100,0.75)")
            elif value < 0:
                colors.append("rgba(250, 100, 100,0.75)")
            else:
                colors.append("rgb(200, 200, 200)")
        colors.insert(0,"rgb(200, 200, 200)")
        if col[-1] > col[0]:
            fin = "rgba(100, 200, 100,0.75)"
        elif col[-1] < col[0]:
            fin = "rgba(250, 100, 100,0.75)"
        else:
            fin = "rgb(200, 200, 200)"
        colors.append(fin)
        return colors
    except:
        return ["rgb(200, 200, 200)"] * len(column)