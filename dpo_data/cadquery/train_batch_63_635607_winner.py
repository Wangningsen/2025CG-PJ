import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().segment((28,-35),(60,-100)).segment((99,-83)).segment((55,18)).arc((-90,59),(28,-35)).assemble().finalize().extrude(26)