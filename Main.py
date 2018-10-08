full_names = [u"Иванов Иван Иванович", u"Петров Петр Петрович"]
short_names = [' '.join([fn.split(' ')[0],fn.split(' ')[0][1]]) for fn in full_names]
