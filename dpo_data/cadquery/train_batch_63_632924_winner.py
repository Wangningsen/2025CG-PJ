import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().rect(122,200).circle(14,mode='s').finalize().extrude(-74)