import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-80,-34),(-51,-34)).segment((-28,-17)).segment((-24,-21)).segment((10,-41)).segment((10,-34)).segment((80,-34)).arc((53,-9),(19,5)).segment((19,6)).segment((10,6)).segment((10,41)).segment((-10,41)).segment((-10,6)).segment((-19,6)).segment((-19,5)).arc((-53,-9),(-80,-34)).assemble().finalize().extrude(200)