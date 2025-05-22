import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-78))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-91,-88),(26,-88)).segment((26,-100)).segment((91,-100)).segment((91,-71)).segment((23,-71)).segment((23,33)).segment((-91,33)).close().assemble().finalize().extrude(26).union(w1.workplane(offset=-26/2).moveTo(75,53).cylinder(26,25))