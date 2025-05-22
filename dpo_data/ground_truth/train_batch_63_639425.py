import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().arc((5,8),(-6,-97),(49,-6)).arc((59,97),(5,8)).assemble().reset().face(w0.sketch().segment((18,46),(19,39)).segment((65,47)).segment((64,54)).close().assemble(),mode='s').finalize().extrude(-129).union(w0.workplane(offset=64/2).moveTo(-12,-9).cylinder(64,82))