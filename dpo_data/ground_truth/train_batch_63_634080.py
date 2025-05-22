import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().arc((31,2),(69,-24),(37,10)).arc((42,-1),(31,2)).assemble().finalize().extrude(-35).union(w0.sketch().segment((2,-27),(100,-27)).segment((100,9)).segment((2,9)).segment((2,-12)).close().assemble().finalize().extrude(8)).union(w0.sketch().push([(-49,0)]).circle(51).circle(48,mode='s').finalize().extrude(25))