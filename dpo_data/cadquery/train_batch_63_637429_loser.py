import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().arc((-44,-18),(-19,-10),(-11,-36)).arc((6,37),(-44,-18)).assemble().finalize().extrude(-90).union(w0.sketch().arc((74,-6),(100,25),(74,55)).segment((74,18)).segment((98,18)).segment((98,16)).segment((74,16)).close().assemble().finalize().extrude(75)).union(w0.workplane(offset=102/2).moveTo(-61,-16).cylinder(102,39)).union(w1.workplane(offset=29/2).moveTo(-61,-16).cylinder(29,30))