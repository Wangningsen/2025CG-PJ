import cadquery as cq
w0=cq.Workplane('YZ',origin=(-49,0,0))
w1=cq.Workplane('YZ',origin=(-48,0,0))
r=w0.workplane(offset=4/2).box(196,16,4).union(w0.workplane(offset=47/2).box(96,30,47)).union(w1.workplane(offset=103/2).box(58,200,103))