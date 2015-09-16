from pprint import pprint

#Name, Distance, Apparent Brightness, Absolute Brightness
stars = [
('Alpha Centauri A',    4.3, 0.26,     1.56),
('Alpha Centauri B',    4.3, 0.077,    0.45),
('Alpha Centauri C',    4.2, 0.00001,  0.00006),
("Barnard's Star",      6.0, 0.00004,  0.0005),
('Wolf 359',            7.7, 0.000001, 0.00002),
('BD +36 degrees 2147', 8.2, 0.003,    0.006),
('Luyten 726-8 A',      8.4, 0.000003, 0.00006),
('Luyten 726-8 B',      8.4, 0.000002, 0.00004),
('Sirius A',            8.6, 1.00,     23.6),
('Sirius B',            8.6, 0.001,    0.003),
('Ross 154',            9.4, 0.0002,   0.0005),
]


dist = []
dist_sort = []
app = []
app_sort = []
abso = []
abs_sort = []

def sortList(z):
    for temp in range(1,4):
        if temp == 1:
            for a in range (0, len(z)):
                dist.append([z[a][temp], z[a][0]])
            dist_sort = sorted(dist)
        elif temp == 2:
            for b in range (0, len(z)):
                app.append([z[b][temp], z[b][0]])
            app_sort = sorted(app)
        elif temp == 3:
            for c in range (0, len(z)):
                abso.append([z[c][temp], z[c][0]])
            abs_sort = sorted(abso)
    
    for num in range(0, len(z)):
        dist_sort[num] = dist_sort[num][::-1]
        app_sort[num] = app_sort[num][::-1]
        abs_sort[num] = abs_sort[num][::-1]
    
    print 'Ranking by Distance:'
    pprint(dist_sort)
    print 'Ranking by Apparent Brightness:'
    pprint(app_sort)
    print 'Ranking by Absolute Brightness:'
    pprint(abs_sort)

sortList(stars)