import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-70,-23),(-21,-70)).segment((70,23)).segment((21,70)).close().assemble().finalize().extrude(160).union(w0.sketch().circle(31).rect(16,34,mode='s').finalize().extrude(200))