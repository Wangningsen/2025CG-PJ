import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-80,-34),(-50,-34)).segment((-37,-12)).segment((10,-41)).segment((10,-34)).segment((80,-34)).arc((50,-7),(10,6)).segment((10,41)).segment((-10,41)).segment((-10,6)).arc((-50,-7),(-80,-34)).assemble().finalize().extrude(200)