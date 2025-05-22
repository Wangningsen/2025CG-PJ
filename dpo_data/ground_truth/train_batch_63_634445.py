import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,87,0))
r=w0.sketch().segment((-100,-58),(-59,-58)).arc((0,-83),(59,-58)).segment((100,-58)).segment((100,58)).segment((59,58)).arc((0,83),(-59,58)).segment((-100,58)).close().assemble().finalize().extrude(-175)