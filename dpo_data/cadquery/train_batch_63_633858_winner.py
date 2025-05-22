import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
w1=cq.Workplane('YZ',origin=(30,0,0))
r=w0.workplane(offset=54/2).moveTo(-12,76.5).box(36,47,54).union(w1.workplane(offset=-29/2).moveTo(-65,-26).box(70,84,29))