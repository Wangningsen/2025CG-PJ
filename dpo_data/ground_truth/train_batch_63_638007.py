import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.sketch().segment((-55,-75),(-5,-100)).segment((26,-38)).arc((36,-28),(39,-14)).segment((55,18)).segment((5,44)).close().assemble().push([(0,-28)]).circle(24,mode='s').finalize().extrude(-160).union(w0.sketch().segment((-33,89),(-32,90)).segment((-29,87)).segment((-30,86)).arc((-21,97),(-33,89)).assemble().finalize().extrude(-78))