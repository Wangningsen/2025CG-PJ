import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('YZ',origin=(-14,0,0))
r=w0.sketch().segment((-64,-41),(-56,-46)).segment((-56,-74)).segment((-21,-74)).segment((-12,-80)).arc((50,-91),(48,-27)).segment((48,-26)).segment((40,-20)).segment((40,9)).segment((39,9)).segment((39,29)).segment((5,29)).segment((-3,35)).segment((-9,29)).segment((-56,29)).segment((-56,-29)).close().assemble().finalize().extrude(98).union(w1.sketch().segment((0,-26),(17,-26)).segment((17,-95)).segment((100,-95)).segment((100,16)).segment((0,16)).close().assemble().finalize().extrude(67))