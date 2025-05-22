import cadquery as cq
w0=cq.Workplane('YZ',origin=(-49,0,0))
w1=cq.Workplane('YZ',origin=(-48,0,0))
r=w0.sketch().rect(198,16).reset().face(w0.sketch().segment((40,-1),(42,-1)).segment((42,-4)).segment((48,-4)).segment((48,-1)).segment((50,-1)).segment((50,3)).segment((48,3)).segment((48,6)).segment((42,6)).segment((42,3)).segment((40,3)).close().assemble(),mode='s').finalize().extrude(-5).union(w0.workplane(offset=47/2).box(96,30,47)).union(w1.workplane(offset=103/2).box(58,200,103))