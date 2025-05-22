import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().segment((26,-11),(28,-66)).segment((50,-65)).segment((48,-10)).close().assemble().push([(38,-38)]).circle(4,mode='s').finalize().extrude(-95).union(w0.sketch().arc((-71,-15),(62,-82),(14,62)).arc((3,74),(-9,82)).segment((-9,100)).segment((-58,100)).segment((-58,82)).arc((-90,41),(-71,-15)).assemble().finalize().extrude(35))