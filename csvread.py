def fetch_url():

    import psycopg2
    conn = psycopg2.connect("dbname=djangodb host=localhost user=postgres password=nakadev")
    cur = conn.cursor()
    cur.execute("SELECT url FROM search_promotion;")
    temp = cur.fetchall()
    url_list = []
    for each in temp:
        url_list.append(each[0])
    return url_list


def csvread(filename, list_of_urls):

    from search.models import Promotion
    import csv

    f = open('csvfile/'+filename, 'r')
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if not row[2] in list_of_urls:
            print(row[2]+"を保存")
            p = Promotion(sponsored=row[1], url=row[2], date=row[3], title=row[4], content=row[5], site=row[6])
            p.save()
    f.close()
