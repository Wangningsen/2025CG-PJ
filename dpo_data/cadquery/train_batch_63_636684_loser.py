import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
r=w0.workplane(offset=78/2).box(54,200,78)