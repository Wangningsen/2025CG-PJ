import cadquery as cq
w0=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().segment((28,-41),(28,-21)).segment((31,-21)).segment((28,-6)).segment((63,0)).segment((67,-21)).segment((79,-21)).arc((36,14),(28,-41)).assemble().finalize().extrude(-125).union(w0.workplane(offset=75/2).moveTo(-20,0).cylinder(75,60))