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
    temp = 1
    while temp <= 3:
        if temp == 1:
            dist = [[z[a][temp], z[a][0]] for a in range(0, len(z))]
            dist_sort = sorted(dist)
        elif temp == 2:
            app = [[z[a][temp], z[a][0]] for a in range(0, len(z))]
            app_sort = sorted(app)
        elif temp == 3:
            abso = [[z[a][temp], z[a][0]] for a in range(0, len(z))]
            abs_sort = sorted(abso)
        temp += 1
    
    dist_sort = [dist_sort[num][::-1] for num in range(0, len(z))]
    app_sort = [app_sort[num][::-1] for num in range(0, len(z))]
    abs_sort = [abs_sort[num][::-1] for num in range(0, len(z))]
    
    print 'Ranking by Distance:'
    pprint(dist_sort)
    print 'Ranking by Apparent Brightness:'
    pprint(app_sort)
    print 'Ranking by Absolute Brightness:'
    pprint(abs_sort)

#dist_sort = [[num][::-1] for num in range(0, len(z))]    
sortList(stars)