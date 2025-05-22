import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-65,58),(-47,42)).arc((-34,41),(-21,38)).segment((2,28)).segment((-6,5)).segment((36,5)).segment((36,-15)).segment((4,-15)).segment((65,-60)).arc((25,34),(-65,58)).assemble().finalize().extrude(200)