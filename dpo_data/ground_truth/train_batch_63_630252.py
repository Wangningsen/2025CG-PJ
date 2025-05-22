import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
r=w0.workplane(offset=-68/2).moveTo(32.5,-75.5).box(125,49,68).union(w0.sketch().segment((-95,24),(-70,17)).segment((-70,8)).segment((-29,8)).segment((-29,78)).segment((-43,78)).segment((-39,90)).segment((-74,100)).close().assemble().finalize().extrude(-23))