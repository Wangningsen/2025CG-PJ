import cadquery as cq
w0=cq.Workplane('YZ',origin=(77,0,0))
r=w0.workplane(offset=-154/2).moveTo(-79,38).cylinder(154,21).union(w0.sketch().push([(72.5,-10.5)]).rect(55,97).reset().face(w0.sketch().segment((55,7),(57,7)).segment((57,8)).arc((59,11),(57,14)).segment((57,15)).segment((55,15)).segment((55,14)).arc((53,11),(55,8)).close().assemble(),mode='s').finalize().extrude(-19))