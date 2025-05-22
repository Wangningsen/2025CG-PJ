import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.workplane(offset=-160/2).moveTo(-53,13).cylinder(160,47).union(w0.sketch().segment((59,-60),(100,-60)).segment((100,-53)).segment((93,-53)).arc((92,-55),(91,-53)).segment((59,-53)).close().assemble().finalize().extrude(-19))