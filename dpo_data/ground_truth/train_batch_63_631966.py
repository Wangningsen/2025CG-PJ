import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.workplane(offset=-85/2).moveTo(-74,-1).cylinder(85,24).union(w0.sketch().segment((69,22),(96,5)).segment((98,8)).segment((70,25)).close().assemble().finalize().extrude(115))