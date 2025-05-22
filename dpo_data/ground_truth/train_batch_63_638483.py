import cadquery as cq
w0=cq.Workplane('YZ',origin=(17,0,0))
r=w0.workplane(offset=-34/2).box(200,50,34)