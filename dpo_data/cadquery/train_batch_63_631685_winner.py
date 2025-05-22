import cadquery as cq
w0=cq.Workplane('YZ',origin=(-67,0,0))
r=w0.workplane(offset=134/2).box(148,200,134)