import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().circle(100).rect(42,138,mode='s').finalize().extrude(158)